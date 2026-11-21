# Реестры проекта / Project registers

Реестры сохраняют определённые факты и связи. Перед добавлением строки выберите её назначение по таблице; одинаковую сущность не нужно заново описывать во всех CSV. / Each register tracks a defined kind of fact or relationship. Choose the appropriate register below; do not duplicate a complete record in every CSV.

| Файл / File | Что здесь / What it tracks | Когда обновлять / When to update |
| --- | --- | --- |
| [content-index.csv](content-index.csv) | Текущее рабочее место импортированной темы и источник / Current working record of an imported topic and its source | Новая выделенная карточка, перенос, изменение статуса / New extracted record, relocation, status change |
| [source-register.csv](source-register.csv) | Источники и пределы применения / Sources and limitations | Новый источник или проверка его пригодности / A new source or source assessment |
| [decisions.csv](decisions.csv) | Исходные CAN с историческим авторским статусом / Source CAN statements and historical authorial status | Уточнение записи источника с основанием / Evidenced correction of a source record |
| [open-questions.csv](open-questions.csv) | Открытые творческие GAP/DIV и критерии закрытия / Open creative GAP/DIV questions and closure criteria | Новый вопрос или доказанное изменение состояния / New question or evidenced state change |
| [asset-register.csv](asset-register.csv) | Ресурсы, версии, мастера, права, хеши / Assets, versions, masters, rights, hashes | Новый ресурс или изменённая версия/местоположение / New asset or changed version/location |
| [contribution-register.csv](contribution-register.csv) | Вклад человека по объекту и версии / Human contribution by object and version | Существенный проверяемый вклад / Substantive attributable contribution |
| [work-register.csv](work-register.csv) | Задачи без GitHub Issue / Work without a GitHub Issue | Начало, передача или завершение такой задачи / Start, handoff or completion of such a task |
| [release-register.csv](release-register.csv) | Согласованные и выпущенные версии продуктов / Agreed and published product versions | Фактический переход выпуска с основанием / Evidenced release transition |

## Русский

[CONTENT_CATALOG](../CONTENT_CATALOG.md) автоматически показывает карточки, найденные в файлах; его обновляет `python tools/navigate.py build`. Он не заменяет редакционный `content-index.csv`, реестры источников, вкладов и решений. Совпадение ID в историческом источнике и в рабочей карточке не является новым авторским решением.

Новые реальные подтверждения находятся в [approvals](../approvals/README.md), а не выводятся из слова «КОНСЕНСУС» в старом источнике. Права сторонних материалов учитываются в [юридическом реестре](../../legal/THIRD_PARTY_ASSETS.csv). Исторические объектные референсы имеют профильный [каталог коллекций](../../research/visual-references/drafts/historical-collections/catalog.csv).

Issue/PR остаётся оперативным источником задачи, если он существует. [Журнал управления](../../production/planning/drafts/project-management/README.md) связывает результаты и точки продолжения; он не должен дублировать все строки первичных таблиц. Состояние `branch=main` в рабочем реестре описывает место работы, а не даёт отдельное разрешение обходить процесс.

Пустые таблицы содержат только заголовки. Не заполняйте их фиктивными ресурсами, сроками, вкладом или одобрениями. Сохраняйте CSV-заголовки, устойчивые ID и минимальный diff. Ответственный `owner`, автор идеи, проверяющий и правообладатель — разные роли. Подробности: [WORKFLOW](../WORKFLOW.md), [RESPONSIBILITIES](../RESPONSIBILITIES.md), [работа с импортом](../source-import-guide.md).

## English

[CONTENT_CATALOG](../CONTENT_CATALOG.md) automatically lists records found in files and is refreshed by `python tools/navigate.py build`. It does not replace the editorial `content-index.csv` or the source, contribution and decision registers. An ID appearing in both a historical source and its working record is not a new authorial decision.

Actual new approvals belong in [approvals](../approvals/README.md); they cannot be inferred from source consensus labels. Third-party rights are recorded in the [legal register](../../legal/THIRD_PARTY_ASSETS.csv). Historical object references also have a subject-specific [collection catalogue](../../research/visual-references/drafts/historical-collections/catalog.csv).

An existing Issue/PR remains the operational task source. The [management log](../../production/planning/drafts/project-management/README.md) links results and continuation points without duplicating every primary table row. `branch=main` records a work location; it does not independently authorise bypassing the workflow.

Empty registers contain headers only. Do not populate them with invented assets, dates, contributions or approvals. Preserve CSV headers, stable IDs and focused diffs. Task owner, originator, reviewer and rights holder are distinct roles. See [WORKFLOW](../WORKFLOW.md), [RESPONSIBILITIES](../RESPONSIBILITIES.md) and the [source import guide](../source-import-guide.md).

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../../README.md) › [studio](../README.md) › [registers](README.md)

[По задаче / By task](../NAVIGATION.md) · [Карта / Map](../REPOSITORY_MAP.md) · [Материалы / Content](../CONTENT_CATALOG.md) · [Шаблоны / Templates](../../templates/README.md)

### Файлы рядом / Files here

- [asset-register.csv](asset-register.csv) — `asset-register.csv`.
- [content-index.csv](content-index.csv) — `content-index.csv`.
- [contribution-register.csv](contribution-register.csv) — `contribution-register.csv`.
- [decisions.csv](decisions.csv) — `decisions.csv`.
- [open-questions.csv](open-questions.csv) — `open-questions.csv`.
- [release-register.csv](release-register.csv) — `release-register.csv`.
- [source-register.csv](source-register.csv) — `source-register.csv`.
- [work-register.csv](work-register.csv) — `work-register.csv`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context studio/registers`

<!-- NAVIGATION:END -->
