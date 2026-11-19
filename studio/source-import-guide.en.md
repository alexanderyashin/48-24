---
id: "SPOT-IMPORT-GUIDE-001-EN"
entity_id: "SPOT-IMPORT-GUIDE-001"
title: "Working with the SPOT source and current documents"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-19"
language: "en"
translation_of: "SPOT-IMPORT-GUIDE-001"
translation_path: "studio/source-import-guide.md"
translation_status: "draft-unreviewed"
source: "TASK-SPOT-WIKI-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ РЕАЛИЗАЦИЯ"]
discussion_buckets: ["discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: decomposition, translation and navigation; model version not recorded; human review pending."
---

# Working with the SPOT source and current documents

**Draft · 0.1.0** · [Русский](source-import-guide.md) · [Project wiki](navigation/en/README.md)

## One current working edition per subject

Start with the [Russian wiki](navigation/ru/README.md) or [English wiki](navigation/en/README.md). The [subject index](registers/content-index.csv) connects each ID to its current RU/EN documents. The [file catalogue](navigation/file-catalog.csv) also registers instructions, templates, registers, configuration, code and navigation files themselves.

Specifications stay in subject areas. The former broad chapters on government, economy, geography, technology and society remain at their old paths as indexes to their child specifications. Characters CHAR001–CHAR016 and storylines ARC001–ARC025 retain their working paths and IDs. Edit a subject's own card, not a copy in the wiki.

## Source and derivatives

The [SPOT 0.1 import](../world/world-bible/drafts/spot-0-1-import.md) remains an immutable historical snapshot for checking context, attribution and source wording. New plot decisions do not belong inside that snapshot. A technical import correction requires an explicit description and must not change the original meaning.

The decomposition covers all 25 chapters. The [coverage map](navigation/spot-coverage.csv) assigns every one of the 840 source blocks to one current Russian document and its full English translation. It covers tables, lists, methodology, templates, glossary, sources, priorities and introductory qualifications, not only narrative material.

A card begins with preserved source wording and then develops independently. Revising a working card does not rewrite history. Distinguish the source, current edition and editorial alternatives explicitly. “Cyberstolypin” in source text is an earlier working name; the repository's current working designation is 48/24, and the final brand is not approved.

## Status and the scope of agreement

Every extracted document remains Draft. CAN, DIV, GAP, CHAR, ARC and PRI retain their IDs and authorial statuses. Consensus concerns a particular source statement; it is not new agreement by both coauthors with an entire document. Proposals, joint development, editorial recommendations, earlier versions and cancelled alternatives must not be collapsed into “approved”.

The [original CAN register](registers/decisions.csv) and [GAP/DIV register](registers/open-questions.csv) are retained. New `working_path_ru` and `working_path_en` fields point to current documents; provenance fields continue to point to the snapshot. Closing a question or promoting a document to canon follows the separate [canon policy](CANON_POLICY.md).

## Bilingual work

New documents have a full `.en.md` counterpart, shared `entity_id`, unique technical language-edition IDs and reciprocal links. Translations are marked `draft-unreviewed`. Structural checking is not presented as human acceptance of meaning. Content changes require both editions to be updated; unresolved translation ambiguity must be explicit.

Machine-readable CSV/JSON remains a shared data structure; substantive translations live in the linked documents and two wikis. Older files outside this decomposition may retain language debt, recorded in the file catalogue. A short English link description does not conceal the lack of a full translation.

## Sources and limitations

Historical references retain SPOT's qualifications; this migration did not research them afresh. П1–П7 and Р1 identify foundations described in the source document. Original private correspondence is not published. A new historical assertion requires its own source and verification; an invented event requires its own authorial decision.

The documents and wikis contain spoilers, alternative endings and unselected story variants. A public repository makes them neither canon nor freely licensed material. Public descriptions of a work are prepared separately with regard to status, provenance and rights rules.
