# Работа студии / Studio operations

Действующие инструкции и реестры организации проекта. Они обслуживают работу над вселенной и не являются художественным каноном. / Current operating instructions and registers. They support development of the universe and are not creative canon.

## Войти в работу / Start working

| Документ / Document | Когда открыть / When to use |
| --- | --- |
| [Начало работы / Start here](START_HERE.md) | Первый визит и первая задача / First visit and first task |
| [Навигатор / Navigator](NAVIGATION.md) | Куда положить материал и что читать / Choose a destination and reading route |
| [Карта папок / Folder map](REPOSITORY_MAP.md) | Все разделы и вложенные папки / All areas and subfolders |
| [Каталог материалов / Content catalogue](CONTENT_CATALOG.md) | Поиск существующих карточек по ID, теме, статусу / Find records by ID, topic and status |
| [Практические руководства / Practical guides](guides/README.md) | Сюжеты, сотрудничество, ресурсы и задания ИИ / Writing, collaboration, assets and AI briefs |
| [Работа в ветках / Work in branches](BRANCHES.md) | Открытые PR и работа, ещё не включённая в main / Open PRs and work awaiting integration |

## Общие правила / Shared policies

| Документ / Document | Назначение / Purpose |
| --- | --- |
| [WORKFLOW](WORKFLOW.md) | Задачи, ветки, рассмотрение, передача / Tasks, branches, review, handoff |
| [RESPONSIBILITIES](RESPONSIBILITIES.md) | Направления и учёт вкладов / Domain stewardship and contribution attribution |
| [CANON_POLICY](CANON_POLICY.md) | Статусы, версии и решения двух авторов / Statuses, versions and coauthor decisions |
| [REPOSITORY_RULES](REPOSITORY_RULES.md) | Структура, расширение и сохранение истории / Structure, extension and preserved history |
| [LANGUAGE_POLICY](LANGUAGE_POLICY.md) | Равноправные RU/EN версии / Equal-standing RU/EN versions |
| [NAMING_AND_METADATA](NAMING_AND_METADATA.md) | Идентификаторы, имена и поля / IDs, names and metadata |
| [AI_COLLABORATION](AI_COLLABORATION.md) | Контекст, происхождение и ответственность / AI context, provenance and responsibility |
| [source-import-guide](source-import-guide.md) | Исторический SPOT и развивающиеся рабочие карточки / Historical SPOT and evolving working records |

## Предметы, ресурсы и продукты / Objects, assets and products

| Документ / Document | Назначение / Purpose |
| --- | --- |
| [OBJECT_STANDARD](OBJECT_STANDARD.md) | REF → OBJ → ART и связи / REF → OBJ → ART and relationships |
| [VISUAL_GOVERNANCE](VISUAL_GOVERNANCE.md) | Описание, виды, материалы и дизайн-ревью / Description, views, materials and design review |
| [PHYSICS_GOVERNANCE](PHYSICS_GOVERNANCE.md) | Физические свойства и уровни P0–P2 / Physical properties and P0–P2 levels |
| [3D_READINESS_GATES](3D_READINESS_GATES.md) | Производственная готовность L0–L3 / Production readiness L0–L3 |
| [ENGINE_DATA_CONTRACT](ENGINE_DATA_CONTRACT.md) | Типы данных, схема, адаптеры движков / Data types, schema and engine adapters |
| [ASSET_WORKFLOW](ASSET_WORKFLOW.md) | Файлы, паспорта, права, внешние мастера / Files, sidecars, rights, external masters |
| [PRODUCT_STRATEGY](PRODUCT_STRATEGY.md) | Общая вселенная и конкретные адаптации / Shared universe and individual adaptations |
| [RELEASE_PROCESS](RELEASE_PROCESS.md) | Состав и проверка выпуска / Release manifest and review |

## Учёт и проверка / Tracking and verification

| Место / Location | Что искать / What to find |
| --- | --- |
| [inbox](inbox/README.md) | Сырые идеи и история их маршрутизации / Raw ideas and routing history |
| [registers](registers/README.md) | Источники, вопросы, текущие карточки, вклады, ресурсы / Sources, questions, records, contributions, assets |
| [approvals](approvals/README.md) | Подтверждения реальных решений / Evidence of actual decisions |
| [migrations](migrations/README.md) | Планы изменения зарегистрированной структуры / Registered structure migration plans |
| [rollout](rollout/README.md) | История внедрения и настройки GitHub / Rollout history and GitHub configuration |
| [repository-checks](repository-checks.md) | Что проверяет основной валидатор / What the core validator checks |
| [tools](../tools/README.md) | Команды навигации и проверки / Navigation and validation commands |
| [Журнал управления / Management log](../production/planning/drafts/project-management/README.md) | Ход работ, открытые задачи, сессии / Work history, open tasks, sessions |

[structure.json](structure.json) задаёт зарегистрированную структуру; [team.json](team.json) — идентификаторы участников. [navigation.json](navigation.json) помогает находить рабочее место, но не изменяет эти договорённости. / structure.json defines the registered structure; team.json records participant IDs. navigation.json helps locate work without changing either agreement.

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../README.md) › [studio](README.md)

[По задаче / By task](NAVIGATION.md) · [Карта / Map](REPOSITORY_MAP.md) · [Материалы / Content](CONTENT_CATALOG.md) · [Шаблоны / Templates](../templates/README.md)

### Подразделы / Subfolders

- [Подтверждения решений](approvals/README.md) — `approvals/`.
- [Практические инструкции / Practical guides](guides/README.md) — `guides/`.
- [Входящие творческие фрагменты / Creative Inbox](inbox/README.md) — `inbox/`.
- [Изменения структуры](migrations/README.md) — `migrations/`.
- [Реестры проекта / Project registers](registers/README.md) — `registers/`.
- [Развёртывание защиты GitHub](rollout/README.md) — `rollout/`.

### Файлы рядом / Files here

- [3D Production Readiness / Готовность к 3D-производству](3D_READINESS_GATES.md) — `3D_READINESS_GATES.md`.
- [Организация: контекст для помощника / Studio assistant context](AGENTS.md) — `AGENTS.md`.
- [Работа с ИИ](AI_COLLABORATION.md) — `AI_COLLABORATION.md`.
- [Работа с изображениями шрифтами аудио и исходниками](ASSET_WORKFLOW.md) — `ASSET_WORKFLOW.md`.
- [Работа в ветках / Work in branches](BRANCHES.md) — `BRANCHES.md`.
- [Канон и версии](CANON_POLICY.md) — `CANON_POLICY.md`.
- [Каталог материалов / Content catalogue](CONTENT_CATALOG.md) — `CONTENT_CATALOG.md`.
- [Engine Data Contract / Контракт данных для игровых движков](ENGINE_DATA_CONTRACT.md) — `ENGINE_DATA_CONTRACT.md`.
- [Языковая политика проекта 48/24 / Language Policy](LANGUAGE_POLICY.md) — `LANGUAGE_POLICY.md`.
- [Имена и метаданные](NAMING_AND_METADATA.md) — `NAMING_AND_METADATA.md`.
- [Навигатор проекта / Project navigator](NAVIGATION.md) — `NAVIGATION.md`.
- [Единый стандарт объектов 48/24 / Universal Object Standard](OBJECT_STANDARD.md) — `OBJECT_STANDARD.md`.
- [Physics Governance / Норматив физического поведения объектов](PHYSICS_GOVERNANCE.md) — `PHYSICS_GOVERNANCE.md`.
- [Один мир и несколько продуктов](PRODUCT_STRATEGY.md) — `PRODUCT_STRATEGY.md`.
- [Подготовка выпуска](RELEASE_PROCESS.md) — `RELEASE_PROCESS.md`.
- [Карта репозитория / Repository map](REPOSITORY_MAP.md) — `REPOSITORY_MAP.md`.
- [Правила репозитория](REPOSITORY_RULES.md) — `REPOSITORY_RULES.md`.
- [Ответственность и творческий вклад / Responsibilities and Creative Contributions](RESPONSIBILITIES.md) — `RESPONSIBILITIES.md`.
- [Начать работу / Start here](START_HERE.md) — `START_HERE.md`.
- [Норматив визуального ряда 48/24 / Visual Asset Governance Standard](VISUAL_GOVERNANCE.md) — `VISUAL_GOVERNANCE.md`.
- [Совместный рабочий процесс](WORKFLOW.md) — `WORKFLOW.md`.
- [navigation.json](navigation.json) — `navigation.json`.
- [Проверки репозитория](repository-checks.md) — `repository-checks.md`.
- [Как использовать исходный корпус и рабочие карточки](source-import-guide.md) — `source-import-guide.md`.
- [structure.json](structure.json) — `structure.json`.
- [team.json](team.json) — `team.json`.

### Подходящие формы / Relevant forms

[idea-fragment.md](../templates/idea-fragment.md) · [decision.md](../templates/decision.md) · [approval.example.json](../templates/approval.example.json) · [archive-note.md](../templates/archive-note.md) · [handoff.md](../templates/handoff.md)

Контекст для ИИ / AI reading list: `python tools/navigate.py context studio`

<!-- NAVIGATION:END -->
