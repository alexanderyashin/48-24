---
id: "WIKI-OQ-PRODUCTS-EN"
entity_id: "WIKI-OQ-PRODUCTS"
title: "Products, data and game engines — open questions"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-20"
language: "en"
translation_of: "WIKI-OQ-PRODUCTS"
translation_path: "studio/navigation/ru/open-questions/products.md"
translation_status: "draft-unreviewed"
source: "TASK-OPEN-QUESTIONS-001"
source_statuses: ["ПОРУЧЕНИЕ САШИ; РЕДАКЦИОННАЯ ФИКСАЦИЯ"]
discussion_buckets: ["gap", "discussion"]
canon_refs: []
supersedes: []
ai_assistance: "ChatGPT: repository audit, question routing and full translation; human review pending."
authority: "navigation-only"
---

# Products, data and game engines — open questions

**Draft** · [Wiki](../README.md) · [All questions](README.md) · [Русский](../../ru/open-questions/products.md) · [Master register](../../../registers/open-questions.csv)

This page is a view of the unified register. Write answers in the subject documents listed below; change current state in the primary record, then synchronise both wikis.

| ID | Topic | Question | State |
| --- | --- | --- | --- |
| [OQ-0048](products.md#oq-0048) | Game technology and verifiable implementation | Game stack and project boundaries | Deferred until condition |
| [OQ-0049](products.md#oq-0049) | Production and adaptations | Book: reader promise and outline | Deferred until condition |
| [OQ-0050](products.md#oq-0050) | Production and adaptations | Game: player experience and prototype | Deferred until condition |
| [OQ-0051](products.md#oq-0051) | Production and adaptations | Tabletop: rules and test package | Deferred until condition |
| [OQ-0052](products.md#oq-0052) | Production and adaptations | Video: first production package | Deferred until condition |
| [PM-Q001](products.md#pm-q001) | Game technology and verifiable implementation | Target game engine and exact version | Open |
| [PM-Q002](products.md#pm-q002) | Game technology and verifiable implementation | Existing pipeline components and licenses | Open |
| [PM-Q003](products.md#pm-q003) | Game technology and verifiable implementation | End-to-end OBJ/ART/PHYS to scene prototype | Open |
| [PM-Q004](products.md#pm-q004) | Game technology and verifiable implementation | Mapping the shared contract to the engine | Open |
| [PM-Q005](products.md#pm-q005) | Game technology and verifiable implementation | Evidence-based model and gameplay-state verification | Open |
| [PM-Q006](products.md#pm-q006) | Game technology and verifiable implementation | Assigning P0/P1/P2 and Game/Render Ready per asset | Deferred until condition |

<a id="oq-0048"></a>

## OQ-0048 — Game stack and project boundaries

**Deferred until condition** · Open gap · Owner: Unassigned

**Question.** What are the game component and source-code boundaries, target platforms, interchange format and relationship between any future game repository and the shared-world version?

**Closure criterion.** The product specification records chosen technical boundaries and format; a separate repository is created only if needed, preserving canon linkage and rights.

**Activation condition.** A game or standalone game-technology prototype is selected for actual development, with a testable mechanic and experiment boundaries identified.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Техническая архитектура / Technical architecture](../../../../products/video-game/drafts/technical-architecture/README.md#русский) | [Техническая архитектура / Technical architecture](../../../../products/video-game/drafts/technical-architecture/README.md#english) | Record accepted architecture, component boundaries and decision links. |
| Related | [Стартовый пакет компьютерной игры](../../../../products/video-game/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Specify platforms, scope, stack, source location and world baseline. |
| Related | [Правила репозитория](../../../REPOSITORY_RULES.md#как-расширять) | No full edition; translation required | Update source-location policy only after an actual decision. |

**Evidence.** [Recorded uncertainty / source entry](../../../REPOSITORY_RULES.md#как-расширять).

**Related records.** [PM-Q001](products.md#pm-q001) · [PM-Q004](products.md#pm-q004)


<a id="oq-0049"></a>

## OQ-0049 — Book: reader promise and outline

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** If this track is selected for production, what exactly belongs in its first complete package? Reader promise, language, format, synopsis, viewpoint, chapters and first-manuscript working scope.

**Closure criterion.** A concrete product package identifies the world baseline, boundaries, acceptance criteria and owner. Postponement retains deferred status and does not close the record; a folder does not establish active production.

**Activation condition.** A book adaptation is selected for a specific manuscript or standalone book fragment.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет книги](../../../../products/books/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Complete start decisions and links to the selected product’s actual working materials. |
| Related | [Один мир и несколько продуктов](../../../PRODUCT_STRATEGY.md) | No full edition; translation required | Record the track’s actual position in the shared plan. |

**Evidence.** [Recorded uncertainty / source entry](../../../../products/books/drafts/starting-package-v0-1.md).

**Related records.** [GAP056](production.md#gap056) · [GAP053](narrative.md#gap053)


<a id="oq-0050"></a>

## OQ-0050 — Game: player experience and prototype

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** If this track is selected for production, what exactly belongs in its first complete package? Core experience, genre, camera, actions, core loop, progression and the first prototype’s minimal mechanic.

**Closure criterion.** A concrete product package identifies the world baseline, boundaries, acceptance criteria and owner. Postponement retains deferred status and does not close the record; a folder does not establish active production.

**Activation condition.** A video game is selected as an active product track or a test game prototype is explicitly launched.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет компьютерной игры](../../../../products/video-game/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Complete start decisions and links to the selected product’s actual working materials. |
| Related | [Один мир и несколько продуктов](../../../PRODUCT_STRATEGY.md) | No full edition; translation required | Record the track’s actual position in the shared plan. |

**Evidence.** [Recorded uncertainty / source entry](../../../../products/video-game/drafts/starting-package-v0-1.md).

**Related records.** [PM-Q001](products.md#pm-q001) · [PM-Q003](products.md#pm-q003) · [GAP056](production.md#gap056)


<a id="oq-0051"></a>

## OQ-0051 — Tabletop: rules and test package

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** If this track is selected for production, what exactly belongs in its first complete package? Player count, duration, loop, actions, components, ending, print-and-play and playtest method.

**Closure criterion.** A concrete product package identifies the world baseline, boundaries, acceptance criteria and owner. Postponement retains deferred status and does not close the record; a folder does not establish active production.

**Activation condition.** A tabletop adaptation is selected for development of a specific test package.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет настольной игры](../../../../products/tabletop/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Complete start decisions and links to the selected product’s actual working materials. |
| Related | [Один мир и несколько продуктов](../../../PRODUCT_STRATEGY.md) | No full edition; translation required | Record the track’s actual position in the shared plan. |

**Evidence.** [Recorded uncertainty / source entry](../../../../products/tabletop/drafts/starting-package-v0-1.md).

**Related records.** [GAP056](production.md#gap056) · [DIV001](production.md#div001)


<a id="oq-0052"></a>

## OQ-0052 — Video: first production package

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** If this track is selected for production, what exactly belongs in its first complete package? First episode purpose and duration, script, shot plan, animatic, sound, subtitles, edit and source package.

**Closure criterion.** A concrete product package identifies the world baseline, boundaries, acceptance criteria and owner. Postponement retains deferred status and does not close the record; a folder does not establish active production.

**Activation condition.** Video is selected as the next standalone release and a specific episode is identified for production.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет видео](../../../../products/youtube/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Complete start decisions and links to the selected product’s actual working materials. |
| Related | [Один мир и несколько продуктов](../../../PRODUCT_STRATEGY.md) | No full edition; translation required | Record the track’s actual position in the shared plan. |

**Evidence.** [Recorded uncertainty / source entry](../../../../products/youtube/drafts/starting-package-v0-1.md).

**Related records.** [GAP056](production.md#gap056) · [DIV001](production.md#div001) · [DIV002](production.md#div002)


<a id="pm-q001"></a>

## PM-Q001 — Target game engine and exact version

**Open** · Open gap · Owner: Unassigned

**Question.** Which engine and exact version fit the first prototype, with which physics backend and target platform?

**Closure criterion.** A comparison, selected engine/version/platform and rationale are recorded; the product package, engine index and R3 are updated. Selection alone does not establish a successful import.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет компьютерной игры](../../../../products/video-game/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | Record the selected engine, version, platform and first-prototype constraints. |
| Related | [Игровой движок / Game engine](../../../../products/video-game/drafts/engine/README.md#русский) | [Игровой движок / Game engine](../../../../products/video-game/drafts/engine/README.md#english) | Link the actual decision and versioned implementation profile. |
| Related | [Решения / Decision Log](../../../../production/planning/drafts/project-management/DECISIONS.md#русский) | [Решения / Decision Log](../../../../production/planning/drafts/project-management/DECISIONS.md#english) | Record the technology selection separately from creative canon. |
| Related | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#русский) | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#english) | Update R3 only after an actual selection. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q002](products.md#pm-q002) · [PM-Q004](products.md#pm-q004)


<a id="pm-q002"></a>

## PM-Q002 — Existing pipeline components and licenses

**Open** · Verification / research · Owner: Unassigned

**Question.** Which existing generators, importers and adapters cover the required pipeline, support the selected versions, and permit the intended use?

**Closure criterion.** A verified candidate matrix records source, version, license, features, limitations and experiment; chosen components link to the technical decision and rights records.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Интеграции и адаптеры / Integrations and adapters](../../../../products/video-game/drafts/integrations/README.md#русский) | [Интеграции и адаптеры / Integrations and adapters](../../../../products/video-game/drafts/integrations/README.md#english) | Record a comparison matrix and links to studies of specific components. |
| Related | [legal/THIRD_PARTY_ASSETS.csv](../../../../legal/THIRD_PARTY_ASSETS.csv) | No full edition; translation required | Register only actually selected third-party components and verified permission scope. |
| Related | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#русский) | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#english) | Record R2 results and remaining incompatibilities. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q001](products.md#pm-q001) · [PM-Q003](products.md#pm-q003)


<a id="pm-q003"></a>

## PM-Q003 — End-to-end OBJ/ART/PHYS to scene prototype

**Open** · Unfinished work · Owner: Unassigned

**Question.** Can a test wooden crate with metal corners be reproducibly built from cards and JSON through a real 3D model into an imported scene without undocumented manual setup?

**Closure criterion.** Actual cards, manifest, model sources, adapter, export, engine version, reproduction instructions, import log and an independently repeated result exist; documentation alone cannot close the question.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Прототипы / Prototypes](../../../../products/video-game/drafts/prototypes/README.md#русский) | [Прототипы / Prototypes](../../../../products/video-game/drafts/prototypes/README.md#english) | Add the specific prototype record and links to sources, cards and results. |
| Related | [Конвейер игровых ресурсов / Asset pipeline](../../../../products/video-game/drafts/asset-pipeline/README.md#русский) | [Конвейер игровых ресурсов / Asset pipeline](../../../../products/video-game/drafts/asset-pipeline/README.md#english) | Document the actual reproducible chain, commands, versions and limitations. |
| Related | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#русский) | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#english) | Update R4/R5 from artifacts and an actual import. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q001](products.md#pm-q001) · [PM-Q002](products.md#pm-q002) · [PM-Q004](products.md#pm-q004) · [PM-Q005](products.md#pm-q005)


<a id="pm-q004"></a>

## PM-Q004 — Mapping the shared contract to the engine

**Open** · Open gap · Owner: Unassigned

**Question.** Which shared-schema fields map to native properties of the chosen engine, require conversion or a plugin, or remain unsupported?

**Closure criterion.** For the engine, exact version and adapter version, all applicable fields, conversions, fallback/unsupported cases and import evidence are mapped; no data is silently dropped.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Игровой движок / Game engine](../../../../products/video-game/drafts/engine/README.md#русский) | [Игровой движок / Game engine](../../../../products/video-game/drafts/engine/README.md#english) | Link the completed profile for a specific version. |
| Related | [Engine Implementation Profile / Профиль реализации для движка](../../../../templates/engine-implementation-profile.md) | [Engine Implementation Profile / Профиль реализации для движка](../../../../templates/engine-implementation-profile.md) | Refine the form from an actual completed implementation profile; do not present the template as an implemented adapter. |
| Related | [Engine Data Contract / Контракт данных для игровых движков](../../../ENGINE_DATA_CONTRACT.md#русский) | [Engine Data Contract / Контракт данных для игровых движков](../../../ENGINE_DATA_CONTRACT.md#english) | Record discovered limitations and required contract changes. |
| Related | [templates/engine-asset.schema.json](../../../../templates/engine-asset.schema.json) | No full edition; translation required | Change the schema only where evidence requires it, retaining typing and versioning. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q001](products.md#pm-q001) · [PM-Q003](products.md#pm-q003)


<a id="pm-q005"></a>

## PM-Q005 — Evidence-based model and gameplay-state verification

**Open** · Unfinished work · Owner: Unassigned

**Question.** Which reproducible scenarios establish consistency between the first object’s cards, geometry, materials, collisions, damage, fracture and gameplay states?

**Closure criterion.** Scenarios identify resource versions, initial conditions, expected results and tolerances, actual results and evidence; R6/R7 reflect actual tests.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Тесты и приёмка / Tests and acceptance](../../../../products/video-game/drafts/tests/README.md#русский) | [Тесты и приёмка / Tests and acceptance](../../../../products/video-game/drafts/tests/README.md#english) | Record specific scenarios and link test reports. |
| Related | [Physics Governance / Норматив физического поведения объектов](../../../PHYSICS_GOVERNANCE.md#русский) | [Physics Governance / Норматив физического поведения объектов](../../../PHYSICS_GOVERNANCE.md#english) | Refine criteria if the first verified prototype exposes gaps. |
| Related | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#русский) | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#english) | Record actual R6/R7, incompatibilities and the scaling decision. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q003](products.md#pm-q003) · [PM-Q004](products.md#pm-q004) · [PM-Q006](products.md#pm-q006)


<a id="pm-q006"></a>

## PM-Q006 — Assigning P0/P1/P2 and Game/Render Ready per asset

**Deferred until condition** · Unfinished work · Owner: Unassigned

**Question.** Which first-package objects require P0, P1 or P2 physics, and which need only static rendering; which N/A cases and unknowns are permissible for each?

**Closure criterion.** Selected objects specify purpose, physics mode, target L-gate, applicable tests and justified N/A cases; existing general rules need not be reinvented.

**Activation condition.** A concrete first-prototype or release asset set and its intended uses are selected; then required physics and production modes are assigned per asset.

### Where to write the answer

| Role | RU document | EN document | Required change |
| --- | --- | --- | --- |
| Primary | [Стартовый пакет компьютерной игры](../../../../products/video-game/drafts/starting-package-v0-1.md#решения-для-старта) | No full edition; translation required | List first-package assets and required modes/gates. |
| Related | [Прототипы / Prototypes](../../../../products/video-game/drafts/prototypes/README.md#русский) | [Прототипы / Prototypes](../../../../products/video-game/drafts/prototypes/README.md#english) | Record P/L modes of specific prototypes and link their completed cards. |
| Related | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#русский) | [Дорожная карта / Roadmap](../../../../production/planning/drafts/project-management/ROADMAP.md#english) | Align R4/R6 scope with selected modes, without requiring P2 for every asset. |

**Evidence.** [Recorded uncertainty / source entry](../../../../production/planning/drafts/project-management/OPEN_ISSUES.md).

**Related records.** [PM-Q003](products.md#pm-q003) · [PM-Q005](products.md#pm-q005)
