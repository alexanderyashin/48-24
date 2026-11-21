# Тексты и сюжеты / Writing and stories

[Все инструкции / All guides](README.md) · [Навигация / Navigation](../NAVIGATION.md) · [Сюжетный раздел / Narrative](../../narrative/README.md)

## Русский

### 1. Выберите масштаб материала

Для начала достаточно одной идеи или одной сцены. Структура помогает сохранить и развить материал; заполнять все направления проекта сразу не требуется.

| Что вы принесли | Куда положить | С чего начать |
| --- | --- | --- |
| Фрагмент, свободная заметка, смешанная идея, пока без классификации | [studio/inbox](../inbox/README.md) | [Карточка идеи](../../templates/idea-fragment.md) |
| Логлайн, общее обещание истории, тема, синопсис всего произведения | [narrative/premise/drafts](../../narrative/premise/drafts/README.md) | Существующие [премиса](../../narrative/premise/drafts/premise-v0-1.md) и [логлайны](../../narrative/premise/drafts/logline-options-v0-1.md), общие поля метаданных |
| Длинная линия через несколько событий или выпусков | [narrative/story-arcs/drafts](../../narrative/story-arcs/drafts/README.md) | [Сюжетная арка](../../templates/story-arc.md) |
| Самостоятельный сюжет, рассказ, глава, миссия или приключение | [narrative/episodes/drafts](../../narrative/episodes/drafts/README.md) | [Эпизод](../../templates/episode.md) |
| Конкретный эпизод действия: место, участники, выбор, последствие | [narrative/scenes/drafts](../../narrative/scenes/drafts/README.md) | [Сцена](../../templates/scene.md) |
| Биография, мотивация, отношения, развитие героя | [narrative/characters/drafts](../../narrative/characters/drafts/README.md) | [Персонаж](../../templates/character.md) |
| Реплики, монолог, словарь или особенности речи | [narrative/dialogue/drafts](../../narrative/dialogue/drafts/README.md) | Общие поля метаданных, ссылки на персонажа и сцену |
| Правило мира, институт, технология или география | Нужная область [world](../../world/README.md), затем `drafts` | [Выбор направления](../NAVIGATION.md) и [шаблоны](../../templates/README.md) |

**Для Вани:** если у тебя уже есть самостоятельный сюжет с завязкой, развитием и финалом, удобная стартовая точка — `narrative/episodes/drafts/`. Если это протяжённая линия через несколько историй — `narrative/story-arcs/drafts/`. Если мысль ещё складывается, её можно спокойно сохранить в `studio/inbox/` и разобрать позднее.

Не нужно копировать один текст сразу в книгу, игру и YouTube. Общая история живёт в `narrative`; конкретная адаптация в `products` ссылается на неё и описывает особенности своего формата.

### 2. Проверьте, что уже существует

1. Откройте [каталог материалов](../CONTENT_CATALOG.md) и README нужной папки. Ищите название, тему и связанный ID, включая варианты в `drafts`, принятые версии в `canon` и прежние версии в `archive`.
2. При продолжении существующего материала сохраните его ID. Самостоятельное предложение получает новый свободный ID; не выдавайте заново уже использованные номера. Соглашения — в [именах и метаданных](../NAMING_AND_METADATA.md).
3. Уточните исходный статус мысли по [импортированному корпусу](../source-import-guide.md), [реестру положений](../registers/decisions.csv) и [открытым вопросам](../registers/open-questions.csv). Предложение одного автора, совместная разработка и утверждённое решение — разные состояния.
4. Полный [SPOT 0.1](../../world/world-bible/drafts/spot-0-1-import.md) используйте как источник. Развивайте отдельные рабочие карточки; исторический снимок не заменяйте новым пересказом.

### 3. Создайте рабочую карточку

Скопируйте выбранный шаблон в целевую папку. Если в шаблоне front matter показан внутри блока кода, перенесите сам блок `--- … ---` в начало карточки без внешних обратных кавычек. Замените все примеры и заглушки: уникальный `id`, `title`, `status`, `owner`, фактическую дату `updated`, `source`, `ai_assistance`; укажите версию. Для профильного черновика ставьте `status: draft`. Для входящей идеи используются отдельные состояния обработки, начиная с `captured`.

`owner` — ответственный человек, а не заявление о юридическом владении. Для Вани внутренний идентификатор в [команде](../team.json) — `ivan-konyushkov`; его GitHub-логин — `ivankoniushkov`. Если идея другого автора, сохраните его атрибуцию в тексте и записи о вкладе.

Новый текст оформляйте на русском и английском по [языковой политике](../LANGUAGE_POLICY.md). Для короткой новой карточки удобно иметь секции «Русский» и «English» в одном файле: так у одной записи остаются один ID и одна версия. Это практический способ оформления, а не изменение общей политики. Не исправляйте авторский смысл в процессе перевода; сомнения помечайте.

Для самостоятельного сюжета достаточно последовательно ответить:

1. Кто главный участник и чего он хочет?
2. Где и когда происходит история? Что уже известно, а что пока предложено?
3. Что нарушает исходное положение?
4. Какое препятствие вынуждает героя сделать выбор?
5. Какие последствия порождает этот выбор?
6. Каков поворот и чем заканчивается история?
7. Что меняется в герое или мире?
8. Какие персонажи, места, арки и открытые вопросы затронуты?

Для сцены важнее её конкретное изменение: что участники знают, хотят и могут сделать до сцены и после неё. Реплики могут оставаться внутри сцены; отдельная карточка диалога полезна, когда её действительно нужно редактировать или переиспользовать отдельно. Слова ненадёжного персонажа не становятся фактом мира.

### 4. Свяжите материал и передайте его

Ссылки на персонажей, места, источники и предыдущие записи делайте по ID и относительному пути. Если разбираете входящую идею, сохраните исходную карточку, поставьте `routed` и добавьте двусторонние ссылки. Если существенный творческий вклад нужно отразить отдельно, используйте [реестр вкладов](../registers/contribution-register.csv); [каталог](../CONTENT_CATALOG.md) помогает находить карточки, а [content-index.csv](../registers/content-index.csv) сохраняет происхождение рабочего импорта SPOT.

Проверьте diff и выполните `python tools/validate_repo.py` из корня репозитория. Передайте задачу через PR по [рабочему процессу](../WORKFLOW.md): что написано, точные файлы, проверка, нерешённые вопросы и следующий шаг. Для обновления навигации используйте команды из [инструкции инструментов](../../tools/README.md).

`drafts` содержит разработку и рассмотрение. `canon` содержит точные версии, принятые обоими авторами по [правилам канона](../CANON_POLICY.md). `archive` сохраняет отвергнутые или заменённые версии с причиной. Слияние PR само по себе не канонизирует историю.

## English

### 1. Choose the scale of the material

One idea or one scene is enough to begin. The structure helps preserve and develop material; you do not need to fill every project domain at once.

| Material | Destination | Starting point |
| --- | --- | --- |
| Unclassified fragment, loose note or mixed idea | [studio/inbox](../inbox/README.md) | [Idea record](../../templates/idea-fragment.md) |
| Logline, overall promise, theme or synopsis of the whole work | [narrative/premise/drafts](../../narrative/premise/drafts/README.md) | Existing [premise](../../narrative/premise/drafts/premise-v0-1.md), [loglines](../../narrative/premise/drafts/logline-options-v0-1.md) and common metadata |
| Long-running development across events or installments | [narrative/story-arcs/drafts](../../narrative/story-arcs/drafts/README.md) | [Story arc](../../templates/story-arc.md) |
| Standalone plot, short story, chapter, mission or adventure | [narrative/episodes/drafts](../../narrative/episodes/drafts/README.md) | [Episode](../../templates/episode.md) |
| A specific unit of action, choice and consequence | [narrative/scenes/drafts](../../narrative/scenes/drafts/README.md) | [Scene](../../templates/scene.md) |
| Biography, motivation, relationships or character development | [narrative/characters/drafts](../../narrative/characters/drafts/README.md) | [Character](../../templates/character.md) |
| Lines, monologues, vocabulary or speech patterns | [narrative/dialogue/drafts](../../narrative/dialogue/drafts/README.md) | Common metadata and character/scene links |
| A world rule, institution, technology or geography | Relevant [world](../../world/README.md) area, then `drafts` | [Task navigation](../NAVIGATION.md) and [templates](../../templates/README.md) |

**For Ivan:** a standalone plot with a beginning, development and ending fits `narrative/episodes/drafts/`. A longer line spanning several stories fits `narrative/story-arcs/drafts/`. An idea still taking shape can go into `studio/inbox/` for later triage.

Keep shared story material in `narrative`. Book, game and YouTube adaptations in `products` link to it and document their format-specific changes rather than copying the same text into several domains.

### 2. Check existing material

1. Open the [content catalog](../CONTENT_CATALOG.md) and target folder's README. Search titles, topics and IDs across drafts, canon and archive.
2. Preserve the ID when continuing an existing record. Give an independent proposal an unused ID. Follow [naming and metadata](../NAMING_AND_METADATA.md).
3. Check the [source import guide](../source-import-guide.md), [source propositions](../registers/decisions.csv) and [open questions](../registers/open-questions.csv). An author's proposal, joint development and an approved decision are distinct.
4. Use the full [SPOT 0.1 snapshot](../../world/world-bible/drafts/spot-0-1-import.md) as a source. Develop the separate working records; do not replace the historical snapshot with a new retelling.

### 3. Create the working record

Copy the appropriate template into the destination. If its front matter is shown inside a code fence, move the actual `--- … ---` block to the top of the record without the outer backticks. Replace every example and placeholder: unique `id`, `title`, `status`, `owner`, actual `updated` date, `source`, `ai_assistance`, and version. Use `status: draft` for domain drafts. Inbox records have separate processing states, beginning with `captured`.

`owner` is the responsible human, not a statement of legal ownership. Ivan's internal [team](../team.json) ID is `ivan-konyushkov`; his GitHub login is `ivankoniushkov`. Preserve another originator's credit in the text and contribution record.

Provide Russian and English versions under the [language policy](../LANGUAGE_POLICY.md). For a short new record, sections titled “Русский” and “English” in one file keep a single ID and version. This is a practical formatting option, not a change to the policy. Preserve meaning during translation and mark uncertainties.

A standalone plot can answer these questions in sequence:

1. Who is the central participant, and what do they want?
2. Where and when does it happen? Which details are established and which proposed?
3. What disturbs the starting situation?
4. Which obstacle forces a choice?
5. What consequences follow?
6. What is the turning point and ending?
7. What changes in the character or world?
8. Which characters, places, arcs and open questions are affected?

For a scene, identify the concrete change in what participants know, want and can do. Dialogue may stay within the scene; extract a separate dialogue record when it actually needs separate editing or reuse. An unreliable character's words do not establish world facts.

### 4. Link and hand over

Link characters, locations, sources and earlier records by ID and relative path. When routing an inbox idea, retain its original record, mark it `routed` and cross-link both directions. Record significant creative contributions in the [contribution register](../registers/contribution-register.csv) when needed. The [catalog](../CONTENT_CATALOG.md) locates records; [content-index.csv](../registers/content-index.csv) preserves the working SPOT import's provenance.

Review the diff and run `python tools/validate_repo.py` from the repository root. Hand over through a PR under the [workflow](../WORKFLOW.md), stating changed files, checks, open questions and the next step. Follow the [tools instructions](../../tools/README.md) to refresh navigation.

`drafts` contains development and review. `canon` contains exact versions accepted by both authors under the [canon policy](../CANON_POLICY.md). `archive` preserves rejected or superseded versions with reasons. A PR merge alone does not canonize a story.
