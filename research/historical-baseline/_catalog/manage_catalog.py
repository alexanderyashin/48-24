#!/usr/bin/env python3
"""Validate the source-planning tables and rebuild their deterministic CSV views.

Run from any directory. --check compares generated files without changing them.
The six tables declared in catalog-schema.json are the editable source of truth.
No network access, package installation or historical extraction is performed.
"""
import argparse
import csv
import io
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

CAT = Path(__file__).resolve().parent
BASE = CAT.parent

def csv_text(fields, rows):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n', extrasaction='raise')
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate and compare generated files without writing.')
    args = parser.parse_args()
    schema = json.loads((CAT / 'catalog-schema.json').read_text(encoding='utf-8'))
    taxonomy = json.loads((BASE / 'taxonomy.json').read_text(encoding='utf-8'))
    errors = []
    tables = {}
    for name, spec in schema['tables'].items():
        with (CAT / name).open(encoding='utf-8', newline='') as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != spec['fields']:
                errors.append(f'{name}: header differs from catalog-schema.json')
            rows = list(reader)
        tables[name] = rows
        identifiers = set()
        for number, row in enumerate(rows, 2):
            if None in row or any(v is None for v in row.values()):
                errors.append(f'{name}:{number}: malformed CSV row')
                continue
            key = row[spec['primary_key']]
            if not key or key in identifiers:
                errors.append(f'{name}:{number}: missing or duplicate primary key {key!r}')
            identifiers.add(key)
            for field in spec['required']:
                if not row[field].strip():
                    errors.append(f'{name}:{number}: required field {field} is empty')
            for field, value in row.items():
                if field.endswith('_url') and value and (urlsplit(value).scheme not in {'http','https'} or not urlsplit(value).netloc):
                    errors.append(f'{name}:{number}: invalid URL in {field}')
                if field not in {'canonical_url','verification_url','checked_url','license_url','result_urls_json'} and re.search('[А-Яа-яЁё]', value):
                    errors.append(f'{name}:{number}: non-English Cyrillic prose in {field}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1

    sources = {s['source_id']:s for s in tables['sources.csv']}
    maps = tables['source-topic-map.csv']
    gaps = tables['research-gaps.csv']
    evidence = tables['evidence-log.csv']
    topics = {}
    folders = {}
    for domain in taxonomy['domains']:
        dp = domain['slug']
        folders[dp] = []
        for group in domain['groups']:
            gp = f"{dp}/{group['slug']}"
            folders[gp] = []
            for topic in group['topics']:
                path = f"{gp}/{topic['slug']}"
                if path in topics:
                    errors.append(f'taxonomy.json: duplicate topic {path}')
                topics[path] = (domain['title_en'],group['title_en'],topic['title_en'])
                folders[path] = [path]
                folders[gp].append(path)
                folders[dp].append(path)
                if not (BASE / path / 'README.md').is_file():
                    errors.append(f'{path}: README.md missing')
    by_topic = defaultdict(list)
    by_source = defaultdict(set)
    for row in maps:
        if row['topic_path'] not in topics:
            errors.append(f"{row['mapping_id']}: unknown topic {row['topic_path']}")
        if row['source_id'] not in sources:
            errors.append(f"{row['mapping_id']}: unknown source {row['source_id']}")
        if row['extraction_status'] != 'not-started':
            errors.append(f"{row['mapping_id']}: this phase permits source plans only")
        if row['priority'] not in {'high','medium','low'}:
            errors.append(f"{row['mapping_id']}: invalid priority")
        by_topic[row['topic_path']].append(row)
        by_source[row['source_id']].add(row['topic_path'])
    evidence_counts = Counter(row['source_id'] for row in evidence)
    for row in evidence:
        if row['source_id'] not in sources:
            errors.append(f"{row['evidence_id']}: dangling source")
    for row in gaps:
        if row['topic_path'] not in topics:
            errors.append(f"{row['gap_id']}: unknown topic")
        if row['status'] not in {'open','resolved'}:
            errors.append(f"{row['gap_id']}: invalid status")
    for sid, source in sources.items():
        role_admission = {
            'scholarly-analysis':'accepted-for-source-planning',
            'edited-primary-source':'accepted-for-source-planning',
            'primary-document-or-object':'accepted-for-source-planning',
            'scientific-data':'accepted-for-source-planning',
            'reference-collection-or-series':'discovery-route-only',
            'discovery-index':'discovery-route-only',
            'method-support':'method-support-only',
        }
        if source['source_role'] not in role_admission or source['admission_status'] != role_admission.get(source['source_role']):
            errors.append(f'{sid}: invalid or inconsistent source_role/admission_status')
        if not re.fullmatch(r'HBS-[A-Z]+-\d{4}', sid):
            errors.append(f'{sid}: invalid source ID')
        if not by_source[sid] or not evidence_counts[sid]:
            errors.append(f'{sid}: needs both a planned use and verification evidence')
        if source['needs_item_selection'] not in {'true','false'}:
            errors.append(f'{sid}: needs_item_selection must be a lowercase boolean')
        if source['human_review_status'] != 'pending':
            errors.append(f'{sid}: human approval cannot be inferred in this source-discovery pass')
        if source['license_status'] != 'not-established' and not source['license_url']:
            errors.append(f'{sid}: a recorded rights statement needs its verification URL')
        for key in ('coverage_start','coverage_end'):
            if source[key] and not source[key].isdigit():
                errors.append(f'{sid}: {key} must be an integer year or empty')
        if source['coverage_start'] and source['coverage_end'] and int(source['coverage_start']) > int(source['coverage_end']):
            errors.append(f'{sid}: reversed coverage interval')
        try:
            date.fromisoformat(source['verified_on'])
        except ValueError:
            errors.append(f'{sid}: invalid verification date')
    seen_urls = {}
    for sid, source in sources.items():
        url = source['canonical_url'].rstrip('/').lower()
        if url in seen_urls:
            errors.append(f'{sid}: canonical URL duplicates {seen_urls[url]}; resolve identity or qualify the record')
        seen_urls[url] = sid
    for row in tables['source-id-aliases.csv']:
        if row['retired_source_id'] in sources or row['canonical_source_id'] not in sources:
            errors.append('source-id-aliases.csv: invalid alias endpoints')
    for row in tables['search-log.csv']:
        try:
            urls = json.loads(row['result_urls_json'])
            assert isinstance(urls, list) and all(isinstance(u,str) and urlsplit(u).scheme in {'http','https'} for u in urls)
        except (ValueError,AssertionError):
            errors.append(f"{row['search_id']}: result_urls_json must be a JSON URL array")
        for sid in re.findall(r'HBS-[A-Z]+-\d{4}', row['selected_source_ids']):
            if sid not in sources:
                errors.append(f"{row['search_id']}: selected source {sid} is missing")
    for path in topics:
        if not by_topic[path]:
            errors.append(f'{path}: no source plan')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1

    generated = {}
    view_fields = schema['derived_tables']['source-plan.csv']
    views = {}
    for path in topics:
        rows = []
        for mapping in sorted(by_topic[path], key=lambda m:(m['source_id'],m['mapping_id'])):
            source = sources[mapping['source_id']]
            rows.append({field: mapping[field] if field in mapping else source[field] for field in view_fields})
        views[path] = rows
    for folder, children in sorted(folders.items()):
        rows = [row for path in sorted(children) for row in views[path]]
        generated[BASE / folder / 'source-plan.csv'] = csv_text(view_fields,rows)
    gap_counts = Counter(g['topic_path'] for g in gaps if g['status']=='open')
    coverage = []
    for path, labels in sorted(topics.items()):
        subset = {m['source_id']: sources[m['source_id']] for m in by_topic[path]}
        roles = Counter(s['source_role'] for s in subset.values())
        specific = sum(s['admission_status']=='accepted-for-source-planning' for s in subset.values())
        discovery = sum(s['admission_status']=='discovery-route-only' for s in subset.values())
        research_status = 'source-plan-recorded; extraction-not-started' if specific else ('discovery-routes-only; item-review-required' if discovery else 'method-support-only; calculation-input-review-required')
        coverage.append(dict(topic_path=path,domain_title=labels[0],group_title=labels[1],topic_title=labels[2],unique_source_count=len(subset),
          specific_source_count=specific,discovery_source_count=discovery,scholarly_source_count=roles['scholarly-analysis'],primary_source_count=roles['primary-document-or-object']+roles['edited-primary-source'],scientific_data_source_count=roles['scientific-data'],method_source_count=roles['method-support'],open_gap_count=gap_counts[path],research_status=research_status))
    generated[CAT / 'coverage.csv'] = csv_text(schema['derived_tables']['coverage.csv'],coverage)
    index = [dict(source_id=sid,title=s['title'],canonical_url=s['canonical_url'],mapped_topic_count=len(by_source[sid]),topic_paths_json=json.dumps(sorted(by_source[sid]),ensure_ascii=False,separators=(',',':')),evidence_check_count=evidence_counts[sid],source_role=s['source_role'],admission_status=s['admission_status'],human_review_status=s['human_review_status']) for sid,s in sorted(sources.items())]
    generated[CAT / 'source-plan-index.csv'] = csv_text(schema['derived_tables']['source-plan-index.csv'],index)
    summary = dict(schema_version=2,research_stage='source-discovery-and-extraction-planning',historical_fact_extraction_started=False,metadata_language='English',scope_start=1910,scope_end=1940,last_source_check=max(s['verified_on'] for s in sources.values()),source_count=len(sources),source_role_counts=dict(sorted(Counter(s['source_role'] for s in sources.values()).items())),admission_status_counts=dict(sorted(Counter(s['admission_status'] for s in sources.values()).items())),domain_count=len(taxonomy['domains']),group_count=sum(len(d['groups']) for d in taxonomy['domains']),topic_count=len(topics),topic_count_with_source_plan=len(by_topic),topic_count_with_only_discovery_routes=sum(r['specific_source_count']==0 and r['discovery_source_count']>0 for r in coverage),topic_count_with_only_method_support=sum(r['specific_source_count']==0 and r['discovery_source_count']==0 for r in coverage),mapping_count=len(maps),evidence_check_count=len(evidence),logged_query_count=sum(r['action_type']=='web-search' for r in tables['search-log.csv']),research_log_record_count=len(tables['search-log.csv']),open_gap_count=sum(g['status']=='open' for g in gaps),folder_source_plan_count=len(folders),human_review_status='pending',exhaustive_bibliography_claim=False,unknown_reuse_licence_count=sum(s['license_status']=='not-established' for s in sources.values()))
    generated[CAT / 'catalog-status.json'] = json.dumps(summary,ensure_ascii=False,indent=2)+'\n'
    stale = []
    for path,content in generated.items():
        if args.check:
            if not path.is_file() or path.read_text(encoding='utf-8')!=content:
                stale.append(str(path.relative_to(BASE)))
        else:
            path.write_text(content,encoding='utf-8')
    if stale:
        print('Stale generated files:\n'+'\n'.join(stale),file=sys.stderr)
        return 1
    print(json.dumps(dict(result='PASS',mode='check' if args.check else 'build',sources=len(sources),topics=len(topics),mappings=len(maps),generated_files=len(generated))))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
