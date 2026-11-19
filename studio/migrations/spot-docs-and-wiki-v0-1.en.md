---
id: "MIG-SPOT-WIKI-001-EN"
entity_id: "MIG-SPOT-WIKI-001"
title: "SPOT decomposition and two wikis: migration record"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-19"
language: "en"
translation_of: "MIG-SPOT-WIKI-001"
translation_path: "studio/migrations/spot-docs-and-wiki-v0-1.md"
translation_status: "draft-unreviewed"
source: "TASK-SPOT-WIKI-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ РЕАЛИЗАЦИЯ"]
discussion_buckets: ["discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: decomposition, translation and navigation; model version not recorded; human review pending."
---

# SPOT decomposition and two wikis: migration record

**Draft · 0.1.0** · [Русский](spot-docs-and-wiki-v0-1.md) · [Project wiki](../navigation/en/README.md)

## Task and scope

Task owner: Alexander Yashin (`alexanderyashin`). Branch: `work/sasha/spot-docs-and-bilingual-wiki`. Base: `23d18f172cfee87129695c082f4846c1a00734e6`. The basis is Sasha's direct request to decompose SPOT into subject Draft documents, create Russian and English wikis, distinguish consensus/discussion/gaps, and document mandatory registration of every file.

This record documents working decomposition and navigation. It does not claim Ivan's approval or adoption of creative canon. The cataloguing standard and accompanying revisions remain Draft for review; new technical enforcement is outside scope.

## Source and completeness

The source is the supplied `Киберстолыпин_SPOT_v0_1.docx`, SHA-256 `22914491f0cdf1b901008457fb1397d0965c59d1e012c1d45afc06e5562897f9`. Its substance matches the structured source: 1,276 text atoms were checked. Title-page and packaging differences from the preceding export do not change the main text or tables.

All 25 chapters, 840 blocks, 56 CAN, 22 DIV, 60 GAP, 16 CHAR, 25 ARC and 10 PRI are represented in the working decomposition. The [block-level map](../navigation/spot-coverage.csv) identifies Russian and English destinations. The [subject index](../registers/content-index.csv) lists current documents. The [file catalogue](../navigation/file-catalog.csv) also includes infrastructure.

## Transformation map

| Previous location | Current destination | History preservation |
| --- | --- | --- |
| Immutable SPOT import | Source snapshot plus references from subject documents | Snapshot bytes unchanged |
| Broad government, economy, geography, technology and society chapters | Subject specifications split by logical subsection | Existing paths and IDs retained as indexes |
| 16 characters and 25 arcs | The same cards plus full English counterparts | Paths and subject IDs retained |
| CAN, DIV and GAP in the large source | Source-position groups, individual divergence cards and subject gap registers | Original registers and IDs retained; new fields point to working locations |
| Methodology, priorities, forms, glossary and sources | Separate documents under studio, production, templates, world and research | Original qualifications and editorial status retained |
| Incomplete navigation | `studio/navigation/ru/` and `studio/navigation/en/` | Existing entry points retained and linked |

No registered path or top-level area is deleted or renamed; `structure.json`, GitHub settings, tools and CI remain unchanged. New infrastructure folders for Draft documents use `proposals`, because the validator reserves `drafts/canon/archive` for registered creative areas. `status: draft` is retained. This placement does not alter the world's lifecycle.

## Languages and statuses

All new subject documents have full RU/EN text and reciprocal links. A shared `entity_id` connects them; an English edition's separate `id` ends in `-EN`. Exact source labels remain attached to statements. The requested `consensus`, `discussion` and `gap` categories are supplemented by `historical`, keeping earlier and cancelled versions distinct from active alternatives.

Fourteen CAN records carry source consensus, 35 are active discussion and seven are historical variants. No document is promoted to canon, no approval record is created, and no GAP/DIV is automatically closed.

## Checks and accompanying correction

The existing validator was actually run against the unchanged base and found five missing frontmatter blocks in existing project-log files. Only mandatory metadata was added; historical body text was preserved. This fixes a known technical defect without changing recorded decisions.

Final checking includes the existing validator against the base commit, no deletion or rewriting of protected material, complete source coverage, reciprocal language pairs, catalogue-to-file equality, and local links including anchors. Actual results are recorded in the handoff and PR; this plan alone is not evidence of a PASS.

## Rollback and continuation

Before merge, the working branch can remain under review without changing main. After adoption, rollback uses an ordinary revert commit preserving history; force push, archive deletion and rewriting other work are unnecessary. A substantive change updates the corresponding subject pair, then its catalogue entries and dependencies. New canon requires a separate decision under the existing rules.

## Observed checks of the working edition

On 2026-11-19 the existing validator completed against base `23d18f172cfee87129695c082f4846c1a00734e6`: **PASS, 678 files, 0 errors**. Independent source comparison covered 25 chapters, 840 blocks and 1,276 text atoms, with no omissions or double ownership. All 145 RU/EN pairs were checked and remain Draft. The wikis contain 28+28 pages and 2,805 internal links, with no missing files or anchors. Every one of the 678 files has a unique catalogue row and a direct link from each wiki. The one-off audit scripts are outside the repository; no permanent catalogue CI gate was added. These are technical and editorial checks, not human approval of canon or translations.
