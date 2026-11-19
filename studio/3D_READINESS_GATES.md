# 3D Production Readiness / Готовность к 3D-производству

## Русский

Этот документ дополняет [VISUAL_GOVERNANCE](VISUAL_GOVERNANCE.md), [OBJECT_STANDARD](OBJECT_STANDARD.md) и [формуляр 3D](../templates/3d-production-spec.md). Он **не** меняет статусы канона: `draft/review/canonical` описывают художественное согласование, а L1/L2/L3 — производственную готовность.

| Gate | Минимум для перехода | Запрещено считать достаточным |
| --- | --- | --- |
| L0 Captured | OBJ/IDEA ID, источник, описание, ответственный | Одно изображение без контекста |
| L1 Concept Ready | Назначение, эпоха, социальный контекст, исторические REF, анфас и профиль (для объёмного предмета), 3/4, материалы, масштабный ориентир, список неизвестного | Несогласованные перспективные картинки вместо ортографических видов |
| L2 Modeling Ready | Заполнен 3D-формуляр; согласованы размеры и ортографические виды; перечислены детали, материалы, соединения, функции, критические допуски; есть спецификация геометрии, UV/PBR, LOD и экспорта под целевой тип применения; нет блокирующих геометрических неизвестных | `unknown` в критических размерах, противоречивые виды, невыбранная производственная цель |
| L3 Game/Render Ready | Реальные исходники, экспорт, текстуры, проверенная геометрия, согласованный масштаб, контроль импорта/рендера, QA с доказательствами и указанием версии | Один красивый рендер без исходника и проверок |

**Гибкость:** для статичного иллюстрационного объекта допускается `N/A` для рига, коллизий, LOD и игрового импорта с объяснением; L3 тогда означает **Render Ready**, а не Game Ready. Для игрового объекта нельзя пропускать применимые проверки. Пока движок не выбран, разрешена переносимая спецификация, но нельзя утверждать успешную интеграцию в движок.

**Проверка:** ответственный заполняет поля; другой человек проверяет доказательства. Укажите дату, версию, ссылки на файлы и причины исключений. Переход L2/L3 — производственное решение, **не** канонизация. Канон требует отдельных подтверждений обоих соавторов.

**Тест на достаточность:** независимый моделлер должен воспроизвести объект в заявленных пределах без самостоятельного изобретения критической геометрии, конструкции и материалов. Если это невозможно, возвращаем на уточнение L2.

## English

This policy supplements [visual governance](VISUAL_GOVERNANCE.md), the [object standard](OBJECT_STANDARD.md), and the [3D production form](../templates/3d-production-spec.md). Creative status and production readiness are separate.

- **L0 Captured:** identity, source, basic description and responsible person.
- **L1 Concept Ready:** purpose, era/context, references, consistent front/side and 3/4 views as applicable, material intent, scale reference, open questions.
- **L2 Modeling Ready:** completed technical form, resolved critical dimensions, orthographic consistency, part breakdown, materials, functions, topology/UV/PBR/LOD/export requirements appropriate to the deliverable. No geometry-critical unknowns.
- **L3 Game/Render Ready:** actual editable master, exports, textures, geometry/scale validation, import or render test, QA evidence and versioned handoff.

A static illustration may mark rigging, collision, LOD or game import N/A with reasons and reach **Render Ready**, not Game Ready. A game asset must pass relevant checks. If the engine is undecided, portable specifications are allowed, but engine integration cannot be claimed complete.

A second reviewer checks evidence. L2/L3 are production gates, not canon approval. An independent modeler should be able to build within specified tolerances without inventing critical geometry, construction or materials.

## Engine-ready addendum / Дополнение к готовности движка

Для L3 Game Ready дополнительно обязательны типизированный [контракт данных](ENGINE_DATA_CONTRACT.md), ссылочная целостность ID, [профиль реализации](../templates/engine-implementation-profile.md), проверка возможностей и фактический импорт. Соответствие JSON Schema без адаптера и теста не означает Game Ready. / Engine-ready requires a typed manifest, resolved references, versioned adapter, capability mapping and a successful import/behavior test.
