# Historical source catalogue

This catalogue is the English-language source inventory for the 1910–1940 historical baseline. It records what to investigate and where; historical extraction has not started.

## Authoritative tables

| Table | Editable content |
| --- | --- |
| [sources.csv](sources.csv) | One record per distinct source, edition, dataset or discovery route; stable source IDs |
| [source-topic-map.csv](source-topic-map.csv) | One row per planned use of a source in a specific topic |
| [evidence-log.csv](evidence-log.csv) | Evidence of bibliographic, scope, access and rights checks |
| [research-gaps.csv](research-gaps.csv) | Unresolved research requirements, with exact topic paths |
| [search-log.csv](search-log.csv) | Queries, selection decisions and retained result routes |
| [source-id-aliases.csv](source-id-aliases.csv) | Retired duplicate IDs and their retained canonical record |

## Generated views

| View | Meaning |
| --- | --- |
| [source-plan-index.csv](source-plan-index.csv) | All destination topics for each source |
| [coverage.csv](coverage.csv) | Per-topic counts, source roles and open explicit gaps |
| [catalog-status.json](catalog-status.json) | Current counts and stage; never a claim of exhaustive factual coverage |
| `source-plan.csv` in each subject folder | Join of source metadata with all plans belonging to that folder or its descendant topics |

Derived files must not be hand-edited. Run `python research/historical-baseline/_catalog/manage_catalog.py` after editing authoritative tables; use `--check` to validate without writing. The script uses only the Python standard library and does not fetch or extract source material.

## Documentation

- [Research protocol and provenance](research-protocol.md)
- [Data dictionary](data-dictionary.csv) and [table schema](catalog-schema.json)
- [Metadata vocabulary](metadata-vocabulary.md)
- [Source intake requirements](intake-checklist.md)
- [Rights and provenance](rights-and-provenance.md)
- [Tabular source-record template guidance](source-card-template.md)
- [Subject taxonomy](../taxonomy.json) and [main navigation](../README.md)

IDs use `HBS-<stream>-<four digits>`. The stream prefix records research provenance, not exclusive subject ownership. Cross-topic use points to the same source ID. Never recycle an ID or silently substitute a new edition or dataset version under an old one.
