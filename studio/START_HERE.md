# Начать работу / Start here

[Главная / Home](../README.md) · [Выбрать задачу / Choose a task](NAVIGATION.md) · [Карта папок / Folder map](REPOSITORY_MAP.md) · [Каталог материалов / Content catalog](CONTENT_CATALOG.md)

## Русский

**Если вы пришли с новой идеей, начните с [inbox](inbox/README.md). Если уже знаете, что создаёте, выберите маршрут ниже.** Структура помогает двум авторам работать независимо; заполнять все папки до первой истории не нужно.

### Куда идти прямо сейчас

| Ваша задача | Первый шаг |
| --- | --- |
| Быстро сохранить мысль или смешанный фрагмент | [Входящие идеи](inbox/README.md) и [шаблон](../templates/idea-fragment.md) |
| Написать сюжет, персонажа, сцену или диалог | [Инструкция автора](guides/writing.md) |
| Развить устройство мира, историю, экономику или технологию | [Маршрутизатор задач](NAVIGATION.md) → нужная область `world`/`research` |
| Создать арт, палитру, шрифт, музыку или 3D-ресурс | [Ресурсы и продукты](guides/assets-and-products.md) |
| Работать вместе и передать результат | [Совместная работа](guides/working-together.md) |
| Дать задачу нейросети | [Готовые задания для ИИ](guides/ai-task-briefs.md) и [AGENTS.md](../AGENTS.md) |
| Найти существующий материал | [Каталог](CONTENT_CATALOG.md), [карта](REPOSITORY_MAP.md), [поиск и навигатор](../tools/README.md) |

Для Вани: самостоятельная история обычно начинается в [narrative/episodes/drafts](../narrative/episodes/drafts/README.md); длинная линия — в [narrative/story-arcs/drafts](../narrative/story-arcs/drafts/README.md). Инструкция выше помогает выбрать между ними без перестройки папок.

### Первая рабочая задача

1. Найдите связанные материалы и прочитайте README целевой папки. Проверьте, не занят ли тот же файл другой задачей.
2. Назовите результат, ответственного человека и разрешённые пути. Используйте Issue/PR либо [реестр задач](registers/work-register.csv) для работы без Issue.
3. Создайте свежую ветку по [рабочему процессу](WORKFLOW.md), возьмите [шаблон](../templates/README.md), заполните одну небольшую карточку. Новая идея не обязана сразу решать все вопросы мира.
4. Сохраните источники, авторство, ID и отметку об использовании ИИ. Русская и английская версии нужны по [языковой политике](LANGUAGE_POLICY.md).
5. Проверьте diff, выполните доступные проверки и передайте результат через PR с открытыми вопросами и следующим шагом. Подробная последовательность — в [совместной работе](guides/working-together.md).

Самая простая проверка из корня локальной копии — `python tools/validate_repo.py`. Команды навигации и её обновления находятся в [tools](../tools/README.md). Можно работать через GitHub, Desktop или редактор; если локальные команды не выполнялись, укажите это и посмотрите фактический CI у PR.

### Три различия, которые помогают не запутаться

- **Папка и статус.** `drafts` — разработка и рассмотрение; `canon` — точные версии с реальным решением обоих авторов; `archive` — прежние версии с причиной. Входящие `captured/triaged/routed/discarded` описывают обработку идеи, а не её каноничность.
- **Авторство и ответственность.** `owner` — человек, который ведёт задачу; происхождение идеи, вклад и имущественные права учитываются отдельно. Посмотрите [роли](RESPONSIBILITIES.md) и [команду](team.json).
- **Публикация и утверждение.** Репозиторий публичен, включая черновики и архив. Попадание файла в `main` не делает его каноном и не меняет условия [лицензии](../LICENSE).

### Команда и текущие организационные вопросы

В [team.json](team.json) зафиксированы Саша (`alexanderyashin`) и Иван: внутренний ID `ivan-konyushkov`, GitHub `ivankoniushkov`. Доступ Ивана на запись подтверждён в записи команды от 2026-11-19; повторное приглашение не является стартовой задачей. Если доступ перестал работать, проверяйте фактическое состояние GitHub.

Состояние настройки репозитория и защиты `main` смотрите в [rollout](rollout/STATUS.md): файл конфигурации сам по себе не доказывает, что настройка включена. Следующие творческие решения — совместная проверка импорта SPOT, первые небольшие решения канона и выбор пробной истории/выпуска. Места для игры, видео, настолки и книги уже есть; это не объявление одновременного запуска всех производств.

## English

**Start in the [inbox](inbox/README.md) for a new unclassified idea. If you know what you are creating, choose a route below.** The structure supports two authors working independently; you do not need to fill every folder before writing a story.

### Where to go now

| Task | First step |
| --- | --- |
| Capture a thought or mixed fragment | [Creative inbox](inbox/README.md) and [template](../templates/idea-fragment.md) |
| Write a plot, character, scene or dialogue | [Writing guide](guides/writing.md) |
| Develop world structure, history, economics or technology | [Task navigation](NAVIGATION.md) → relevant `world`/`research` area |
| Create art, a palette, typography, music or a 3D asset | [Assets and products](guides/assets-and-products.md) |
| Collaborate and hand over work | [Working together](guides/working-together.md) |
| Delegate to an AI assistant | [Ready task briefs](guides/ai-task-briefs.md) and [AGENTS.md](../AGENTS.md) |
| Find existing material | [Catalog](CONTENT_CATALOG.md), [map](REPOSITORY_MAP.md), [search and navigator](../tools/README.md) |

For Ivan: a standalone story usually starts in [narrative/episodes/drafts](../narrative/episodes/drafts/README.md); a longer arc in [narrative/story-arcs/drafts](../narrative/story-arcs/drafts/README.md). The writing guide helps choose without restructuring folders.

### Your first task

1. Find related material and read the destination README. Check for another task editing the same file.
2. State the result, responsible human and permitted paths. Use an Issue/PR, or the [work register](registers/work-register.csv) for work without an Issue.
3. Create a fresh branch under the [workflow](WORKFLOW.md), choose a [template](../templates/README.md), and fill one small record. A new idea need not resolve every world question.
4. Preserve sources, authorship, IDs and AI provenance. Provide Russian and English under the [language policy](LANGUAGE_POLICY.md).
5. Inspect the diff, perform available checks and hand over through a PR with open questions and the next step. See [working together](guides/working-together.md) for the full sequence.

The simplest local check is `python tools/validate_repo.py` from the repository root. See [tools](../tools/README.md) for navigation and refresh commands. GitHub, Desktop or an editor can be used. If local commands were not run, state that and inspect the PR's actual CI results.

### Three useful distinctions

- **Folder and status.** `drafts` holds development/review; `canon` holds exact versions with actual decisions by both authors; `archive` holds earlier versions with reasons. Inbox states `captured/triaged/routed/discarded` describe intake processing, not canon.
- **Authorship and responsibility.** `owner` is the person carrying the work; origin, contribution and property rights are recorded separately. See [roles](RESPONSIBILITIES.md) and [team](team.json).
- **Publication and approval.** The repository is public, including drafts and archive. Being in `main` does not make a file canon or change its [license](../LICENSE).

### Team and remaining organizational questions

[team.json](team.json) records Sasha (`alexanderyashin`) and Ivan: internal ID `ivan-konyushkov`, GitHub `ivankoniushkov`. The team record confirms Ivan's write access as of 2026-11-19; another invitation is not a starting task. If access fails, inspect GitHub's actual state.

See [rollout](rollout/STATUS.md) for repository setup and `main` protection: a configuration file alone is not evidence that the setting is enabled. Upcoming creative decisions include jointly reviewing the SPOT import, accepting small portions of canon and choosing a trial story/installment. Game, video, tabletop and book workspaces exist without implying all productions have started.
