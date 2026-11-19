# Норматив визуального ряда 48/24 / Visual Asset Governance Standard

**Version / Версия:** 1.0 (working governance, 2026-11-19). **Scope / Область:** all depicted material objects, costumes, buildings, machinery, vehicles, interiors, exteriors and props. **Authority:** documentation and production readiness only; does not approve artistic canon or change rights.

## Русский

### 1. Обязательные правила

1. Для каждого самостоятельного вымышленного объекта заводится **OBJ** по [универсальному шаблону](../templates/world-object.md). Исторические предметы — **REF** по [историческому шаблону](../templates/historical-object-reference.md). Каждый самостоятельный рисунок, лист видов, модель или рендер — **ART** по [арт-шаблону](../templates/game-art-asset.md). Один OBJ может иметь несколько REF и ART; копии не заменяют связи.
2. **Обязательная текстовая часть OBJ:** название и ID, назначение, кто и где использует, эпоха, регион, социальная среда, функция, конструкция, материалы, примерный масштаб (или «не определён»), внешний вид, ограничения, исторические источники, связанные объекты, авторство, версия и статус. Неизвестные параметры явно обозначаются как неизвестные.
3. **Обязательный минимальный визуальный пакет для объёмного предмета перед дизайн-ревью:** **анфас (front)** и **профиль (side)**, согласованные между собой по пропорциям; хотя бы один общий вид в 3/4 для объёмного восприятия; обозначение масштаба; материалы и ключевые детали. До готовности видов допускается статус `draft` и явный список недостающего.
4. **Дополнительные виды по геометрии и назначению:** сзади, сверху, снизу, второй профиль, разрез, взрыв-схема, план, развёртка, схема действия. Для зданий **экстерьер** требует фасада и бокового вида/разреза; **интерьер** требует плана и минимум двух направлений обзора. Для костюма — фронт, профиль, спина и конструктивные детали. Для асимметричных предметов нужны обе стороны.
5. **Функция:** назначение, принцип действия, способы использования и обслуживания, уязвимости и ограничения должны быть объяснимы. Если это декоративный объект, укажите это прямо.
6. **Арт-лист:** единый ID и версия, название, дата, художник/ответственный, OBJ ID, стадия, подписи видов, масштаб и единицы, обозначения материалов, ссылки на источники и исходники. Рисунки разных вариантов не должны молча подменять друг друга.
7. **Производственная передача:** оригинальный редактируемый файл, экспорт/превью, имена файлов, цветовое пространство, размер/разрешение, версии, производные, лицензии, AI provenance, контроль качества. Бинарный ресурс в Git требует паспорт `.asset.json`; крупные исходники — внешняя ссылка и хеш согласно [ASSET_WORKFLOW](ASSET_WORKFLOW.md).
8. **Контроль приёмки:** визуальная согласованность видов, физическая и историческая правдоподобность в пределах допущений мира, точность надписей и дореформенной орфографии, материалы, износ, пропорции, освещение и читаемость силуэта. Пробелы фиксируются; не изображайте непроверенную работу как готовую.
9. **Статусы:** `draft` — допускается неполный пакет; `review` — минимум выполнен или есть обоснованные `N/A`; `canonical` — только после действительного согласия двух соавторов по [CANON_POLICY](CANON_POLICY.md). Дизайн-ревью само по себе не делает объект каноном.

### 2. Применимость

Для плоского орнамента, шрифта или карты требование профиля может быть `N/A` с причиной. Для абстрактной идеи без рисунков сначала используйте [inbox](inbox/README.md). Требования к двум видам применяются **на этапе дизайн-ревью**, а не как барьер при первичной записи идеи.

### 3. Открытые профессиональные источники и границы заимствования

- [Blender Studio — Naming Conventions](https://studio.blender.org/tools/naming-conventions/introduction): идентификаторы, типы, задачи, варианты, версии.
- [Blender Studio — Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline): распределение ответственности по этапам, публикация и версии ресурса.
- [Blender Studio — File Naming](https://studio.blender.org/tools/naming-conventions/file-types): классификация ассетов, текстуры, модели, сцены.

**Важно:** эти источники подтверждают практики пайплайна и именования, но **не предписывают универсально обязательные виды «анфас + профиль»**. Набор обязательных видов выше — **собственный норматив 48/24**, сформулированный для контроля геометрии и воспроизводимости. Мы не выдаём его за официальный стандарт Blender Studio.

## English

### 1. Binding documentation requirements

1. Create a distinct **OBJ** record for each fictional object, a **REF** record for each historical prototype, and a separate **ART** record for each depiction or production asset. Cross-reference IDs rather than duplicating files.
2. Every OBJ records its ID, name, purpose, users, era, region, social context, operation, construction, materials, approximate scale (or unknown), appearance, constraints, historical sources, related objects, contributors, version, and status.
3. **Minimum visual package for three-dimensional objects before design review:** consistent **front and side orthographic views**, at least one **three-quarter view**, a scale indicator, and material/detail callouts. Early drafts may remain incomplete with documented gaps.
4. Add back/top/bottom/opposite side views, sections, exploded diagrams, plans, or operating diagrams as needed. Building exteriors require an elevation plus side view/section; interiors require a plan plus at least two views; costumes require front/side/back and construction details; asymmetric objects require both sides.
5. Explain function, use, maintenance, and constraints; identify purely decorative objects as such.
6. Each art sheet identifies its ART ID, version, title, date, artist/owner, depicted OBJ, stage, view labels, scale/units, material callouts, references, and editable sources.
7. Handoff includes editable master, exports, naming, color space, resolution, versions, derivatives, licences, AI provenance, QA, and rights sidecars under [ASSET_WORKFLOW](ASSET_WORKFLOW.md).
8. Review checks view consistency, setting plausibility, exact historical-style inscriptions, materials, wear, proportions, lighting, and silhouette. Record missing work explicitly.
9. `draft` may be incomplete; `review` requires the minimum or justified N/A; `canonical` requires actual approvals by both coauthors under [CANON_POLICY](CANON_POLICY.md).

### 2. Applicability

Flat ornament, fonts, and maps may mark side views N/A with a reason. Raw ideas belong in the [inbox](inbox/README.md). Required views are a **design-review gate**, not a condition for initial capture.

### 3. External foundations and provenance

[Blender Studio Naming Conventions](https://studio.blender.org/tools/naming-conventions/introduction), [Blender Studio Asset Pipeline](https://studio.blender.org/tools/addons/asset_pipeline), and [File Naming](https://studio.blender.org/tools/naming-conventions/file-types) support naming, task-layer ownership, versions, and publishing practices. **The front/side minimum is a project-specific 48/24 rule**, not a requirement attributed to Blender Studio.
