# Ресурсы и продукты / Assets and products

[Все инструкции / All guides](README.md) · [Выбор папки / Choose a folder](../NAVIGATION.md) · [Правила ресурсов / Asset policy](../ASSET_WORKFLOW.md)

## Русский

### Начните с назначения

Сначала определите, что создаётся: источник для исследования, объект вымышленного мира, изображение или звук, либо реализация для конкретного продукта. Для сырой смешанной идеи достаточно [inbox](../inbox/README.md). Не нужно заранее заполнять производственные формуляры, которые не относятся к её текущему этапу.

| Материал | Рабочее место | Полезная форма или правило |
| --- | --- | --- |
| Исторический предмет или внешний визуальный источник | [research/visual-references/drafts](../../research/visual-references/drafts/README.md), [исторические коллекции](../../research/visual-references/drafts/historical-collections/README.md) | [REF](../../templates/historical-object-reference.md) |
| Функция, конструкция и контекст вымышленного предмета | Профильная область `world` или `art`, затем `drafts`; например, [технологии](../../world/technology/drafts/README.md), [костюмы](../../art/character-design/drafts/costumes/README.md), [бытовые вещи](../../art/props/drafts/household-objects/README.md) | [OBJ](../../templates/world-object.md), [стандарт объектов](../OBJECT_STANDARD.md) |
| Концепт, чертёж, модель или рендер | Нужный раздел [art](../../art/README.md), затем `drafts` | [ART](../../templates/game-art-asset.md), [арт-бриф](../../templates/art-brief.md) |
| Цветовая система | [art/palettes/drafts](../../art/palettes/drafts/README.md) | [Палитра](../../templates/palette.md) |
| Шрифт, надписи, орфография и набор | [art/typography/drafts](../../art/typography/drafts/README.md) | [Гарнитура](../../templates/font.md), [реестр шрифтов](../../art/typography/drafts/font-register.csv) |
| Музыка, звуковая среда или голос | [audio/music](../../audio/music/README.md), [sound-design](../../audio/sound-design/README.md), [voices](../../audio/voices/README.md), затем `drafts` | Бриф, метаданные и [паспорт файла](../../templates/asset.example.json) |
| Адаптация для игры, видео, настолки или книги | Нужный раздел [products](../../products/README.md), затем `drafts` | [Манифест адаптации](../../templates/adaptation.md) |

Выберите одно основное место для карточки. Если объект относится к нескольким направлениям, добавьте связи, а не одинаковые копии. Название папки помогает найти объект, а ID позволяет сохранить его идентичность при развитии.

### Источник, объект и изображение — три связанные записи

По [стандарту объектов](../OBJECT_STANDARD.md), `REF` описывает реальный источник, `OBJ` — вымышленный объект, `ART` — конкретное изображение или производственную реализацию. Один OBJ может опираться на несколько REF и иметь несколько ART.

Например, запись о музейном пальто хранит его атрибуцию и ссылку. Карточка костюма героя описывает авторский вариант, функцию и контекст. Эскиз, лист видов и 3D-модель получают свои записи реализации со связью с этим костюмом. Права на музейный снимок не возникают из того, что он указан как референс.

Укажите известные характеристики и источники; неизвестные оставьте обозначенными как неизвестные. Не придумывайте историческую атрибуцию, размеры, свойства материала или согласие авторов ради заполненной таблицы.

### Какой стандарт читать на каком этапе

| Текущая задача | Читайте | Что проверить перед передачей |
| --- | --- | --- |
| Описать объект | [OBJECT_STANDARD](../OBJECT_STANDARD.md) | ID, функция, контекст, описание, происхождение, связи и открытые вопросы |
| Подготовить дизайн к рассмотрению | [VISUAL_GOVERNANCE](../VISUAL_GOVERNANCE.md) | Применимые виды, масштаб, материалы, детали и согласованность; неполнота раннего черновика явно обозначена |
| Передать объект в моделирование или получить готовый ресурс | [3D_READINESS_GATES](../3D_READINESS_GATES.md), [3D-формуляр](../../templates/3d-production-spec.md) | Заявленному L0–L3 соответствуют реальные материалы и проверки |
| Описать физическое поведение | [PHYSICS_GOVERNANCE](../PHYSICS_GOVERNANCE.md), [физическая спецификация](../../templates/physical-behavior-spec.md) | Выбран P0/P1/P2; единицы, источники, допущения и проверки соответствуют назначению |
| Подключить объект к игре | [ENGINE_DATA_CONTRACT](../ENGINE_DATA_CONTRACT.md), [профиль реализации](../../templates/engine-implementation-profile.md), [JSON Schema](../../templates/engine-asset.schema.json) | Связи, ресурсы, выбранная версия движка, адаптер и фактический тест импорта/поведения |

Эти шкалы независимы. `draft/review/canonical` — творческий статус; L0–L3 — готовность ресурса к производству; P0–P2 — режим физической модели. Красивый рендер не доказывает игровую готовность. Успешная проверка JSON не доказывает работу в движке. Существующий общий валидатор репозитория не заменяет все специальные проверки контракта движка.

### Что положить рядом с файлом

Для каждого публикуемого бинарного ресурса нужен соседний `<filename>.<ext>.asset.json` по [образцу](../../templates/asset.example.json): ID, название, статус, ответственный, дата, происхождение, права, использование ИИ и SHA-256 фактического файла. Заполните [реестр ресурсов](../registers/asset-register.csv), если регистрируете ресурс, и [реестр сторонних прав](../../legal/THIRD_PARTY_ASSETS.csv), если применимо.

В [ASSET_WORKFLOW](../ASSET_WORKFLOW.md) установлен локальный предел 20 MiB на бинарный файл. Большие мастера, видео, стемы и производственные сцены подключаются через согласованное внешнее хранилище: в Git остаются карточка, допустимая ссылка, версия, размер и хеш. Не создавайте пустой файл или фиктивный LFS-указатель вместо отсутствующего мастера. Подключение нового хранилища или платного сервиса — отдельное решение.

При неподтверждённых правах сохраните допустимую ссылку и описание вопроса; сам файл не загружайте. Для шрифтов учитывайте разрешённые способы встраивания и передачи. Для аудио фиксируйте права на использованные композиции, записи и исполнение. Для ИИ отмечайте известный инструмент, входные материалы, существенную обработку человеком и ограничения; неизвестную модель или seed не придумывайте.

### Как связать с будущим продуктом

Общий мир остаётся в `world`, история — в `narrative`, общие ресурсы — в `art` и `audio`. В `products` описывайте применение: игровой квест или механика, сценарий видео, правила и компоненты настолки, редакция книги. Укажите используемые ID, версию или commit основы и особенности адаптации по [стратегии продуктов](../PRODUCT_STRATEGY.md).

Для игры уже есть отдельные рабочие папки [технической архитектуры](../../products/video-game/drafts/technical-architecture/README.md), [систем](../../products/video-game/drafts/gameplay-systems/README.md), [прототипов](../../products/video-game/drafts/prototypes/README.md), [конвейера ресурсов](../../products/video-game/drafts/asset-pipeline/README.md) и [тестов](../../products/video-game/drafts/tests/README.md). Наличие папки не означает, что движок выбран или производство уже запущено.

Перед передачей проверьте применимые требования, ссылки и права, затем выполните общую проверку по [инструкции инструментов](../../tools/README.md). Запишите фактический результат и оставшиеся препятствия. Готовность к публикации оформляется отдельно по [процессу выпуска](../RELEASE_PROCESS.md).

## English

### Start with the purpose

Identify whether you are creating research evidence, a fictional object, an image or sound, or a product-specific implementation. Capture a raw mixed idea in the [inbox](../inbox/README.md). Production forms are needed when their stage becomes relevant.

| Material | Workspace | Useful form or rule |
| --- | --- | --- |
| Historical object or external visual source | [research/visual-references/drafts](../../research/visual-references/drafts/README.md), [historical collections](../../research/visual-references/drafts/historical-collections/README.md) | [REF](../../templates/historical-object-reference.md) |
| Function, construction and context of a fictional object | Relevant `world` or `art` area, then `drafts`; for example [technology](../../world/technology/drafts/README.md), [costumes](../../art/character-design/drafts/costumes/README.md) or [household objects](../../art/props/drafts/household-objects/README.md) | [OBJ](../../templates/world-object.md), [object standard](../OBJECT_STANDARD.md) |
| Concept, drawing, model or render | Relevant [art](../../art/README.md) area, then `drafts` | [ART](../../templates/game-art-asset.md), [art brief](../../templates/art-brief.md) |
| Color system | [art/palettes/drafts](../../art/palettes/drafts/README.md) | [Palette](../../templates/palette.md) |
| Typeface, inscriptions, orthography and typesetting | [art/typography/drafts](../../art/typography/drafts/README.md) | [Typeface](../../templates/font.md), [font register](../../art/typography/drafts/font-register.csv) |
| Music, soundscape or voice | [audio/music](../../audio/music/README.md), [sound-design](../../audio/sound-design/README.md) or [voices](../../audio/voices/README.md), then `drafts` | Brief, metadata and [file sidecar](../../templates/asset.example.json) |
| Game, video, tabletop or book adaptation | Relevant [products](../../products/README.md) area, then `drafts` | [Adaptation manifest](../../templates/adaptation.md) |

Choose one primary home for a record. Link related domains rather than duplicating the same record. Its path helps discovery; its ID preserves identity as it develops.

### Source, object and depiction are linked records

Under the [object standard](../OBJECT_STANDARD.md), `REF` identifies a real source, `OBJ` a fictional object, and `ART` a specific depiction or production implementation. One OBJ can reference multiple REF records and have several ART realizations.

For example, a museum coat record stores attribution and a link. A character costume record describes the fictional version, purpose and context. Its sketch, model sheet and 3D model each have implementation records linked to the costume. Citing a museum image does not grant rights to copy it.

Record known properties and their sources; mark unknowns explicitly. Do not invent attribution, dimensions, material properties or approvals to complete a table.

### Which standard applies at each stage

| Task | Read | Check before handoff |
| --- | --- | --- |
| Describe an object | [OBJECT_STANDARD](../OBJECT_STANDARD.md) | ID, function, context, description, provenance, links and open questions |
| Prepare design review | [VISUAL_GOVERNANCE](../VISUAL_GOVERNANCE.md) | Applicable views, scale, materials, details and consistency; early-draft gaps are explicit |
| Hand off for modeling or deliver a finished asset | [3D_READINESS_GATES](../3D_READINESS_GATES.md), [3D form](../../templates/3d-production-spec.md) | Actual material and checks support the claimed L0–L3 stage |
| Describe physical behavior | [PHYSICS_GOVERNANCE](../PHYSICS_GOVERNANCE.md), [physics specification](../../templates/physical-behavior-spec.md) | Selected P0/P1/P2 mode, units, provenance, assumptions and appropriate checks |
| Integrate into a game | [ENGINE_DATA_CONTRACT](../ENGINE_DATA_CONTRACT.md), [implementation profile](../../templates/engine-implementation-profile.md), [JSON Schema](../../templates/engine-asset.schema.json) | Resolved links, available resources, engine version, adapter and actual import/behavior tests |

These scales are independent: `draft/review/canonical` describes creative status; L0–L3 production readiness; P0–P2 physical fidelity. A render does not prove game readiness. Schema conformance does not prove engine behavior. The general repository validator does not replace all specialized engine-contract checks.

### What accompanies a file

Each published binary needs a sibling `<filename>.<ext>.asset.json` following the [example](../../templates/asset.example.json): ID, title, status, responsible person, date, provenance, rights, AI involvement and the actual file's SHA-256. Use the [asset register](../registers/asset-register.csv) when registering an asset and the [third-party rights register](../../legal/THIRD_PARTY_ASSETS.csv) where applicable.

[ASSET_WORKFLOW](../ASSET_WORKFLOW.md) sets a local 20 MiB binary limit. Large masters, video, stems and production scenes use agreed external storage, with a record, permissible link, version, size and hash in Git. Do not replace missing masters with empty files or fake LFS pointers. New storage or paid services require a separate decision.

If rights remain unresolved, retain a permissible link and description of the issue without uploading the file. For fonts, check permitted embedding and redistribution. For audio, record rights to compositions, recordings and performances used. For AI, record known tools, inputs, substantive human editing and limitations; do not invent model versions or seeds.

### Connecting a future product

Shared world material stays in `world`, narrative in `narrative`, and shared assets in `art` and `audio`. `products` describes their use in quests, mechanics, video scripts, tabletop rules/components or book editions. Identify source IDs, the baseline version or commit, and adaptation differences under the [product strategy](../PRODUCT_STRATEGY.md).

The game workspace already separates [technical architecture](../../products/video-game/drafts/technical-architecture/README.md), [gameplay systems](../../products/video-game/drafts/gameplay-systems/README.md), [prototypes](../../products/video-game/drafts/prototypes/README.md), [asset pipeline](../../products/video-game/drafts/asset-pipeline/README.md) and [tests](../../products/video-game/drafts/tests/README.md). A folder's existence does not mean an engine is chosen or production started.

Before handoff, check applicable requirements, links and rights, then run general validation under the [tools instructions](../../tools/README.md). Record actual results and blockers. Publication readiness follows the separate [release process](../RELEASE_PROCESS.md).
