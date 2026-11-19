# Engine Data Contract / Контракт данных для игровых движков

## Русский

**Норматив v1.0.** Внешние редакторские карточки OBJ/ART/PHYS — человекочитаемые документы. Для машинной обработки каждой игровой реализации обязателен **JSON-манифест по [схеме](../templates/engine-asset.schema.json)**. Это не нативный файл Unreal/Unity/Godot: нужен **детерминированный адаптер** к выбранной версии движка, с правилами преобразования и тестом импорта. Нельзя обещать прямое «скармливание» Markdown или универсального JSON движку.

**Строгая типизация:** UTF-8 JSON; обязательные поля, `additionalProperties:false` на структурных объектах; `schema_version`; уникальные строковые ID; `boolean`, `integer`, `number`, массивы и перечисления; диапазоны `minimum/maximum`, `maxLength`, `maxItems`, `pattern`. Числа — JSON number, не строка с единицей; все физические значения в SI, углы в радианах, цвета в линейном RGB [0,1], PBR roughness/metallic [0,1]. Не допускать NaN, Infinity, локальные десятичные запятые. Для неизвестного использовать `null` **только в черновике**, в экспортируемом профиле критические значения должны быть числовыми. N/A оформляется отсутствием необязательного поля и обоснованием в `exceptions`. Размеры строк и массивов — **наши договорные ограничения для безопасности/переносимости**, не выдуманные лимиты движков.

**Связи:** ID компонентов едины в `parts`, `joints`, `damage_zones`, `fracture`, `states`, `art_assets`; не допускаются висячие ссылки. Каждая часть имеет материал, геометрию, массу, центр масс и коллизию. Для разрушаемых частей — зоны повреждения, пороги, последствия и визуальные представления. Для гибких — деформируемая сетка, ограничения, параметры ткани/soft body и решатель. Для разрушения — фрагменты, кластеры, связи, пороги, бюджет и поведение осколков. Для оружия — состояние каждой функциональной части и влияние повреждения на функции (без предписания реальных способов изготовления).

**Повреждения:** `damage_zones` связывают часть, тип воздействия, числовые пороги, единицы, накопление и переход состояния; `states` задают `healthy/damaged/disabled/destroyed` и другие состояния, `transitions` — триггеры и последствия (коллизия, подвижность, функциональность, VFX/SFX, замена mesh/material). Состояния должны быть однозначны, а переходы ссылаться на существующие ID. Физический ущерб и игровая «прочность» (HP) — **разные величины**; HP — условная игровая единица и требует явной маркировки.

**Профили:** `engine.target` = `unreal` / `unity` / `godot` / `generic`, `engine.version`, `engine.adapter_version`, `engine.asset_type`. `generic` пригоден для нейтрального обмена, но **не считается engine-ready**. Для конкретного движка отдельно фиксируются импорт геометрии/материалов, collision layers/masks, solver settings, joints, разрушение, soft bodies, скрипты, события и ограничения. Отсутствующие в движке возможности реализуются плагином/скриптом или получают статус `unsupported`; никакой «тихой» потери данных.

**Гейты:** draft допускает пропуски в Markdown; `engine-ready` требует успешной проверки JSON Schema, ссылочной целостности, применимости возможностей, наличия внешних ресурсов, адаптера и **реального импорта с тестовым сценарием**. Валидатор репозитория сейчас не меняем; проверки этого контракта пока нормативные, не заявляются как автоматизированные.

## English

**Normative v1.0.** Human-readable OBJ/ART/PHYS cards feed a **typed JSON manifest** governed by [JSON Schema](../templates/engine-asset.schema.json). It is **not** a native Unreal/Unity/Godot asset: a version-specific deterministic adapter and tested import are necessary.

Use UTF-8 JSON, strict field types, required keys, bounded arrays and strings, enumerations, numeric ranges, SI units, radians, linear RGB [0,1], metallic/roughness [0,1]. No NaN/Infinity or numbers encoded as localized strings. Unknown values may appear in drafts but not in required export parameters. N/A means omitted optional field with a documented exception. String and array limits are **project contract limits**, not claims about engine limits.

Keep stable part IDs across geometry, joints, damage zones, fracture, states and visuals; reject dangling references. Damage thresholds, accumulation, state transitions and functional effects must be explicit. HP is an abstract gameplay value, not physical energy. Define fracture clusters, debris budgets and deformable solver inputs when relevant.

`engine.target` names the target and version plus adapter version. `generic` is portable but not engine-ready. Missing engine capabilities must be implemented explicitly or marked unsupported; no silent dropping. Engine-ready requires schema conformance, reference integrity, asset availability, capability mapping and a successful import/behavior test. The repository validator is unchanged.

### Public technical references / Публичные технические источники

- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12)
- [Unreal Engine — Chaos Destruction](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-destruction-in-unreal-engine)
- [Unreal Engine — Physical Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physical-materials-in-unreal-engine)
- [Unity — Physics](https://docs.unity3d.com/Manual/PhysicsSection.html)
- [Godot — Physics introduction](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html)
- [glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)

These document different APIs and import formats; none defines a universal all-engine physical-object JSON file.
