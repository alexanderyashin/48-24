# Единый стандарт объектов 48/24 / Universal Object Standard

## Русский

**Цель:** фиксировать любой объект материальной культуры и окружающей среды по одной системе: одежду, оружие, инструменты, мебель, бытовые вещи, здания, транспорт, машины, инфраструктуру и природные объекты. Стандарт описывает объект, а не заменяет художественный канон.

**Три уровня идентичности (не смешивать):**
1. `REF-...` — реальный исторический предмет или источник с музеем, датировкой и правами.
2. `OBJ-...` — объект вымышленного мира, его функция, конструкция и варианты. Один OBJ может ссылаться на несколько REF.
3. `ART-...` — конкретная реализация OBJ: рисунок, модель, чертёж, рендер, анимация. У OBJ может быть много ART.

**Обязательный минимум при создании OBJ:** уникальный ID, название, тип, статус, ответственный, дата, источник идеи, версия, авторство/участники (если известны), временной и географический контекст либо «не определён», функция, описание, ссылки на референсы и связанные объекты, открытые вопросы. Неизвестные характеристики обозначать «не определено»; не выдумывать размеры и технические параметры.

**Стандартные секции полной карточки:** идентификация; история и контекст; назначение; геометрия и масштаб; материалы и производство; конструкция и эксплуатация; эстетика и признаки износа; варианты и социальное распространение; связи и зависимости; исторические прототипы; арт-ресурсы; источники и права; проверки и решения.

**Специализации:** одежда — крой, слои, посадка; оружие — конструкция, обслуживание и ограничения; мебель и утварь — эргономика и материалы; архитектура — планы, фасады, интерьеры и инженерные системы; транспорт — компоновка, тяга и обслуживание; механизмы — энергетический цикл, кинематика, надёжность. Отмечать неприменимые поля `N/A`.

**Арт-пакет:** референсная доска → варианты силуэта → выбранный дизайн → согласованные виды (фас/профиль/сзади/сверху, где применимо) → масштаб/размеры → материалы, детали и крепления → контекстный кадр → исходник и экспорты. Каждый файл имеет отдельный ART ID, версию и паспорт по [ASSET_WORKFLOW](ASSET_WORKFLOW.md). Этапы 3D и анимации обязательны только если нужны продукту.

**Связи:** `based_on` (OBJ→REF), `depicts` (ART→OBJ), `part_of`, `used_by`, `manufactured_by`, `variant_of`, `replaces`, `located_in`. Указывайте ID и относительные ссылки; не копируйте объект по нескольким папкам.

**Утверждение:** рабочий черновик не является каноном. Перенос в canon требует действительных решений двух соавторов. `owner` не означает юридическое право собственности. Учёт вкладов ведётся отдельно.

**Основа методики:** общедоступные практики Blender Studio Asset Pipeline (задачи, варианты, передача), Blender naming conventions (имена и версии), производственные concept/model sheets (виды, пропорции, материалы). Это собственный стандарт 48/24, **не официальный бланк Blender Studio**. См. [Blender Studio Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline) и [Blender Studio tools](https://projects.blender.org/studio/blender-studio-tools).

## English

**Purpose:** a shared object-recording system for clothing, weapons, tools, furniture, domestic objects, buildings, vehicles, machinery, infrastructure, and natural objects.

**Three identities:** `REF-...` is a real historical object/source; `OBJ-...` is a fictional world object; `ART-...` is a specific drawing/model/render/animation. One OBJ can have multiple REF and ART links.

**Minimum OBJ record:** unique ID, name, class, status, owner, date, source, version, known contributors, era/location or explicitly unknown, function, description, reference IDs, related object IDs, and open questions. Never invent missing measurements.

**Full sections:** identity; historical and social context; purpose; dimensions and scale; materials and manufacture; construction and operation; visual language and wear; variants and distribution; relationships; historical references; art deliverables; rights; review decisions.

**Type extensions:** clothing—cut, layers, fit; weapons—construction, maintenance, constraints; furniture—ergonomics; architecture—plans, facades, interiors and utilities; transport—layout, propulsion, maintenance; mechanisms—energy cycle, kinematics, reliability. Mark inapplicable fields N/A.

**Art package:** reference board → silhouettes → selected design → consistent views as applicable → scale → material/detail callouts → context view → editable master and exports. Each ART file has its own ID/version and rights/provenance sidecar. 3D stages are conditional on product requirements.

**Links:** `based_on`, `depicts`, `part_of`, `used_by`, `manufactured_by`, `variant_of`, `replaces`, `located_in`. Cross-link IDs; avoid copies.

**Approval:** drafts are not canon. Canon requires the actual coauthor approvals. Responsibility is not legal ownership. Contribution attribution is separate.

**Methodological basis:** publicly documented Blender Studio asset-pipeline and naming practices plus concept/model-sheet conventions, adapted into a project-specific standard, **not an official Blender Studio form**. See [Blender Studio Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline) and [Blender Studio tools](https://projects.blender.org/studio/blender-studio-tools).

## Производственная спецификация / Production specification

Объект OBJ остаётся единым источником идентичности и назначения. Техническая реализация ART для 3D обязана ссылаться на OBJ и заполнять [3D-формуляр](../templates/3d-production-spec.md) согласно [уровням готовности](3D_READINESS_GATES.md). Не переносите в OBJ игровые ограничения конкретного движка: они принадлежат ART-реализации.

OBJ remains the identity and design source. Each 3D ART implementation references OBJ and completes the [3D form](../templates/3d-production-spec.md) under the [readiness gates](3D_READINESS_GATES.md). Engine-specific implementation constraints belong to ART, not OBJ.

## Физическое поведение / Physical behavior

Для физически моделируемых объектов дополнительно обязательна [карточка физических свойств](../templates/physical-behavior-spec.md) по [нормативу физики](PHYSICS_GOVERNANCE.md). Разделяйте оптические свойства (глянец, матовость, отражение) и механические свойства (гибкость, прочность, хрупкость, масса, трение). / Simulated objects require a linked [physics specification](../templates/physical-behavior-spec.md) under [physics governance](PHYSICS_GOVERNANCE.md). Optical and mechanical properties are distinct.

## Вооружение: Draft-дополнение / Weapons: Draft supplement

Для текущих намёток подготовлен [проект профиля оружейной документации](WEAPONS_DRAFT_STANDARD.md): независимые оси бюджета/производства, принципа и применения, область действия каждого свойства и явные неизвестные. Он использует существующие секции OBJ; сам профиль и [содержательные решения](../world/technology/drafts/weapons-systems/weapon-classification-v0-1.md) пока имеют статус Draft. Требования канонизации и производственной готовности сохраняются.

A [proposed weapons documentation profile](WEAPONS_DRAFT_STANDARD.md) supports the current outlines: independent axes of budget/production, principle and use, each property's scope and explicit unknowns. It uses existing OBJ sections; both the profile and [substantive decisions](../world/technology/drafts/weapons-systems/weapon-classification-v0-1.md) remain Draft. Canon-approval and production-readiness requirements continue to apply.
