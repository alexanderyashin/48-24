---
id: STD-SASHA-WEAPONS-DRAFT
title: "Профиль документации вооружения — Draft / Weapons documentation profile — Draft"
status: draft
version: v0-1
owner: alexanderyashin
reviewers: []
updated: 2026-11-20
source: IDEA-SASHA-WEAPONS-FOUNDATION
ai_assistance: "ChatGPT; GPT-6 Astra Pro; scoped draft documentation and translation"
languages: ["ru", "en"]
translation_status: draft-unreviewed
canon_refs: []
---

# Вооружение: проект нормативного дополнения / Weapons: Draft normative supplement

## Русский

### Область и статус

**Draft-профиль для текущей разработки вооружений**, составленный по поручению Саши. Он уточняет оформление намёток в рамках [стандарта объектов](OBJECT_STANDARD.md), [визуального норматива](VISUAL_GOVERNANCE.md) и [именования](NAMING_AND_METADATA.md). Он не меняет процедуру утверждения канона, реестр предметных областей, валидатор или требования производственной приёмки. [Запись решений](inbox/idea-sasha-weapons-foundation-v0-1.md).

### Поля оружейной карточки

Использовать [универсальную OBJ-карточку](../templates/world-object.md). В существующих секциях «Контекст», «Форма» и «Специализация» явно записывать:

| Поле | Что требуется от этой Draft-записи |
| --- | --- |
| Бюджет и производство | Положение на рабочей шкале; способ производства отдельно от состояния и владельца экземпляра |
| Принцип | Ссылка на технологическое семейство и модельные отличия |
| Применение | Контактное/дистанционное; предварительная детализация отдельно от численной дальности и массы |
| Зрелость | Что известно о существовании, выпуске и использовании; не выводить принятие на вооружение из наличия на складе |
| Область свойства | Семейство, конкретная модель, экземпляр, художественный вариант или игровая адаптация |
| Основание | Прямое решение Саши, принятое рабочее предложение, непроверенная гипотеза или открытый вопрос |
| Неизвестные | Явное «не определено»/`unknown`; `N/A` только для неприменимого поля с причиной |

Содержательные значения берутся из [классификации вооружений](../world/technology/drafts/weapons-systems/weapon-classification-v0-1.md). Таблица не вводит новый машинный формат, обязательные префиксы ID или автоматические проверки. Бюджет, сложность, качество, эффективность и распространённость не объединять в одну шкалу.

### Размещение и связи

| Материал | Путь |
| --- | --- |
| Источник рабочих решений | `studio/inbox/` |
| Классификация, технологии, семейства, конкретные OBJ | `world/technology/drafts/weapons-systems/` |
| Визуальные брифы и ART оружия | `art/props/drafts/weapons/` |
| Управление и игровые системы | `products/video-game/drafts/gameplay-systems/` |
| Исторические REF и проверки при появлении | Существующие профильные области `research/` |

Семейство описывается один раз. OBJ ссылаются на него и содержат отличия. ART ссылается на OBJ; игровой документ — на используемые мировые записи и версию. Наличие сырого материала не требует заполнить все поля до L2 или создать фиктивный REF, ART-файл либо физическую спецификацию.

### Согласованность с бюджетом и стадией

У аристократического полюса предусмотрены элегантность, украшения и ручная работа; общий запрет декоративности противоречил бы принятой рамке. Фабричный гранатомёт средней стоимости сохраняет собственную позицию. Криминальное владение не превращает фабричный образец в кустарный.

Два индикатора пневмотермического семейства закреплены в [его записи](../world/technology/drafts/weapons-systems/pneumothermal-family-v0-1.md). Конкретные места, размеры, шкалы и материалы открыты. Визуальная ясность этих двух функций должна проверяться при будущем ревью, а не считаться доказанной самим наличием брифа.

Первичная запись находится на L0; переход к [следующим стадиям](3D_READINESS_GATES.md) требует соответствующих материалов и доказательств. Нормативы [физики](PHYSICS_GOVERNANCE.md) и [игровых данных](ENGINE_DATA_CONTRACT.md) применяются при появлении соответствующей реализации; текущее художественное описание не заявляет P1/P2 или готовность к импорту в движок.

### Передача и изменение

Сохранять обе языковые версии согласно [языковой политике](LANGUAGE_POLICY.md), устойчивые ID и относительные ссылки. Рабочие документы остаются `draft`; изменения фиксируются через отдельную ветку и PR. Следующие уточнения дополняют профильные карточки, не переписывая исходный SPOT и не закрывая неподтверждённые вопросы. [CANON_POLICY](CANON_POLICY.md) продолжает действовать без изменений.

## English

### Scope and status

A **Draft profile for the current weapons development**, prepared at Sasha's request. It clarifies how outlines use the [object standard](OBJECT_STANDARD.md), [visual governance](VISUAL_GOVERNANCE.md) and [naming rules](NAMING_AND_METADATA.md). It does not change canon approval, the registered subject areas, the validator or production-acceptance requirements. See the [decision record](inbox/idea-sasha-weapons-foundation-v0-1.md).

### Weapon-card fields

Use the [universal OBJ card](../templates/world-object.md). Explicitly record the following in its existing Context, Form and Type-specific sections:

| Field | Requirement for this Draft record |
| --- | --- |
| Budget and production | Position on the working scale; production method separately from an individual item's condition and owner |
| Principle | Link to the technological family and model-specific differences |
| Use | Contact/ranged; provisional subdivision separately from numeric range and mass |
| Maturity | Known existence, manufacture and use; do not infer service adoption from depot presence |
| Property scope | Family, specific model, individual example, artistic variant or game adaptation |
| Basis | Sasha's direct decision, accepted working proposal, unverified hypothesis or open question |
| Unknowns | Explicitly undetermined/`unknown`; `N/A` only for inapplicable fields with a reason |

Substantive values come from the [weapon classification](../world/technology/drafts/weapons-systems/weapon-classification-v0-1.md). The table introduces no new machine format, mandatory ID prefixes or automated checks. Budget, complexity, quality, effectiveness and prevalence must not be collapsed into one scale.

### Locations and relationships

| Material | Path |
| --- | --- |
| Working-decision source | `studio/inbox/` |
| Classification, technologies, families and individual OBJ records | `world/technology/drafts/weapons-systems/` |
| Weapon visual briefs and ART | `art/props/drafts/weapons/` |
| Controls and game systems | `products/video-game/drafts/gameplay-systems/` |
| Historical REF and verification when available | Existing subject areas under `research/` |

A family is described once. OBJ records reference it and specify differences. ART references OBJ; game documents identify the world records and version used. Capturing an early idea does not require every field to reach L2 or a fictitious REF, ART deliverable or physics specification.

### Budget and stage consistency

The aristocratic pole explicitly includes elegance, ornament and handcraft; a universal prohibition of decoration would contradict the accepted direction. The medium-cost factory launcher retains its own position. Criminal ownership does not turn a factory product into an improvised one.

The pneumothermal family's two indicators are recorded in [its subject document](../world/technology/drafts/weapons-systems/pneumothermal-family-v0-1.md). Specific locations, dimensions, scales and materials remain open. The clarity of these two functions must be checked in future visual review; the existence of a brief is not proof.

Initial capture is L0; advancement through the [next stages](3D_READINESS_GATES.md) requires the corresponding materials and evidence. [Physics governance](PHYSICS_GOVERNANCE.md) and the [engine data contract](ENGINE_DATA_CONTRACT.md) apply when the relevant implementation exists; the current artistic description does not claim P1/P2 or engine-import readiness.

### Handoff and updates

Retain both language versions under the [language policy](LANGUAGE_POLICY.md), stable IDs and relative links. Working documents remain `draft`; changes use a separate branch and PR. Future clarifications update subject cards without rewriting the original SPOT or closing unconfirmed questions. [CANON_POLICY](CANON_POLICY.md) remains unchanged.
