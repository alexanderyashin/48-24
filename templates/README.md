# Шаблоны по задачам / Templates by task

## Русский

Выберите форму и скопируйте её в рабочую папку. Сам шаблон оставьте в этом каталоге. Для сырой идеи используйте inbox; оформленные творческие материалы начинайте в соответствующем `drafts`. Проверьте, что ID ещё не занят, и заполните владельца, дату, источник и участие ИИ по [правилам метаданных](../studio/NAMING_AND_METADATA.md).

Во многих шаблонах метаданные показаны внутри блока кода. В рабочем Markdown перенесите их в самое начало файла, между строками `---`, без внешнего ограждения кода. Заполните обе языковые версии по [языковой политике](../studio/LANGUAGE_POLICY.md). Неизвестные данные указывайте явно; пустая форма не является согласованным материалом.

## English

Choose a form and copy it into the working folder, leaving the template here. Raw ideas go into the inbox; structured creative records normally start in the relevant `drafts`. Check ID availability and fill in the owner, date, source and AI assistance under the [metadata rules](../studio/NAMING_AND_METADATA.md).

Many templates display metadata inside a code fence. In the working Markdown file, put that metadata at the very beginning between `---` lines, without the surrounding fence. Complete both language versions under the [language policy](../studio/LANGUAGE_POLICY.md). State unknowns explicitly; a blank form is not an approved record.

## Идеи и истории / Ideas and stories

| Форма / Form | Рабочее место / Destination |
| --- | --- |
| [Идея / Idea fragment](idea-fragment.md) | [studio/inbox](../studio/inbox/README.md) |
| [Персонаж / Character](character.md) | [narrative/characters/drafts](../narrative/characters/drafts/README.md) |
| [Сюжетная арка / Story arc](story-arc.md) | [narrative/story-arcs/drafts](../narrative/story-arcs/drafts/README.md) |
| [История, глава, выпуск / Episode](episode.md) | [narrative/episodes/drafts](../narrative/episodes/drafts/README.md) |
| [Сцена / Scene](scene.md) | [narrative/scenes/drafts](../narrative/scenes/drafts/README.md) |

Пошаговый пример выбора формы — в [руководстве автора](../studio/guides/writing.md). / See the [writing guide](../studio/guides/writing.md) for choosing and filling a form.

## Мир и исследования / World and research

| Форма / Form | Рабочее место / Destination |
| --- | --- |
| [Положение мира / World entry](world-entry.md) | Подходящий раздел / appropriate area in [world](../world/README.md) |
| [Место / Location](location.md) | [world/geography/drafts](../world/geography/drafts/README.md) |
| [Фракция / Faction](faction.md) | [world/factions/drafts](../world/factions/drafts/README.md) |
| [Технология / Technology](technology.md) | [world/technology/drafts](../world/technology/drafts/README.md) |
| [Исследование / Research](research.md) | Подходящий раздел / appropriate area in [research](../research/README.md) |
| [Исторический объект / Historical reference REF](historical-object-reference.md) | [Исторические коллекции / Historical collections](../research/visual-references/drafts/historical-collections/README.md) |
| [Объект мира / World object OBJ](world-object.md) | Предметный раздел мира по / subject area under [OBJECT_STANDARD](../studio/OBJECT_STANDARD.md) |

## Визуал, физика и реализация / Visuals, physics and implementation

| Форма / Form | Назначение / Purpose |
| --- | --- |
| [Бриф / Art brief](art-brief.md) | Задание на изображение / Image brief |
| [Ресурс ART / ART asset](game-art-asset.md) | Конкретная реализация связанного OBJ / Specific implementation of a linked OBJ |
| [Палитра / Palette](palette.md) | Цвета, пространство, роли / Colours, colour space, roles |
| [Шрифт / Font](font.md) | Гарнитура, применение, лицензия / Typeface, use, licence |
| [3D-формуляр / 3D production specification](3d-production-spec.md) | Модель, виды, материалы, уровни готовности / Model, views, materials, readiness |
| [Физика / Physical behaviour specification](physical-behavior-spec.md) | Проверяемое физическое поведение / Verifiable physical behaviour |
| [Профиль движка / Engine implementation profile](engine-implementation-profile.md) | Реализация для конкретного движка и версии / Implementation for a particular engine and version |
| [Схема данных / Engine asset schema](engine-asset.schema.json) и [пример / example](engine-asset.example.json) | Схема и пример данных; не доказательство работающего импорта / Data schema and example; not evidence of a working import |
| [Паспорт файла / Asset sidecar](asset.example.json) | Соседний `<filename>.<ext>.asset.json` для ресурса / Adjacent asset provenance and rights record |

Пути и границы REF/OBJ/ART, правила хранения и продуктовые особенности: [ресурсы и продукты](../studio/guides/assets-and-products.md). / Destinations, REF/OBJ/ART boundaries, storage and product-specific guidance: [assets and products](../studio/guides/assets-and-products.md).

## Решения и передача / Decisions and handoff

| Форма / Form | Назначение / Purpose |
| --- | --- |
| [Адаптация / Adaptation](adaptation.md) | Манифест продукта и его связь с каноном / Product manifest and canon baseline |
| [Решение / Decision](decision.md) | Варианты, последствия, основание выбора / Options, consequences, rationale |
| [Подтверждение / Approval](approval.example.json) | Фактические решения обоих авторов и точные байты / Actual coauthor decisions and exact bytes |
| [Архивная заметка / Archive note](archive-note.md) | Причина и преемник / Reason and successor |
| [Миграция / Migration](migration.example.json) | Контролируемое изменение зарегистрированной структуры / Reviewed change to registered structure |
| [Передача / Handoff](handoff.md) | Что готово, где продолжить, что проверено / Deliverables, continuation point, actual checks |

Примеры JSON не содержат действительных одобрений или разрешений. Заполняйте сведения только по реальным основаниям; ИИ не подписывает за автора. / Example JSON files contain no actual approvals or permissions. Record only evidenced information; AI does not sign on an author's behalf.

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../README.md) › [templates](README.md)

[По задаче / By task](../studio/NAVIGATION.md) · [Карта / Map](../studio/REPOSITORY_MAP.md) · [Материалы / Content](../studio/CONTENT_CATALOG.md) · [Шаблоны / Templates](README.md)

### Файлы рядом / Files here

- [3D Production Specification / Технический формуляр 3D-ресурса](3d-production-spec.md) — `3d-production-spec.md`.
- [Шаблоны: контекст для помощника / Template assistant context](AGENTS.md) — `AGENTS.md`.
- [Название материала](adaptation.md) — `adaptation.md`.
- [approval.example.json](approval.example.json) — `approval.example.json`.
- [Название материала](archive-note.md) — `archive-note.md`.
- [Название материала](art-brief.md) — `art-brief.md`.
- [asset.example.json](asset.example.json) — `asset.example.json`.
- [Название материала](character.md) — `character.md`.
- [Название материала](decision.md) — `decision.md`.
- [engine-asset.example.json](engine-asset.example.json) — `engine-asset.example.json`.
- [engine-asset.schema.json](engine-asset.schema.json) — `engine-asset.schema.json`.
- [Engine Implementation Profile / Профиль реализации для движка](engine-implementation-profile.md) — `engine-implementation-profile.md`.
- [Название материала](episode.md) — `episode.md`.
- [Название материала](faction.md) — `faction.md`.
- [Название материала](font.md) — `font.md`.
- [Художественный ресурс / Game Art Asset Card](game-art-asset.md) — `game-art-asset.md`.
- [Название материала](handoff.md) — `handoff.md`.
- [Historical Object Reference / Исторический предмет](historical-object-reference.md) — `historical-object-reference.md`.
- [Шаблон фрагмента идеи / Idea Fragment Template](idea-fragment.md) — `idea-fragment.md`.
- [Название материала](location.md) — `location.md`.
- [migration.example.json](migration.example.json) — `migration.example.json`.
- [Название материала](palette.md) — `palette.md`.
- [Physical Behavior Specification / Формуляр физических свойств объекта](physical-behavior-spec.md) — `physical-behavior-spec.md`.
- [Название материала](research.md) — `research.md`.
- [Название материала](scene.md) — `scene.md`.
- [Название материала](story-arc.md) — `story-arc.md`.
- [Название материала](technology.md) — `technology.md`.
- [Название материала](world-entry.md) — `world-entry.md`.
- [Универсальная карточка объекта / Universal Object Card](world-object.md) — `world-object.md`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context templates`

<!-- NAVIGATION:END -->
