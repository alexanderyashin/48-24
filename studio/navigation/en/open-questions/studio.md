---
id: "WIKI-OQ-STUDIO-EN"
entity_id: "WIKI-OQ-STUDIO"
title: "Collaboration and infrastructure — open questions"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-20"
language: "en"
translation_of: "WIKI-OQ-STUDIO"
translation_path: "studio/navigation/ru/open-questions/studio.md"
translation_status: "draft-unreviewed"
source: "TASK-OPEN-QUESTIONS-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ ФИКСАЦИЯ"]
discussion_buckets: ["gap", "discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: repository audit, question routing and full translation; human review pending."
authority: "navigation-only"
---

# Collaboration and infrastructure — open questions

**Draft** · [Wiki](../README.md) · [All questions](README.md) · [Русский](../../ru/open-questions/studio.md) · [Master register](../../../registers/open-questions.csv)

This page is a view of the unified register. Write answers in the subject documents listed below; change current state in the primary record, then synchronise both wikis.

| ID | Topic | Question | State |
| --- | --- | --- | --- |
| [OQ-0053](studio.md#oq-0053) | Collaboration and project governance | Future catalogue enforcement automation | Deferred until condition |
| [OQ-0054](studio.md#oq-0054) | Collaboration and project governance | First scoped canon approval | Deferred until condition |
| [OQ-0055](studio.md#oq-0055) | Collaboration and project governance | Actual main branch protection | Open |
| [OQ-0056](studio.md#oq-0056) | Collaboration and project governance | Adoption of SPOT editorial governance proposals | Deferred until condition |
| [OQ-0057](studio.md#oq-0057) | Collaboration and project governance | Stale Ivan onboarding task | Open |
| [OQ-0058](studio.md#oq-0058) | Collaboration and project governance | Review and acceptance of the SPOT decomposition | Open |
| [OQ-0059](studio.md#oq-0059) | Collaboration and project governance | Unassigned domains and role confirmation | Open |
| [PM-Q007](studio.md#pm-q007) | Collaboration and project governance | Observed repository validation result | Resolved with evidence |

<a id="oq-0053"></a>

## OQ-0053 — Future catalogue enforcement automation

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** Should per-file cataloguing and bilingual links later be automated, and what would that separate task include?

**Closure criterion.** Manual normative verification remains until separately requested; if automation is chosen, requirements, accepted changes and real checks are recorded separately. No new CI is required by the current task.

**Activation condition.** A separate request authorizes technical catalogue automation; the current request is normative only and does not activate this work.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Обязательная каталогизация и двуязычная навигация](../../proposals/cataloguing-standard-v0-1.md) | [Mandatory file cataloguing and bilingual navigation](../../proposals/cataloguing-standard-v0-1.en.md) | Preserve the normative-only boundary; record automation scope only after a new decision. |
| Related | [Проверки репозитория](../../../repository-checks.md) | No full edition; translation required | Describe checks only after they have actually been implemented. |

**Evidence.** [Recorded uncertainty / source entry](../../proposals/cataloguing-standard-v0-1.md).


<a id="oq-0054"></a>

## OQ-0054 — First scoped canon approval

**Deferred until condition** · Review and agreement · Owner: Unassigned

**Question.** Which minimal set of exact statements are both coauthors ready to approve for the first work once the current Draft stage ends?

**Closure criterion.** A separate decision by both coauthors identifies exact versions and scope; relevant cards and dependencies are updated under CANON_POLICY. The current request keeps everything Draft and does not require this acceptance now.

**Activation condition.** The coauthors select a specific small package for creative approval after the current Draft stage; decomposition or PR merge does not itself activate canonization.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Первые этапы работы студии](../../../../production/planning/drafts/launch-roadmap-v0-1.md#первые-самостоятельные-задачи) | No full edition; translation required | Record the selected minimum and actual draft/review/canon outcome or reasons for deferral. |
| Related | [Состояние организационного rollout](../../../rollout/STATUS.md#административное-состояние) | No full edition; translation required | Update canon status only from actual evidence. |
| Related | [studio/registers/decisions.csv](../../../registers/decisions.csv) | No full edition; translation required | Link the exact new decision without replacing original CAN provenance. |

**Evidence.** [Recorded uncertainty / source entry](../../../rollout/STATUS.md#что-осталось-владельцам).

**Related records.** [GAP056](production.md#gap056) · [DIV001](production.md#div001)


<a id="oq-0055"></a>

## OQ-0055 — Actual main branch protection

**Open** · Unfinished work · Owner: Unassigned

**Question.** Which main protection rules are actually active after both coauthors were connected, and does the server match the prepared two-author configuration?

**Closure criterion.** The selected main-protection mode is actually enabled / Active; server configuration confirms the ruleset ID/mode, required checks and review. An observed protected=false or Disabled state confirms unfinished work; a local JSON file does not close the question.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Состояние организационного rollout](../../../rollout/STATUS.md#административное-состояние) | No full edition; translation required | Update observed administrative state and activation evidence. |
| Related | [Развёртывание защиты GitHub](../../../rollout/README.md#порядок-включения) | No full edition; translation required | Clarify the applicable mode and exact observed check name if needed. |

**Evidence.** [Recorded uncertainty / source entry](../../../rollout/STATUS.md#административное-состояние).

**Related records.** [PM-Q007](studio.md#pm-q007)


<a id="oq-0056"></a>

## OQ-0056 — Adoption of SPOT editorial governance proposals

**Deferred until condition** · Review and agreement · Owner: Unassigned

**Question.** Which SPOT proposals on versions, cards and causality checks should supplement existing rules, and how should the two template sets be reconciled?

**Closure criterion.** The exact accepted or rejected scope is recorded; rules and templates are consistent with WORKFLOW/CANON_POLICY; adoption is not inferred from silence.

**Activation condition.** The coauthors move to permanent use of specific SPOT editorial proposals, or a conflict with existing rules is identified; review only the affected scope.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Предложения SPOT об управлении каноном](../../../governance/proposals/spot-governance-proposals-v0-1.md#gov_ids) | [SPOT proposals for canon governance](../../../governance/proposals/spot-governance-proposals-v0-1.en.md#gov_ids) | Clarify each normative proposal’s status and relationship to existing rules. |
| Related | [Предложения форм SPOT / Proposed SPOT forms](../../../../templates/proposals/README.md) | No full edition; translation required | Identify which forms are recommended and how they relate to existing templates. |
| Related | [Имена и метаданные](../../../NAMING_AND_METADATA.md) | No full edition; translation required | Incorporate only actually accepted identifier and version refinements. |

**Evidence.** [Recorded uncertainty / source entry](../../../governance/proposals/spot-governance-proposals-v0-1.md#gov_ids).


<a id="oq-0057"></a>

## OQ-0057 — Stale Ivan onboarding task

**Open** · Unfinished work · Owner: Unassigned

**Question.** Which onboarding notes still describe Ivan’s connection as outstanding after write access was confirmed and CODEOWNERS merged?

**Closure criterion.** Onboarding notes link the confirmed state; no duplicate invitation is created, and historical records are retained.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Как начать работу](../../../START_HERE.md#что-решить-в-ближайшее-время) | No full edition; translation required | Remove the stale login/access request from current next steps and link confirmation. |
| Related | [Первые этапы работы студии](../../../../production/planning/drafts/launch-roadmap-v0-1.md) | No full edition; translation required | Separate completed access setup from outstanding main protection. |

**Evidence.** [Recorded uncertainty / source entry](../../../START_HERE.md#что-решить-в-ближайшее-время).


<a id="oq-0058"></a>

## OQ-0058 — Review and acceptance of the SPOT decomposition

**Open** · Review and agreement · Owner: Unassigned

**Question.** Have human review of the decomposition/status handling and acceptance of PR #5 documentation been completed while retaining Draft status?

**Closure criterion.** The PR records actual comments and review outcome, and the migration records acceptance or another outcome. Merging does not resolve content questions or approve translations or canon.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Декомпозиция SPOT и две вики: запись миграции](../../../migrations/spot-docs-and-wiki-v0-1.md#порядок-возврата-и-продолжения) | [SPOT decomposition and two wikis: migration record](../../../migrations/spot-docs-and-wiki-v0-1.en.md#rollback-and-continuation) | Append the observed review outcome and PR #5 status. |
| Related | [Единый реестр открытых вопросов: правила ведения](../../../registers/proposals/open-question-register-v0-1.md) | [Unified open-question register: maintenance rules](../../../registers/proposals/open-question-register-v0-1.en.md) | Review the unified-register model and maintenance rules as a continuation of the Draft decomposition; record comments or acceptance through the existing process. |

**Evidence.** [Recorded uncertainty / source entry](../../../migrations/spot-docs-and-wiki-v0-1.md#порядок-возврата-и-продолжения).

**Related records.** [OQ-0075](translation.md#oq-0075)


<a id="oq-0059"></a>

## OQ-0059 — Unassigned domains and role confirmation

**Open** · Open gap · Owner: Unassigned

**Question.** Who will steward research, production and documentation, and does Ivan confirm the described working domain allocation?

**Closure criterion.** Stewards are assigned only by actual agreement; confirmed and unconfirmed roles are distinguished; roles do not determine authorship or ownership.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Ответственность и творческий вклад / Responsibilities and Creative Contributions](../../../RESPONSIBILITIES.md#русский) | [Ответственность и творческий вклад / Responsibilities and Creative Contributions](../../../RESPONSIBILITIES.md#english) | Update domain tables and confirmation provenance in both languages. |
| Related | [studio/team.json](../../../team.json) | No full edition; translation required | Reflect only confirmed roles if the team model requires an update. |

**Evidence.** [Recorded uncertainty / source entry](../../../RESPONSIBILITIES.md#русский).


<a id="pm-q007"></a>

## PM-Q007 — Observed repository validation result

**Resolved with evidence** · Unfinished work · Owner: Unassigned

**Question.** Has the previous DNS blocker been removed and actual repository validation completed?

**Closure criterion.** The historical closeout has a dated follow-up identifying base/revision, command, actual PASS and CI link; the earlier failed attempt is retained.

**Recorded result.** The former network blocker is removed. Revision f33a3c08c88b43b165d57f74e8eaf9f37f5c15e3 has a recorded local PASS (678 files, 0 errors); GitHub Actions run 44629578628 completed successfully. Subsequent evidence has been appended to the session and work log, and current state moved to the unified register. This does not establish game import or human acceptance.

**Evidence of closure.** [https://github.com/alexanderyashin/48-24/actions/runs/44629578628](https://github.com/alexanderyashin/48-24/actions/runs/44629578628)

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Сессия 2026-11-19 / Session 2026-11-19](../../../../production/planning/drafts/project-management/sessions/2026-11-19.md#validation-follow-up-2026-11-20) | [Сессия 2026-11-19 / Session 2026-11-19](../../../../production/planning/drafts/project-management/sessions/2026-11-19.md#validation-follow-up-2026-11-20-en) | Append subsequent successful validation evidence while preserving the historical DNS failure. **Outcome: updated.** Dated evidence appended; earlier history retained and current state tracked in the unified register. [Evidence](../../../../production/planning/drafts/project-management/sessions/2026-11-19.md#validation-follow-up-2026-11-20) |
| Related | [Выполненная работа / Work Log](../../../../production/planning/drafts/project-management/WORK_LOG.md#validation-follow-up-2026-11-20) | [Выполненная работа / Work Log](../../../../production/planning/drafts/project-management/WORK_LOG.md#validation-follow-up-2026-11-20-en) | Append to PM-W009 and clarify that the unrun-validator statement describes the earlier session. **Outcome: updated.** Dated evidence appended; earlier history retained and current state tracked in the unified register. [Evidence](../../../../production/planning/drafts/project-management/WORK_LOG.md#validation-follow-up-2026-11-20) |
| Related | [Открытые вопросы / Open Issues](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md#русский) | [Открытые вопросы / Open Issues](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md#english) | Replace the independent active status with the unified-register reference and evidenced subsequent resolution. **Outcome: updated.** Dated evidence appended; earlier history retained and current state tracked in the unified register. [Evidence](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md#русский) |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).
