---
id: "NAV-CATALOGUE-001-EN"
entity_id: "NAV-CATALOGUE-001"
title: "Mandatory file cataloguing and bilingual navigation"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-19"
language: "en"
translation_of: "NAV-CATALOGUE-001"
translation_path: "studio/navigation/proposals/cataloguing-standard-v0-1.md"
translation_status: "draft-unreviewed"
source: "TASK-SPOT-WIKI-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ РЕАЛИЗАЦИЯ"]
discussion_buckets: ["discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: decomposition, translation and navigation; model version not recorded; human review pending."
---

# Mandatory file cataloguing and bilingual navigation

**Draft · 0.1.0** · [Русский](cataloguing-standard-v0-1.md) · [Project wiki](../en/README.md)

## 1. Purpose and scope

Every project file must have its own entry in the shared catalogue and be reachable from both language wikis. A directory, a list of extensions or an “everything inside” entry does not replace file-level registration. Sasha requested this requirement when commissioning the SPOT decomposition and wikis; this document records it as Draft. It does not establish creative canon or the second coauthor's agreement.

The requirement applies to new and changed materials in this task. Its adoption as a permanent project rule is proposed for review. Enforcement is currently **normative**: the person making a change and its reviewer perform the check. This work introduces no new CI, pre-commit hook, merge block or software scanner.

Scope includes every Git-tracked file: prose, READMEs, translations, images, code, tests, configuration, GitHub files, registers, templates, rights documents, source snapshots, archives, asset sidecars, and the wiki and catalogue files themselves. There are no exceptions based on extension, size, hidden name or status. Git internals and temporary execution-environment files unrelated to the project are not project files. External storage does not remove registration duties: a project master receives an asset record and individual reference in the asset register; the catalogue lists that record and links it to the external object. Confidential materials and secrets must still not be published.

## 2. One registration point

`studio/navigation/file-catalog.csv` is the complete file-level catalogue of the current working version. `studio/registers/content-index.csv` is the subject index of working documents. They have different purposes: the former establishes that a file is registered; the latter locates where a particular subject is edited. The wiki provides navigation and links to these records without creating a competing edition of the lore.

Each subject has one current working location per language. The source SPOT remains an immutable provenance snapshot. Its earlier formulations are not synchronised with revised cards. A translation is a language version of the same entity, not a separate creative alternative. An independent alternative receives its own ID and an explicit link to the choice being considered.

## 3. File entry fields

| Field | Requirement |
| --- | --- |
| `file_id` | Stable catalogue-entry ID, retained when the same file is renamed or moved. |
| `path` | Exact case-sensitive repository-relative path; one current row per existing file. |
| `document_id`, `entity_id` | IDs of the language edition and shared entity where assigned; do not invent a creative ID for infrastructure. |
| `kind`, `lifecycle`, `authority` | Type, work status and role: editable document, index, historical snapshot, instruction, template, data or tool. |
| `language`, `translation_path`, `translation_state` | Language, exact counterpart path and translation state. Latin characters alone do not demonstrate a complete English version. |
| `source_statuses`, `discussion_buckets` | Original authorial statuses and navigation categories; empty where inapplicable. |
| `owner`, `origin` | Explicitly assigned responsible person and provenance. An unknown owner remains `unassigned`; no silent assignment. |
| `summary_ru`, `summary_en` | Brief purpose in both languages. |
| `ru_wiki`, `en_wiki` | Pages in both wikis containing a direct link to the file. |

Machine-readable values use a shared vocabulary across both wikis. CSV/JSON files are not duplicated into independently edited language copies. Their fields and values are explained in both languages; substantive translated records are supplied by the corresponding documents. Until a separate general language decision, this is a migration convention, not an exemption from translating content.

## 4. Two independent statuses

`draft` describes a document's work status. Original `CONSENSUS` describes acceptance of a specific formulation in SPOT. Adding a file to Git, cataloguing, translation or merging a PR does not promote it to `canon`.

| Wiki category | Included material | It does not establish |
| --- | --- | --- |
| Source consensus / `consensus` | Only statements originally labelled КОНСЕНСУС | New approval of the whole document or every detail |
| Discussion / `discussion` | Sasha's frame, jointly developed material, author proposals, editorial proposals and divergences | Agreement through silence |
| Open gap / `gap` | Explicitly missing information and decisions | Permission to choose any convenient answer |
| Variant history / `historical` | Earlier and cancelled decisions | That an earlier version is still an active proposal |

A document may belong to several categories. The precise label on a paragraph or record governs its meaning; a file-level filter does not replace it. All ten original authorial statuses are retained. Discussion, approval, historical accuracy, translation readiness and asset rights remain separate attributes.

## 5. Language editions

This migration retains existing Russian paths and uses the `.en.md` suffix for English counterparts. A pair shares an `entity_id`; the English edition's unique `id` ends in `-EN`, preserving the existing uniqueness check for `id` + `version`. `translation_of` and `translation_path` connect editions in both directions. This distinguishes language records without creating separate CAN/CHAR/ARC or other subject entities.

Both editions must convey the same constraints, alternatives, sources and uncertainty. A translation must not be reduced to an abstract. IDs, source codes П1–П7, Р1, ИСТ and relationships between cards are neither translated nor renumbered. Disputed meaning is checked against the authorial formulation; neither Russian nor English has automatic precedence.

New pairs are marked `draft-unreviewed`: full translations exist, but human acceptance is not claimed. Explicit translation debt is allowed for unrelated legacy documents and is visible in the catalogue. A missing translation neither deletes an existing file nor makes the wiki complete in the sense of an approved canon.

## 6. Addition and revision

1. Find the subject, ID, current edition and active task through the wiki and subject area.
2. Create or update the document in its subject directory with the correct work status.
3. Update both language editions and reciprocal links; explicitly record any unfinished translation.
4. Add or update individual entries in the file catalogue and subject index.
5. Add direct links in both wikis and preserve sources, open questions and dependencies.
6. Compare the change set with the catalogue, check links and run the existing validator, recording actual results.

A change is not ready for handoff while any included file remains unregistered. New catalogue files themselves must also be registered. The one-off completeness check for this migration does not establish a permanent enforcement mechanism.

## 7. Moves, archives and deletion

A move retains `file_id`, subject ID, history, provenance and the language pairing; paths, incoming links and catalogue entries are updated. Replacing a substantive edition requires reasons, a successor and dependencies under the existing archive rules. Archived files remain catalogued.

The current catalogue lists existing files rather than broken links to removed paths. Migration records and Git preserve movement history. Removing a protected path or changing `structure.json`, canon or archives still requires the existing approvals. This document does not authorise bypassing them.

## 8. Two wiki structures

The wikis live in `studio/navigation/ru/` and `studio/navigation/en/`. Each has its own home, subject pages, status views, sources and complete file catalogue. Navigation leads to the full edition in the selected language where available; otherwise it explicitly states the source language and outstanding translation.

Each subject specification stays in its own area and is linked from the wiki. The wiki may offer orientation and lists but does not replace full documents. An older path may remain as a subject index to preserve existing links, explicitly identifying where the content is now edited.

## 9. SPOT completeness

`studio/navigation/spot-coverage.csv` maps each source block from the 25 chapters to one current Russian document and its English counterpart. It covers paragraphs, headings, tables, list items and source links. Characters, arcs, CAN, DIV, GAP and PRI retain their original IDs. Source overview tables may repeat record titles; this is not a second editable edition of their substantive content.

Source text, mappings and Git make the transfer auditable. A mapping row does not establish translation quality, which requires substantive comparison. Creating a well-presented document for an open question does not close that question.

## 10. Responsibility and acceptance

The contributor is responsible for registering every file and accurately describing completed work. The reviewer checks completeness, subject placement, statuses, links and translation equivalence. The catalogue neither assigns intellectual property, replaces an asset sidecar nor proves a person's consent.

Acceptance of this migration concerns whether the organisation and navigation support collaboration. Individual canon statements, the final title, audience, revolution chronology and other open creative decisions require their own approvals.
