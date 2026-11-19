# Physical Behavior Specification / Формуляр физических свойств объекта

**Applies to:** a fictional OBJ with one or more physical implementations. Fill this form alongside [3D Production Specification](3d-production-spec.md). Use `unknown` for unmeasured values and `N/A: reason` only when physically inapplicable. Unknowns block the relevant simulation readiness gate; do not fabricate numbers.

```yaml
---
id: OBJ-0001-PHYS-v0-1
title: "Physical behavior / Физическое поведение"
status: draft
owner: unassigned
updated: 2026-11-19
source: "OBJ-0001"
ai_assistance: "none"
version: v0-1
object_id: OBJ-0001
simulation_mode: "visual"
---
```

## 1. Модель и границы / Model and scope
- Object and version / Объект и версия:
- Mode / Режим: visual | game-physics | engineering
- Intended phenomena and interactions / Моделируемые явления:
- Engine/solver, version, precision, time step / Движок, решатель, точность, шаг времени:
- Coordinate axes, SI units, reference frame / Оси, единицы СИ, система отсчёта:
- Assumptions, simplifications, uncertainty / Допущения, упрощения, неопределённости:
- Sources for every numeric parameter / Источники численных параметров:
- Calibration / Калибровка:
- Expected accuracy and validation envelope / Точность и диапазон применимости:

## 2. Масса и инерция / Mass and inertia
| Component ID | Mass (kg) | Center of mass (m; XYZ) | Inertia tensor (kg·m²; 3×3) | Source | Uncertainty |
| --- | --- | --- | --- | --- | --- |
| pending | unknown | unknown | unknown | unknown | unknown |
- Total mass and center of mass / Полная масса и центр масс:
- Density (kg/m³) and spatial distribution / Плотность и распределение:
- Hollow volumes, fluids, payload, moving mass / Полости, жидкости, груз, подвижные массы:
- Mass variation over operating states / Изменение массы при работе:

## 3. Материалы: механика / Mechanical material properties
| Part | Material and grade | Density kg/m³ | Young's E Pa | Poisson ν | Yield/ultimate strength Pa | Source |
| --- | --- | --- | --- | --- | --- | --- |
| pending | unknown | unknown | unknown | unknown | unknown | unknown |
- Elastic/plastic behavior and hardening / Упругость, пластичность, упрочнение:
- Shear/bulk moduli, anisotropy / Сдвиг, объёмная упругость, анизотропия:
- Flexibility/bending stiffness (N·m²) / Гибкость и изгибная жёсткость:
- Damping, hysteresis, viscoelasticity / Демпфирование, гистерезис, вязкоупругость:
- Compression/tension/shear limits / Пределы сжатия, растяжения и сдвига:
- Fracture toughness (Pa·√m), impact resistance (J), brittleness / Вязкость разрушения, ударопрочность, хрупкость:
- Fatigue, creep, wear and aging / Усталость, ползучесть, износ, старение:
- Temperature/humidity dependence / Зависимость от температуры и влажности:
- For fabrics/leather: thickness, drape, warp/weft stiffness, tearing / Ткани и кожа: толщина, драпировка, продольная/поперечная жёсткость, разрыв:
- For wood: grain direction, moisture, anisotropy / Дерево: волокна, влажность, анизотропия:
- For glass/ceramic: brittle fracture and crack behavior / Стекло, керамика: хрупкое разрушение:

## 4. Контакты и столкновения / Contacts and collisions
- Collision representation and layers / Геометрия и слои коллизий:
- Static/dynamic friction coefficients μs/μk / Статическое и динамическое трение:
- Rolling resistance, restitution e, contact stiffness/damping / Качение, упругость удара, жёсткость и демпфирование контакта:
- Surface roughness and contact material pairs / Шероховатость и пары материалов:
- Self-collision, penetration tolerance, continuous collision / Самоколлизии, допуски проникновения, непрерывные столкновения:
- Grounding, supports, constraints / Опоры и закрепления:
- Break/tear threshold and failure behavior / Порог разрушения и поведение при отказе:
- Debris/fragment behavior and conservation assumptions / Осколки, обломки и допущения:

## 5. Кинематика и динамика / Kinematics and dynamics
| Joint ID | Connected parts | Type | Axis/frame | Range (rad/m) | Stiffness | Damping | Break threshold |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pending | pending | pending | pending | pending | pending | pending | pending |
- Forces, torques, gravity, drag / Силы, моменты, гравитация, сопротивление:
- Actuators, drives, power sources / Приводы, двигатели, источники энергии:
- Torque-speed, force-displacement, efficiency curves / Характеристики момента, усилия и КПД:
- Operating states and state transitions / Режимы работы и переходы:
- Control signals and feedback / Управление и обратная связь:
- Vibrations, resonance, noise / Вибрации, резонанс, шум:
- Kinetic energy and momentum constraints / Энергия и импульс:

## 6. Тепло, энергия и жидкости / Thermal, energy, fluids
- Thermal conductivity W/(m·K), specific heat J/(kg·K), expansion 1/K / Теплопроводность, теплоёмкость, расширение:
- Operating and failure temperatures (K or °C; label units) / Температуры работы и отказа:
- Heat flux, radiation/emissivity, convection / Тепловые потоки, излучательная способность, конвекция:
- Fuel/energy input, output, efficiency, losses / Топливо, энергия, КПД, потери:
- Fluid type, density, viscosity, compressibility / Жидкости и газы, плотность, вязкость, сжимаемость:
- Pressure (Pa), flow (m³/s or kg/s), pipe geometry / Давление, расход, трубопроводы:
- Leakage, condensation, boiling, freezing, phase change / Утечки, конденсация, кипение, замерзание:
- Environmental effects: rain, snow, wind, soot, corrosion / Дождь, снег, ветер, сажа, коррозия:
- Electrical conductivity, voltage/current, insulation if applicable / Электрические параметры:

## 7. Оптика, поверхность и рендер / Optical and surface response
| Surface ID | Base color (linear/sRGB stated) | Metallic | Roughness 0–1 | IOR | Opacity/transmission | Source |
| --- | --- | --- | --- | --- | --- | --- |
| pending | unknown | unknown | unknown | unknown | unknown | unknown |
- Gloss vs matte: microfacet roughness and reflection model / Глянец и матовость: микрошероховатость и модель отражения:
- Specular level, anisotropy, clearcoat, sheen / Блики, анизотропия, лак, тканевый блеск:
- Subsurface scattering, thickness, absorption / Подповерхностное рассеяние, толщина, поглощение:
- Normal/bump/displacement maps and measured scale / Карты микрорельефа и масштаб:
- Emissive behavior, intensity and color / Свечение, интенсивность и цвет:
- Dirt, wetness, frost, scratches, patina, soot / Грязь, влажность, иней, царапины, патина, сажа:
- Texture resolution, UV density, shader convention / Текстуры, UV, шейдер:
- Lighting/render calibration and reference conditions / Калибровка освещения и референсы:

## 8. Деформация, повреждение и разрушение / Deformation, damage, destruction
- Deformation type: rigid | cloth | soft body | elastic | plastic | fracture / Тип деформации:
- Stress/strain curve or constitutive model / Диаграмма напряжение–деформация:
- Mesh resolution and solver parameters / Сетка и параметры решателя:
- Damage initiation and propagation / Возникновение и развитие повреждений:
- Fracture pattern, fragment mass/energy treatment / Схема разрушения и масса осколков:
- Tearing, bending, buckling, compression / Разрыв, изгиб, потеря устойчивости, сжатие:
- Thermal/chemical aging, corrosion / Термическое и химическое старение, коррозия:
- Persistence and reset/repair rules / Сохранение повреждений и ремонт:

## 9. Состояния, взаимодействия и воспроизводимость / States and reproducibility
- Initial and boundary conditions / Начальные и граничные условия:
- Environmental scenarios / Сценарии среды:
- State machine and interaction events / Автомат состояний и события:
- Random seeds and deterministic settings where available / Seed и детерминизм:
- Time step, substeps, solver tolerances / Шаг, подшаги, допуски:
- Numerical stability and energy drift / Численная устойчивость, дрейф энергии:
- Input/output signals, logging and expected results / Входы, выходы, журнал и ожидаемые результаты:
- Known nonphysical artistic overrides / Нефизичные художественные допущения:

## 10. Проверка и доказательства / Verification and evidence
| Test | Conditions and expected numeric result | Actual result | Evidence | Reviewer | Pass/fail |
| --- | --- | --- | --- | --- | --- |
| Mass and inertia | pending | pending | pending | pending | pending |
| Contact/friction/restitution | pending | pending | pending | pending | pending |
| Motion and constraints | pending | pending | pending | pending | pending |
| Flex/impact/fracture | pending | pending | pending | pending | pending |
| Thermal/fluids if applicable | pending | pending | pending | pending | pending |
| Optical response and material calibration | pending | pending | pending | pending | pending |
| Integration and reproducibility | pending | pending | pending | pending | pending |

- Validation sources, measured vs estimated vs invented / Измеренные, оценочные и вымышленные значения:
- Deviations and error budgets / Отклонения и допустимые ошибки:
- Missing parameters and blockers / Недостающие параметры и блокеры:
- Physical behavior review decision / Решение о проверке физики:
- Canon decision reference (separate) / Канон отдельно:

**Readiness rule / Правило:** visual mode may approximate physical parameters but must label them as artistic. Game-physics requires all simulation-relevant mass/inertia, contact, joints, and environment parameters and tests. Engineering requires calibrated constitutive laws, source-backed numeric values, boundary conditions, solver settings, uncertainty and quantitative validation; a completed form alone is not proof of engineering fidelity.
