# 3D Production Specification / Технический формуляр 3D-ресурса

**Use:** one ART production asset linked to one OBJ; fill all fields or state `unknown` / `N/A: reason`. A placeholder is **not** acceptance. This form is required for **L2 Modeling Ready**; the L3 section records actual delivered files and tests. It does not force a particular engine before selection.

```yaml
---
id: ART-0001
title: "3D specification / Техническая спецификация"
status: draft
owner: unassigned
updated: 2026-11-19
source: "OBJ-0001"
ai_assistance: "none"
version: v0-1
object_id: OBJ-0001
readiness: L1
reference_ids: []
---
```

## 1. Назначение / Purpose
- Asset class / Класс:
- Product, scene, camera distance / Продукт, сцена, расстояние камеры:
- Gameplay role / Игровая роль: static | interactive | animated | destructible | modular
- Target engine and version / Движок и версия: TBD if not selected
- Target platform and performance tier / Платформа и производительность:
- Target fidelity and visual style / Детализация и художественный стиль:
- Owner, modeler, reviewer / Ответственный, моделлер, проверяющий:
- OBJ ID, concept ART IDs, historical REF IDs:
- Historical vs fictional departures / Отличия от исторических прототипов:

## 2. Геометрия и измерения / Geometry and measurements
- Unit / Единицы: meters (m); specify all dimensions in m
- Bounding dimensions X × Y × Z (m) / Габариты:
- Reference measurements and confidence / Источник размеров и достоверность:
- Scale figure or object / Масштабный ориентир:
- Coordinate convention / Оси: document forward, up, right; engine conversion if needed
- Origin/pivot location / Начало координат и pivot:
- Real-world orientation / Положение в пространстве:
- Symmetry / Симметрия, исключения:
- Parts list / Составные части (ID, name, dimensions, attachment):
- Clearance, fit, mechanical tolerances / Зазоры и допуски:
- Visible and hidden geometry / Видимая и скрытая геометрия:
- Critical silhouette and protected dimensions / Критический силуэт и размеры:
- Modular grid and snapping (if applicable) / Модульная сетка:
- Geometry assumptions needing design approval / Неопределённости:

## 3. Чертежи и виды / Drawings and views
| View / Вид | Linked ART/file | Projection / Проекция | Scale / Масштаб | Checked / Проверено |
| --- | --- | --- | --- | --- |
| Front / Анфас | pending | orthographic | pending | no |
| Side / Профиль | pending | orthographic | pending | no |
| Back / Сзади | pending | orthographic or N/A | pending | no |
| Top / Сверху | pending | orthographic or N/A | pending | no |
| 3/4 / Три четверти | pending | perspective | reference only | no |
| Detail, section, exploded / Детали, разрезы | pending | as needed | pending | no |

- Shared dimension lines and cross-view consistency / Общие размерные линии и согласование:
- Material callout legend / Обозначения материалов:
- Inscription artwork and exact spelling / Надписи:
- Reference board and annotated uncertainties / Референсы и сомнения:

## 4. Материалы и производство / Materials and construction
| Part ID | Material | Finish/coating | Roughness/metallic intent | Wear/damage | Source |
| --- | --- | --- | --- | --- | --- |
| pending | pending | pending | pending | pending | pending |

- Construction methods and seams / Изготовление, швы, крепления:
- Assembly/disassembly and maintenance / Сборка, обслуживание:
- Motion constraints and mechanical states / Движение, состояния:
- Climate, grime, snow, condensation, soot / Климат, грязь, снег, конденсат, сажа:
- Physical impossibilities or artistic exceptions / Допущения:

## 5. 3D mesh / Сетка
- Mesh use / Назначение: high-poly sculpt | low-poly realtime | cinematic
- Triangle budget per LOD and viewing distance / Бюджет треугольников по LOD:
- LOD count and switching policy / Количество LOD и переключение:
- Topology / Топология: deforming vs rigid, edge-flow, ngons policy:
- Smoothing, hard edges, normals, weighted normals / Нормали и сглаживание:
- Bevel width in m and bake strategy / Фаски и запекание:
- Separate mesh objects and naming / Разбиение и имена:
- Instancing and modularity / Инстансинг и модульность:
- Collision geometry / Коллизии: primitive | convex | custom; gameplay constraints:
- Occlusion and visibility / Окклюзия:
- QA: manifold where required, flipped normals, duplicate faces, degenerate geometry, transforms:

## 6. UV and PBR textures / UV и PBR
- UV sets and purpose / UV-наборы:
- UV overlap policy and padding / Перекрытия и отступы:
- Texel density (px/m) / Плотность текселей:
- Texture sizes and max budget / Разрешение и бюджет:
- UDIM or atlas / UDIM или атлас:
- Tangent basis / Базис касательных:
- Normal map convention / Конвенция normal (OpenGL/DirectX):
- Material workflow / PBR: metallic-roughness or other, explicitly named:
- Required maps / Карты: base color, roughness, metallic, normal, AO; optional height, opacity, emissive, masks:
- Channel packing / Упаковка каналов:
- Color space / Цветовое пространство: sRGB vs linear per map:
- Tileability, seams, decals / Повторяемость, швы, декали:
- Wear masks and variation / Износ, вариативность:
- Texture rights and provenance / Права на текстуры:

## 7. Rig, motion and interactions / Риг, движение и взаимодействие
- Static or animated / Статический или анимированный:
- Hierarchy, bones, joint axes / Иерархия, кости, оси:
- Moving parts, range and limits / Подвижные детали, пределы:
- Animation states, frame rates and transitions / Состояния и переходы:
- Sockets/attachment points / Точки крепления:
- Interaction triggers and gameplay requirements / Взаимодействия:
- Damage, destruction, physics simulation / Разрушение, физика:
- N/A reasons if static / Причина неприменимости:

## 8. Export and integration / Экспорт и интеграция
- Editable master and tool version / Мастер и версия ПО:
- Delivery formats and exact versions / Форматы и версии: FBX | glTF | USD | other:
- Unit scale and axis conversion / Масштаб и оси:
- Transform application and pivot verification / Трансформации и pivot:
- Materials/shaders mapping / Сопоставление шейдеров:
- Collision/LOD naming conventions / Имена коллизий и LOD:
- File paths, naming, dependencies / Пути, имена, зависимости:
- Import test in target engine / Проверка импорта:
- Engine-independent preview if engine TBD / Предпросмотр без движка:
- Reproducible render scene, camera, lights, color management / Сцена рендера, камера, свет:
- Source hashes and external storage links / Хеши и хранилище:

## 9. Проверка и сдача / QA and handoff
| Check | Evidence (path, screenshot, report) | Reviewer | Result |
| --- | --- | --- | --- |
| Dimensions and orthographic agreement | pending | pending | pending |
| Scale, origin, transforms, normals | pending | pending | pending |
| Topology, poly budgets and LOD | pending | pending | pending |
| UVs, texel density, PBR maps | pending | pending | pending |
| Collision, rig and interactions if applicable | pending | pending | pending |
| Master, exports, dependencies and hashes | pending | pending | pending |
| Import and test render | pending | pending | pending |
| Rights, attribution, AI provenance | pending | pending | pending |

- Deviations and approved exceptions / Отклонения:
- Blockers and unresolved decisions / Блокеры:
- L2 decision / Решение о готовности к моделированию: pending
- L3 technical acceptance / Техническая приёмка: pending
- Canon approval reference (separate) / Канон (отдельно): pending

## Type-specific annex / Специализация
- Costume: body measurements, layers, pattern pieces, fabric thickness, cloth simulation, skinning, clipping checks.
- Weapon: mechanical part hierarchy, moving elements, safe depiction, animation sockets, wear states.
- Building exterior: elevations, plans, roof, modules, openings, facade material scale, weathering.
- Building interior: floor plan, ceiling heights, door clearance, lighting/heating fixtures, room modularity.
- Vehicle: chassis and wheels/tracks, articulation, cabin, controls, attachment points, collision.
- Furniture/household: ergonomic dimensions, assembly, handling poses, wear.
- Machinery: power input, moving linkages, clearances, access for maintenance, operating states.

**Rule / Правило:** L2 cannot be marked ready while any applicable geometry-critical field or required view is unknown. Engine-specific values may remain TBD only with a named integration blocker; that means engine integration is **not** ready. L3 requires actual delivered assets and test evidence, not a completed text form.

## Физические свойства / Physical behavior

Для объектов с физическим поведением обязательно связать [Physical Behavior Specification](physical-behavior-spec.md): масса, инерция, упругость, прочность, трение, разрушение, тепловые и оптические параметры. / Link the [physics form](physical-behavior-spec.md) for mass, inertia, elasticity, strength, friction, fracture, thermal and optical behavior.

## Контракт игрового экспорта / Engine export contract

Перед заявлением Game Ready требуется [JSON Schema](engine-asset.schema.json), [пример манифеста](engine-asset.example.json), [профиль движка](engine-implementation-profile.md) и успешный тест импорта. / Game Ready requires a schema-compliant manifest, a versioned engine adapter and import evidence. No direct import of Markdown is implied.
