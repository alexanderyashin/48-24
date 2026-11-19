---
id: "MIG-OPEN-QUESTIONS-001-EN"
entity_id: "MIG-OPEN-QUESTIONS-001"
title: "Unified question register: change record"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-20"
language: "en"
translation_of: "MIG-OPEN-QUESTIONS-001"
translation_path: "studio/migrations/open-question-register-v0-1.md"
translation_status: "draft-unreviewed"
source: "TASK-OPEN-QUESTIONS-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ ФИКСАЦИЯ"]
discussion_buckets: ["gap", "discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: open-question audit and navigation update; historical source body retained; human review pending."
authority: "migration-draft"
---

# Unified question register: change record

**Draft** · [Русский](open-question-register-v0-1.md)

## Task and starting state

Task: collect unfinished and unclear matters in one subject-organised register, identifying exact documents and required additions for each answer. This continues SPOT decomposition on `work/sasha/spot-docs-and-bilingual-wiki`, [Draft PR #5](https://github.com/alexanderyashin/48-24/pull/5). The starting revision is `f33a3c08c88b43b165d57f74e8eaf9f37f5c15e3`.

Before this change, the CSV held 82 source GAP/DIV records. Its working_path fields pointed to question cards; seven PM-Q records had a separate current-state table. Not all substantive outstanding work and language debt were explicitly registered.

## Changes

- One master register: **183 records**—82 source GAP/DIV, 7 PM-Q and 94 new OQ. Original GAP/DIV IDs and substantive formulations are retained.
- **17 subject areas** and narrower topics; **147 open, 35 deferred, 1 resolved**. Conditional tasks have activation conditions.
- **981 “question → document/language pair → required action” relationships** in a separate normalised table. It is not a second question register.
- Two full language views, topic pages, an index of every ID and a reverse document index. Older GAP/DIV cards link to current records; the PM log now acts as an index.
- Maintenance rules define evidence-based closure, required checks of associated documents, a justified “verified, no change needed” outcome and separate Draft, question-state and source-agreement tracking.

## Audit limits

Additional OQ records capture observed outstanding matters; they are not new authorial decisions. No creative alternative is selected and no external research verifies historical or technical hypotheses. Missing translations and human acceptance are represented by subject packages listing exact files. Optional storylines and adaptations are developed only when their stated condition is met.

Only PM-Q007's stale blocker is resolved, supported by a [successful GitHub Actions run](https://github.com/alexanderyashin/48-24/actions/runs/44629578628) for the starting revision. Dated follow-ups are appended to historical logs; earlier network-failure records remain. The game pipeline, importers and physics tests remain separate questions.

## Registration and verification

All new and changed files are included in the individual catalogue and both wiki link sets. Cataloguing remains normative; this task changes no CI, hooks, manifest, rights, immutable SPOT or canon-approval records.

Actual checks of this edition are recorded below and in the PR after execution. Link checks do not establish human translation acceptance. The register and every new specification remain Draft.

<!-- oq-observed-checks:start -->

## Observed checks — 2026-11-20

- Existing `python tools/validate_repo.py --base 23d18f172cfee87129695c082f4846c1a00734e6`: **PASS, 721 files, 0 errors**.
- `git diff --check`: **PASS**.
- One-off data audit: **183 unique questions**, all 82 source GAP/DIV and all 7 PM-Q retained; **981 relationships** to **701 existing files**. Every primary destination matches the relationship table; RU/EN fields, criteria, conditions and closure evidence are present.
- Both wikis contain **47 + 47 pages**; **11,530 internal links**, no errors. An additional check of every changed and new Markdown file covered **11,737 links**, no errors.
- Catalogue: **721 individual entries = 721 existing files**; every file has a direct link from both wikis.
- The historical SPOT, manifest, CI, tools, licence and canon-approval records are unchanged. Subject routing was reviewed independently from link validation; findings concerning criterion-language scope, infection, medical dependencies and production parameters were corrected.

These checks concern the prepared working edition. GitHub CI for the published commit is tracked separately in the PR; a local PASS does not substitute for the server run.

<!-- oq-observed-checks:end -->
