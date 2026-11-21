# Задания для ИИ / AI task briefs

[Все инструкции / All guides](README.md) · [AGENTS.md](../../AGENTS.md) · [Работа с ИИ / AI collaboration](../AI_COLLABORATION.md) · [Навигация / Navigation](../NAVIGATION.md)

## Русский

### Как дать помощнику достаточный контекст

Передайте ссылку на репозиторий, цель, человека-ответственного, разрешённые пути и ожидаемый результат. Если работа продолжает прежнюю сессию, добавьте ветку/commit, точные файлы, выполненные проверки и открытые вопросы. Новый помощник проверяет эти сведения по файлам, прежде чем записывать изменения.

Обязательное начало задаёт корневой [AGENTS.md](../../AGENTS.md): [README](../../README.md), [WORKFLOW](../WORKFLOW.md), [REPOSITORY_RULES](../REPOSITORY_RULES.md), [CANON_POLICY](../CANON_POLICY.md), [structure.json](../structure.json) и README целевой области/стадии. Прочитайте также применимые локальные AGENTS.md по пути к файлу. Для нового или изменяемого текста учитывайте [языковую политику](../LANGUAGE_POLICY.md).

После этого добавляйте предметный контекст по задаче, без загрузки всей библии мира по умолчанию:

| Задача | Дополнительный контекст |
| --- | --- |
| Сюжет, герой, сцена | [Руководство автора](writing.md), связанные карточки CHAR/ARC/EP, соответствующий канон, открытые GAP/DIV и исходные статусы |
| Правило мира или исследование | README нужной области, существующие версии положения, источники и пределы достоверности |
| Предмет или визуальный ресурс | [Маршрут ресурсов](assets-and-products.md), нужные OBJ/REF/ART, правила прав и применимые стандарты этапа |
| Продукт или игровой код | README продукта, его baseline мира, техническое задание, применимые производственные требования и тесты |
| Организация репозитория | [Рабочий процесс](working-together.md), текущие правила, структура, точный scope и последствия изменения |

Навигатор помогает подобрать файлы:

```sh
python tools/navigate.py where "сюжет"
python tools/navigate.py find ARC025
python tools/navigate.py context narrative/episodes/drafts
```

Список контекста — указатель на материалы; он не является подтверждением того, что помощник их прочитал или что найденный черновик утверждён. Полные команды описаны в [tools](../../tools/README.md).

### Универсальное задание: скопируйте и заполните

```text
Мы работаем над проектом 48/24:
https://github.com/alexanderyashin/48-24

Человек-ответственный: [Саша / Иван / другой участник].
Задача: [один конкретный результат].
Разрешённые пути: [папки и файлы].
Исходная ветка/commit: [проверить актуальное состояние].
Рабочая ветка: [work/ivan/... или work/sasha/...].
Материалы и связанные ID: [ссылки, ID, исходный текст].
Критерий готовности: [что должно получиться и как проверить].

Сначала прочитай корневой AGENTS.md, обязательные документы из него,
применимые локальные инструкции и README целевых папок.
Проверь текущие файлы и работу других участников на тех же путях.
Для поиска используй studio/NAVIGATION.md, каталог материалов
и tools/navigate.py, если доступна локальная копия.

Выполни задачу в указанной области. Сохраняй авторский смысл, источники,
существующие ID, обе языковые версии и нерешённые вопросы.
Новые творческие варианты помечай как предложения/черновики.
Не приписывай авторам согласие; не превращай merge или перевод в канон.
Не переноси папки, не меняй лицензии, защиту или общие правила
в качестве попутной уборки. Не перезаписывай чужую работу.
Неизвестные модель, seed, исторические и технические параметры
отмечай как неизвестные. Не публикуй приватный контекст.

Перед передачей просмотри diff, обнови навигацию при необходимости
и выполни применимые проверки. Если доступ к GitHub или запуск команд
недоступен, сообщи это точно; подготовленные локальные файлы не называй
опубликованными. Не отправляй сообщения людям без отдельного поручения.

В конце укажи: изменённые файлы и ссылки, что сделано, фактические
проверки, что осталось открытым, commit/PR при наличии и следующий шаг.
```

### Короткие дополнения для частых задач

**Сюжет:** «Сохрани мой исходный текст. Определи, это самостоятельная история, длинная арка или сцена. Предложи место по руководству `studio/guides/writing.md`; если тип пока неясен, оформи входящую идею. Проверь связанные карточки и зависимости от GAP/DIV. Не добавляй новые факты мира как согласованные. Оформи рабочую версию на русском и английском».

**Арт или объект:** «Отдели исторические REF, объект мира OBJ и реализацию ART. Укажи текущую задачу и применимый уровень готовности. Запиши открытые характеристики и источники. Для бинарных файлов проверь права и подготовь фактический паспорт. Если сейчас нужен только эскиз, не заявляй готовность к моделированию или импорту в движок».

**Продолжение чужой сессии:** «Проверь указанную ветку и commit, прочитай handoff и фактический diff. Назови оставшийся конкретный результат. Сохрани изменения других участников. Если сведения handoff расходятся с репозиторием, используй проверенное состояние и сообщи о расхождении».

### Что проверить в ответе помощника

Попросите точные ссылки на файлы и наблюдаемый результат публикации. Проверьте, что черновики остались черновиками, источники не исчезли, перевод сохранил смысл, а перечень проверок соответствует действительно выполненным командам. Для параллельной работы выдавайте помощникам разные задачи и рабочие каталоги; общий владелец задачи всегда человек.

## English

### Give the assistant sufficient context

Provide the repository URL, goal, responsible human, permitted paths and expected outcome. For continuation, include branch/commit, exact files, checks and open questions. A new assistant verifies this handoff against actual files before writing.

The root [AGENTS.md](../../AGENTS.md) defines mandatory reading: [README](../../README.md), [WORKFLOW](../WORKFLOW.md), [REPOSITORY_RULES](../REPOSITORY_RULES.md), [CANON_POLICY](../CANON_POLICY.md), [structure.json](../structure.json) and the target area/stage READMEs. Also read applicable local AGENTS.md files along the path. Apply the [language policy](../LANGUAGE_POLICY.md) to new and edited text.

Then add task-specific context instead of loading the whole world bible by default:

| Task | Additional context |
| --- | --- |
| Story, character or scene | [Writing guide](writing.md), related CHAR/ARC/EP records, relevant canon, open GAP/DIV and source statuses |
| World rule or research | Target README, existing versions, sources and limits of certainty |
| Object or visual asset | [Asset guide](assets-and-products.md), relevant OBJ/REF/ART, rights requirements and stage-specific standards |
| Product or game code | Product README, world baseline, technical brief, applicable production requirements and tests |
| Repository organization | [Collaboration guide](working-together.md), current rules, structure, exact scope and consequences |

The navigator helps locate context:

```sh
python tools/navigate.py where "story"
python tools/navigate.py find ARC025
python tools/navigate.py context narrative/episodes/drafts
```

A context list points to records. It does not prove that the assistant read them or that a found draft is approved. See [tools](../../tools/README.md) for full command instructions.

### General brief: copy and fill in

```text
We are working on 48/24:
https://github.com/alexanderyashin/48-24

Responsible human: [Sasha / Ivan / another contributor].
Task: [one concrete outcome].
Permitted paths: [folders and files].
Starting branch/commit: [verify current state].
Working branch: [work/ivan/... or work/sasha/...].
Inputs and related IDs: [links, IDs, original text].
Completion criterion: [deliverable and how to verify it].

First read the root AGENTS.md, its mandatory documents, applicable
local instructions and destination READMEs. Check current files and
overlapping work. Use studio/NAVIGATION.md, the content catalog and
tools/navigate.py when a local checkout is available.

Complete the task within the stated scope. Preserve authorial meaning,
sources, stable IDs, both language versions and open questions.
Mark new creative alternatives as proposals/drafts. Never invent human
approval or treat merging or translation as canon acceptance.
Do not move folders, rewrite licenses, weaken checks or change shared
rules as incidental cleanup. Preserve others' work.
Mark unknown models, seeds, historical or technical values as unknown.
Do not publish private context.

Before handoff, review the diff, refresh navigation when needed and run
applicable checks. If GitHub access or command execution is unavailable,
state that precisely. Do not report local files as published.
Do not message people without a separate instruction.

Finish with changed files and links, completed work, actual checks,
open questions, commit/PR when available and the next concrete step.
```

### Additions for common tasks

**Writing:** “Preserve my original text. Identify whether this is a standalone story, a long arc or a scene. Choose a destination using `studio/guides/writing.md`; use an inbox record if classification is unclear. Check related records and GAP/DIV dependencies. Do not present new world facts as accepted. Prepare Russian and English working versions.”

**Art or objects:** “Separate historical REF, fictional OBJ and implementation ART. Identify the current task and applicable readiness stage. Record unknown properties and provenance. For binary files, verify rights and prepare actual sidecar metadata. If only a sketch is requested, do not claim modeling or engine-import readiness.”

**Continuing another session:** “Verify the stated branch and commit, read the handoff and actual diff, and identify the remaining concrete result. Preserve other contributors' work. If the handoff conflicts with the repository, use the verified state and explain the discrepancy.”

### Checking an assistant's handoff

Ask for exact file links and observed publication results. Check that drafts remain drafts, sources survive, translations preserve meaning, and reported checks were actually executed. Give parallel assistants separate tasks and working directories. A human remains responsible for the task.
