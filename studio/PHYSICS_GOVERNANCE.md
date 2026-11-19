# Physics Governance / Норматив физического поведения объектов

## Русский

Применяется к материальным объектам 48/24 вместе с [OBJECT_STANDARD](OBJECT_STANDARD.md), [VISUAL_GOVERNANCE](VISUAL_GOVERNANCE.md) и [3D_READINESS_GATES](3D_READINESS_GATES.md). Для каждого OBJ, которому нужна физика, заполните [Physical Behavior Specification](../templates/physical-behavior-spec.md). Физическая модель описывает поведение, а ART-файл — геометрию и визуальную реализацию; связи через ID.

**Режимы точности:**
- **P0 Visual:** визуальная имитация, правдоподобный вид и анимация. Физические коэффициенты могут быть художественными приближениями с явной маркировкой. Не заявлять инженерную достоверность.
- **P1 Game Physics:** воспроизводимая игровая физика. Обязательны масса, центр масс, инерция, коллизии, коэффициенты трения/упругости, соединения, пределы движения, внешние силы, взаимодействия, параметры решателя и тесты для применимых явлений.
- **P2 Engineering:** проверяемая физическая модель. Обязательны измеренные или обоснованные свойства материалов, законы деформации и разрушения, начальные/граничные условия, численные методы, погрешности, чувствительность, источники данных, калибровка и количественная валидация. Это уровень моделирования, **не сертификация реального изделия**.

**Обязательные семейства свойств:** плотность и масса; центр масс и инерция; упругость, гибкость, пластичность, хрупкость, ударопрочность; трение, сцепление и отскок; кинематика, усилия, привод; тепловые свойства, жидкости и энергия; электрика при необходимости; оптический отклик — глянец/матовость, roughness, отражение, прозрачность, преломление; износ, загрязнение, повреждения и разрушение; окружающая среда; сценарии взаимодействия и тесты.

**Правила заполнения:** все поля заполнены значением, `unknown` или `N/A: reason`. Для P1/P2 `unknown` в релевантных параметрах блокирует приёмку. Каждое число содержит единицу СИ, источник, способ получения (измерено/вычислено/оценено/художественно), диапазон и неопределённость, где применимо. `N/A` допустимо только с объяснением. Отдельно фиксируются допущения альтернативной физики мира; они не выдаются за реальные научные факты.

**Проверка:** тесты привязываются к версии объекта, геометрии, материалам и движку/решателю. Укажите начальные условия, шаг времени, ожидаемые численные результаты, допуски и реальные доказательства. Красивый рендер не подтверждает динамику, а заполненный формуляр не доказывает правильность модели.

**Разделение решений:** P0/P1/P2 — физическая готовность; L0–L3 — готовность художественного ресурса; `draft/canonical` — художественный статус. Ни один из этих статусов не подменяет другой. Канон требует отдельного подтверждения обоих соавторов.

## English

Applies to physical objects alongside [OBJECT_STANDARD](OBJECT_STANDARD.md), [VISUAL_GOVERNANCE](VISUAL_GOVERNANCE.md), and [3D_READINESS_GATES](3D_READINESS_GATES.md). Each OBJ requiring simulation uses the [Physical Behavior Specification](../templates/physical-behavior-spec.md). Physics describes behavior; ART describes geometric/visual realization; cross-link by ID.

**Fidelity modes:** **P0 Visual** (art-directed approximations explicitly labeled), **P1 Game Physics** (mass, inertia, contact, joints, forces, environment, solver settings and tests for relevant behavior), **P2 Engineering** (source-backed material laws, boundary conditions, numerical method, uncertainty, calibration and quantitative validation; not product certification).

**Property families:** density, mass, center of mass, inertia; elasticity, flexibility, plasticity, brittleness, impact resistance; friction and restitution; kinematics, loads and actuation; heat, fluids and energy; electrical behavior where relevant; optical response including gloss/matte, roughness, reflectance, transparency and refraction; wear, damage and fracture; environment; reproducible scenarios and tests.

**Completion rules:** enter a value, `unknown`, or justified `N/A`. Unknown simulation-critical values block P1/P2 acceptance. Numeric values need units, provenance, acquisition method, ranges and uncertainty as applicable. Fictional deviations must be explicit. Tests must identify object/model versions, solver, initial conditions, expected numeric outcomes, tolerances and evidence. Neither a render nor a completed form proves physical validity.

**Separate statuses:** P0/P1/P2 physics fidelity, L0–L3 art readiness, and creative draft/canon status are distinct; canon still needs both coauthors' approvals.
