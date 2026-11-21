# Совместная работа / Working together

[Все инструкции / All guides](README.md) · [Рабочий процесс / Workflow](../WORKFLOW.md) · [Роли и вклад / Roles and contributions](../RESPONSIBILITIES.md)

## Русский

### Что означают основные слова

| Термин | Практический смысл |
| --- | --- |
| Репозиторий | Общая папка проекта с историей изменений |
| `main` | Общая основная ветка; в ней могут лежать материалы со статусом `draft` |
| Ветка задачи | Временная рабочая версия для одной связной задачи |
| Commit | Сохранённый набор изменений с пояснением |
| Pull request, PR | Предложение перенести изменения из ветки задачи в общую ветку; здесь видны файлы, обсуждение и проверки |
| Issue | Карточка задачи, вопроса или проблемы |
| Diff | Сравнение: что именно добавлено, изменено или удалено |
| CI | Автоматическая проверка в GitHub; она не заменяет содержательное рассмотрение |

### Перед началом

Откройте текущую версию репозитория и найдите материал через [навигацию](../NAVIGATION.md) или [каталог](../CONTENT_CATALOG.md). Посмотрите открытые задачи и PR: другой автор может работать над тем же файлом. Уточните одну цель, ответственного человека, целевые пути и критерий завершения.

Для задачи с Issue/PR описание и статус ведутся там. Для задачи без Issue используйте [рабочий реестр](../registers/work-register.csv); не ведите два конкурирующих журнала одной задачи. [Матрица ответственности](../RESPONSIBILITIES.md) помогает найти участника, но не запрещает соавтору развивать другие направления.

### Обычный маршрут в GitHub, Desktop или редакторе

1. Получите актуальный `main`. В локальной копии сначала проверьте несохранённые изменения; не стирайте их ради синхронизации.
2. Создайте ветку от актуальной базы: например, `work/ivan/first-story` или `work/sasha/station-design`. Имя описывает задачу, а не отдельную постоянную вселенную автора.
3. Найдите нужную папку, прочитайте её README и выберите [шаблон](../../templates/README.md). В веб-интерфейсе перед редактированием проверьте выбранную ветку. В Desktop/редакторе проверьте её в своём рабочем каталоге.
4. Внесите небольшой связный результат. При добавлении папки положите в неё README. Сохраняйте исходные ID, источники, авторскую атрибуцию и обе языковые версии.
5. Просмотрите diff целиком. Уберите случайно попавшие файлы из набора изменений, сохранив их локально, если они нужны для другой задачи. Не заменяйте чужие изменения своей старой копией.
6. Проверьте материал и создайте commit с понятным описанием. Опубликуйте свою ветку, затем откройте PR в `main`.
7. В PR укажите цель, изменённые пути, результат проверок, открытые вопросы и ожидаемый следующий шаг. Отдельно отметьте, предлагаете ли вы решение канона: обычный черновик не требует притворяться утверждённым.
8. Дождитесь применимых проверок и рассмотрения по [WORKFLOW](../WORKFLOW.md). После принятия синхронизируйте свою копию с фактическим `main` перед следующей задачей.

Прямая запись в `main` допускается только в рамках конкретно разрешённого действия; наличие поля `branch=main` в реестре не является постоянным разрешением обходить обычный процесс. Не используйте force push и не переписывайте опубликованную историю других участников.

### Проверка перед передачей

Из корня локальной копии:

```sh
python tools/navigate.py build
python tools/navigate.py check
python tools/validate_repo.py
```

`build` обновляет навигационные блоки и каталоги; проверьте их diff вместе с основной правкой. Для изменения инструментов также запустите `python -m unittest discover -s tools/tests -v`. Сравнение с базой PR выполняется по фактическому полному SHA через `python tools/validate_repo.py --base <SHA>`; замените `<SHA>` на реальное значение.

Если работаете только через сайт и команды недоступны, прямо укажите, что локальная проверка не запускалась, и проверьте результаты GitHub Actions у PR. Нельзя называть проверку пройденной только потому, что файлы сохранились. Подробности — в [инструкции инструментов](../../tools/README.md).

### Если работа пересекается

| Ситуация | Что сделать |
| --- | --- |
| Оба развивают одну тему разными способами | Сохранить отдельные предложения и связать общим вопросом; не выдавать одно за согласованный итог |
| Оба меняют один текст | Согласовать владельца текущей правки или разделить задачу по самостоятельным карточкам |
| Git сообщает о конфликте | Прочитать обе версии и понять изменения; сохранить смысл и атрибуцию, затем повторить проверку |
| Один ИИ работает по устаревшему снимку | Остановить запись в затронутые файлы, прочитать актуальные изменения и перенести только свою правку |
| Нужно редактировать бинарный мастер | Назначить одного текущего редактора; альтернативный вариант хранить отдельно с собственным ID |
| Материал отвергнут | Сохранить причину и связь с заменой по [правилам архива](../CANON_POLICY.md) |

Для двух ИИ используйте отдельные задачи, ветки и рабочие каталоги. Передавайте точные пути и явно ограничивайте область изменений. Не поручайте двум помощникам одновременно обновлять один исходный файл без распределения частей работы.

### Как закончить рабочую сессию

Используйте [шаблон передачи](../../templates/handoff.md) в описании PR или журнале задачи. Достаточно указать: задачу и владельца; ветку и исходный commit; изменённые файлы; выполненные проверки с фактическим результатом; открытые решения; следующий конкретный шаг. Дополнительный самостоятельный файл нужен, только если он полезен для продолжения.

[Реестр вкладов](../registers/contribution-register.csv) фиксирует, кто и как участвовал в конкретной версии; автор commit не обязательно является автором идеи. [Реестр источников](../registers/source-register.csv) хранит происхождение материалов. [Подтверждения](../approvals/README.md) содержат реальные решения. [Каталог](../CONTENT_CATALOG.md) и [карта](../REPOSITORY_MAP.md) служат поиску и не подменяют эти записи.

## English

### Basic terms

| Term | Practical meaning |
| --- | --- |
| Repository | The shared project files and their change history |
| `main` | The shared primary branch; it may contain material marked `draft` |
| Task branch | A temporary working version for one coherent task |
| Commit | A saved set of changes with an explanation |
| Pull request, PR | A proposal to integrate a task branch; it shows files, discussion and checks |
| Issue | A task, question or problem record |
| Diff | The exact additions, modifications and deletions |
| CI | Automated GitHub checks; they do not replace editorial review |

### Before starting

Open the current repository and locate material through [navigation](../NAVIGATION.md) or the [catalog](../CONTENT_CATALOG.md). Check open tasks and PRs for overlapping work. Define one goal, the responsible human, target paths and completion criterion.

Keep a task's description and status in its Issue/PR. Use the [work register](../registers/work-register.csv) for work without an Issue, avoiding duplicate competing status logs. The [responsibility matrix](../RESPONSIBILITIES.md) helps identify participants without excluding either coauthor from other domains.

### Normal workflow in GitHub, Desktop or an editor

1. Obtain current `main`. Check unsaved local work before synchronizing; preserve it.
2. Create a task branch from that base, such as `work/ivan/first-story` or `work/sasha/station-design`. Branches represent tasks, not permanent separate fictional universes.
3. Read the destination README and choose a [template](../../templates/README.md). Check the selected branch before editing on the website or in your local working directory.
4. Make a small coherent change. Give each new folder a README. Preserve stable IDs, sources, attribution and both language versions.
5. Inspect the complete diff. Exclude accidentally included files while preserving useful unrelated work locally. Do not overwrite others' work with an older copy.
6. Check the material and commit with a clear explanation. Publish your branch and open a PR into `main`.
7. State purpose, changed paths, actual checks, open questions and next step. Explicitly identify any proposed canon decision; ordinary drafts do not need to pretend to be approved.
8. Complete applicable checks and review under [WORKFLOW](../WORKFLOW.md). After integration, synchronize with actual `main` before starting again.

Writing directly to `main` needs authorization for that specific action. A `branch=main` field does not provide standing permission to bypass the normal workflow. Do not force-push or rewrite others' published history.

### Check before handing over

From the local repository root:

```sh
python tools/navigate.py build
python tools/navigate.py check
python tools/validate_repo.py
```

`build` refreshes navigation blocks and catalogs; inspect its diff along with the main change. For tooling changes, also run `python -m unittest discover -s tools/tests -v`. Compare with the actual full PR base SHA using `python tools/validate_repo.py --base <SHA>`, replacing `<SHA>` with that value.

If working only on the website, state that local checks were not run and inspect the PR's GitHub Actions results. Saving files alone is not evidence of passing validation. See the [tools instructions](../../tools/README.md).

### Overlapping work

| Situation | Action |
| --- | --- |
| Two approaches to one topic | Retain separate proposals and link the shared question; do not invent consensus |
| Two edits to one text | Agree on the current editor or divide work into independent records |
| Git reports a conflict | Read both versions, preserve meaning and attribution, then rerun checks |
| An AI is using an old snapshot | Pause writes to affected paths, read current changes and reapply only the intended edit |
| A binary master needs editing | Assign one current editor; give independent alternatives their own IDs |
| Material is rejected | Preserve the reason and replacement link under the [archive rules](../CANON_POLICY.md) |

Use separate tasks, branches and working directories for parallel AI assistants. Give them exact paths and scope. Do not let two assistants overwrite one source file without assigning distinct parts.

### Ending a session

Use the [handoff template](../../templates/handoff.md) in the PR or task log: goal and owner, branch and starting commit, changed files, actual check results, open decisions and next concrete action. Create a separate handoff file only when it helps continuation.

The [contribution register](../registers/contribution-register.csv) records each person's role in a version; a committer is not automatically the idea's author. The [source register](../registers/source-register.csv) records provenance. [Approval records](../approvals/README.md) hold actual decisions. The [catalog](../CONTENT_CATALOG.md) and [map](../REPOSITORY_MAP.md) support discovery without replacing these records.
