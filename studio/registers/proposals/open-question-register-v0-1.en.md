---
id: "REG-OPEN-QUESTIONS-001-EN"
entity_id: "REG-OPEN-QUESTIONS-001"
title: "Unified open-question register: maintenance rules"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-20"
language: "en"
translation_of: "REG-OPEN-QUESTIONS-001"
translation_path: "studio/registers/proposals/open-question-register-v0-1.md"
translation_status: "draft-unreviewed"
source: "TASK-OPEN-QUESTIONS-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ ФИКСАЦИЯ"]
discussion_buckets: ["gap", "discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: repository audit, question routing and full translation; human review pending."
authority: "governance-draft"
---

[Русский](open-question-register-v0-1.md)

# Unified open-question register: maintenance rules

**Draft.** This working specification implements Sasha's request to collect unfinished and unclear matters in one register and give exact documents to update for every item. It does not approve creative decisions, assign contributors or replace the existing canon-approval policy.

## 1. One question record, several views

The primary question record and its current state live only in [open-questions.csv](../open-questions.csv). Relationships of “question → document → required change” live in [open-question-targets.csv](../open-question-targets.csv). This second table is a relationship to the same ID, not a second question register.

The [Russian wiki](../../navigation/ru/open-questions/README.md) and [English wiki](../../navigation/en/open-questions/README.md) are full language views of this shared data. Topic pages, status lists and the reverse document index are updated with the CSV files. They have no independent states and do not accept separate answers.

DIV cards, original GAP tables and the former PM log retain provenance and earlier wording. Check current openness in the unified register; write the actual answer in the subject specifications listed for the question. Do not edit the immutable SPOT import.

## 2. What warrants a separate question

A separate ID represents a verifiable decision, investigation, unfinished task or human review. “Develop the world” is not precise enough. The record must explain what is unknown, the evidence for that uncertainty and the result that permits closure.

Before adding an item, look for an existing GAP, DIV, PM-Q or OQ. For the same question, extend its relationships and editing destinations. For an independently answerable detail within a broad question, add a linked child record; closing the detail does not automatically close its parent. An empty directory, optional template or missing asset does not itself create an obligation to produce anything.

Original GAP001–GAP060, DIV001–DIV022 and PM-Q001–PM-Q007 retain their IDs. New audit findings receive sequential OQ-0001 IDs onwards; numbers are never reused. OQ does not imply a SPOT origin or authorial agreement.

## 3. Subject structure

Each record has one principal `category` and a narrower `topic_ru` / `topic_en`. Cross-domain effects are represented by additional editing destinations and relationships to other IDs, not by copies of the same question in several registers. The wiki provides both topic navigation and a reverse “document → questions” index.

`kind` describes the required work: `gap` for a missing decision; `divergence` for choosing or consolidating alternatives; `research` for verifying foundations; `review` for substantive review and acceptance; `task` for unfinished work. It is not a canon status.

## 4. States and activation conditions

| Value | Meaning and required condition |
| --- | --- |
| `open` | The question remains open. An owner and deadline may be unassigned. |
| `in-progress` | Work has actually started; the responsible person and a working-change link are recorded. |
| `blocked` | A specific obstacle is named, with the action that can remove it. |
| `deferred` | Work is needed only under an explicit condition: adoption of an arc, product, release or technology. It is not a promise to produce every draft. |
| `resolved` | The criterion is met, the answer is reflected in all applicable documents, and evidence and required human decisions exist. |
| `superseded` | Another linked ID replaces the record, with a reason. History and links remain. |

`lifecycle: draft` describes this register edition. `status` describes the question's state. `source_status` preserves the original authorial label. Canon approval, translation review, historical accuracy and a successful technical check are distinct matters.

A deferred question requires `activation_condition_ru/en`. Update its state when that condition occurs. An unknown assignee remains `unassigned`. A document's metadata owner is not automatically assigned every question associated with it.

## 5. Where the answer must be written

Every ID requires at least one existing concrete file. `primary_target_ru/en` identifies where the principal decision belongs. `open-question-targets.csv` lists all required associated checks and necessary edits, while `change_ru/en` describes each check or change. A folder link, the question itself or the source import does not replace a subject destination.

An associated document may already match the answer. For that relationship, `completion_status: verified-no-change` is valid with a reason and evidence; a cosmetic edit is not required. Other values are `pending` for unfinished work, `updated` for completed changes, and `not-applicable` when a specific reasoned decision removes applicability. Record the outcome in `result_ru/en` and its basis in `completion_evidence`. Do not delete an unchecked relationship to force closure.

If the result requires an artifact not yet created—a work, map, model or document—point to the existing specification or brief where its creation decision and requirements belong. Describe a prospective path in prose until the file exists; do not publish a broken link. Once created, add the new destination and its individual file-catalogue entry.

For an existing language pair, list both editions. If a full counterpart is missing, leave its field empty and make the language debt explicit; an existing bilingual file may be a shared destination. Do not invent an English path or duplicate a shared CSV/JSON into competing editions. The completeness of language views for machine formats and immutable source snapshots is a separate decision.

## 6. Data fields

Original `id`, `kind`, `area`, `title`, `question`, `closure_criteria`, `status`, `owner`, `source_status`, `source_refs`, `related_ids`, `source_path`, `working_path_ru/en` and `navigation_category` fields are retained. Russian text stays in `title`, `question` and `closure_criteria`; full English counterparts use the `_en` suffix.

| Group | Fields and purpose |
| --- | --- |
| Classification | `category`, `topic_ru/en`, `kind`, `lifecycle`, `question_origin` |
| Verifiable result | `question`, `question_en`, `closure_criteria`, `closure_criteria_en`, `activation_condition_ru/en` |
| Traceability | `source_path`, `working_path_ru/en`, `evidence_path`, `evidence_excerpt`, `related_ids`, `depends_on` |
| Work state | `work_ref` for a working-change link; `blocker_ru/en` and `unblock_action_ru/en` for the obstacle and its removal; `replacement_id` for the exact successor of a `superseded` item |
| Editing destinations | `primary_target_ru/en`, `target_count`; the relationship table contains the complete list |
| Navigation | `registry_view_ru/en`; this is the current question card, not the specification containing the answer |
| Closure | `resolution_ru/en`, `resolution_evidence`, `updated` |

The relationship table contains `target_id`, `question_id`, `role` (`primary` / `related`), `path_ru/en`, `anchor_ru/en`, `change_ru/en`, `completion_status`, `result_ru/en`, `completion_evidence`. `target_count` counts relationships, not language files. One shared bilingual destination counts once.

## 7. Closing a question

1. Check current authorial positions, dependencies and the question's evidence. Do not infer agreement from silence, translation, a PR merge or a source heading called “canon”.
2. Write the answer, limits and evidence in the primary subject document; check all associated destinations and language editions, make necessary edits or justify an unchanged document on its relationship row.
3. If a new card is needed, create it in its subject area, catalogue it and add it to the question's relationships. Structural and rights rules continue to apply.
4. Obtain exactly the human decisions required by the existing policy. A technically successful test does not close a creative divergence or substitute for translation review.
5. Record the concise result and evidence in the register, then refresh the language views and cross-references. Only then set `resolved`.

If only part of the criterion is met, keep the question open and clarify the remainder. If evidence shows a previous blocker is already removed, it may be closed on that factual basis without inventing a new approval. Earlier session logs remain history; add a link to the new state rather than rewriting the past.

## 8. Maintaining completeness

When a subject document changes, check for new uncertainty, stale links and changed activation conditions for deferred work. Preserve IDs during moves and update every destination. Resolved records remain in the register so that a decision's reason and result stay traceable.

Verification for this edition consists of a one-off file, link and language correspondence audit plus the repository's existing validator. This specification adds no new CI, hook or compulsory catalogue automation. Coverage concerns the available corpus at the stated date, not future ideas that have not yet been expressed.
