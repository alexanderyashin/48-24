# Совместный рабочий процесс

Оба автора могут независимо исследовать, писать и создавать визуальные варианты. Независимость обеспечивают отдельные задачи и ветки, небольшие файлы и явная передача результата. `main` содержит согласованную организацию работы, но может содержать черновой художественный материал.

## Одна задача и одна ветка

Откройте задачу с целью, владельцем, путями, ожидаемым результатом и зависимостями. Владелец — человек, даже если всю операцию выполняет ИИ. Укажите активную ветку в Issue/PR или в [реестре работы](registers/work-register.csv). Issue/PR — основной оперативный журнал; CSV нужен только для задач без Issue, чтобы не дублировать статусы вручную.

Используйте свежую ветку от main: `work/sasha/<task>`, `work/ivan/<task>`, `work/<contributor>/<task>`. Один PR решает одну связную задачу. Сначала публикуйте небольшой рабочий результат, затем расширяйте его. Ветки авторов не являются постоянными отдельными версиями мира.

Если два автора исследуют один вопрос, заведите два варианта с разными ID и общую карточку решения. Если меняют один файл, согласуйте владельца текущей правки; второму лучше внести отдельный вариант или комментарий. Git не умеет содержательно сливать изображения, шрифты и монтажные проекты: один бинарный исходник одновременно редактирует один человек.

## Ответственность и вклад

[Матрица ответственности](RESPONSIBILITIES.md) не закрепляет исключительные творческие территории. Автор идеи, исполнитель, редактор и утверждающий канон могут быть разными людьми. Существенные творческие вклады фиксируются по объекту и версии в [реестре вкладов](registers/contribution-register.csv), с указанием источника и типа участия. Коммит сам по себе не доказывает авторство идеи. Для прямой работы в `main` реестр задач допускает `branch=main`; это не отменяет требований проверки и согласования канона.

## Рассмотрение изменений

| Изменение | Что требуется |
| --- | --- |
| Новый черновик или уточнение исследования | Автор материала, проверка структуры, рассмотрение вторым автором по мере доступности |
| Исправление опечатки без изменения смысла | Краткий PR и автоматическая проверка |
| Принятие или изменение канона | Явное решение обоих авторов, точная версия и запись подтверждения |
| Новая структура, новые права, изменение правил или защит | Отдельная задача, последствия, план миграции и явное согласование обоих авторов |
| Публикация продукта | Манифест выпуска, права на все ресурсы и отдельное решение о выпуске |
| Вклад сообщества | Условия вклада, источник, проверка прав и содержательное рассмотрение |

GitHub-аккаунт Ивана — `ivankoniushkov`, его внутренний ID для записей решений — `ivan-konyushkov`; они указаны в [team.json](team.json). Доступ `write` подтверждён повторно 2026-11-21. Наличие доступа не означает выполненного review или согласия с конкретным изменением. Содержательное решение фиксируется по реальному авторскому подтверждению; приватные переписки в открытый репозиторий не копируются.

## Перед слиянием

1. Обновите ветку относительно main обычным merge/rebase своей неопубликованной работы; не переписывайте чужие ветки. Для общей опубликованной ветки используйте merge.
2. Проверьте diff: только заявленные пути, никакой случайной массовой перезаписи.
3. Выполните `python tools/validate_repo.py`; при изменении инструментов также `python -m unittest discover -s tools/tests -v`.
4. Проверьте статусы, источники, авторство, права, ссылки и отсутствие приватной информации.
5. Зафиксируйте незакрытые вопросы и следующий шаг. Зелёный CI подтверждает структуру, а не историческую истину и не согласие человека.

Слияние выполняется после применимых проверок и рассмотрения. Пустая первоначальная настройка репозитория выполнена по прямому поручению Саши и записана в [rollout](rollout/STATUS.md); это отдельное разовое действие.

## Передача задачи

Используйте [шаблон handoff](../templates/handoff.md): что сделано, ветка, точные файлы, что проверено, какие решения не приняты, где продолжить. Следующий ИИ начинает с фактических файлов и текущего состояния Git, а не с уверенного пересказа предыдущего ИИ.

## Навигация и связанные инструкции

Практические шаги для двух авторов и нескольких ИИ — в [руководстве совместной работы](guides/working-together.md). [Указатель веток](BRANCHES.md) помогает найти ещё не интегрированные материалы. Перед передачей добавленных или переименованных файлов пересоберите указатели командой `python tools/navigate.py build` и проверьте `python tools/navigate.py check`. Основной валидатор выполняется как прежде. Значение `branch=main` в реестре описывает факт и само по себе не даёт разрешения обходить рабочий процесс.

## English

Both authors can research, write and develop visual alternatives independently. Separate tasks and branches, small files and explicit handoffs make this possible. `main` contains the shared working organisation and may still contain creative drafts.

### One task, one branch

Create a task with a goal, human owner, paths, expected result and dependencies. Record the branch in the Issue/PR or the [work register](registers/work-register.csv). Issue/PR is the operational source; use CSV only for tasks without an Issue, avoiding manually duplicated statuses. If working without an Issue, the PR description can record the scope and owner.

Start from current main with `work/sasha/<task>`, `work/ivan/<task>` or `work/<contributor>/<task>`. One PR covers a coherent task. Publish a small useful draft before expanding it. Author branches are not permanent competing universes.

For independent proposals on one question, use distinct IDs and a shared decision record. If both authors need to edit one file, agree who currently owns the edit; the other can prepare a separate variant or comment. Images, fonts and editing projects cannot be meaningfully merged as text; one person edits a binary master at a time.

### Responsibility and contributions

The [responsibility matrix](RESPONSIBILITIES.md) does not allocate exclusive creative territories. Originator, implementer, editor and canon approver can be different people. Record substantive contributions by object/version in the [contribution register](registers/contribution-register.csv), with type and provenance. A commit alone does not prove authorship. `branch=main` can describe explicitly directed work in that location; it does not independently authorise bypassing the workflow or canon approval.

### Review

| Change | Requirement |
| --- | --- |
| New draft or research refinement | Human owner, structural validation, second-author review as available |
| Meaning-preserving typo correction | Short PR and automated validation |
| Adoption or change of canon | Explicit decisions by both authors, exact version and evidence |
| Structure, rights, governance or protection changes | Dedicated task, consequences, migration plan and explicit agreement of both authors |
| Product publication | Release manifest, asset rights and separate publication decision |
| Community contribution | Contribution terms, provenance, rights check and editorial review |

Ivan's GitHub login is `ivankoniushkov`; his internal approval ID is `ivan-konyushkov`, as recorded in [team.json](team.json). Write access was rechecked on 2026-11-21. Access does not mean a review has occurred or that he agrees with a particular change. Record decisions only from actual attributable confirmation; do not publish private correspondence.

### Before merging

1. Update against main by merging or rebasing your own unpublished work. Use merge for a shared published branch; do not rewrite another person's branch.
2. Inspect the diff for the declared scope and unintended replacement of other work.
3. Run `python tools/validate_repo.py`; for tooling changes, also `python -m unittest discover -s tools/tests -v`.
4. Check statuses, sources, attribution, rights, links and absence of private data.
5. Record unresolved questions and the next step. Green CI checks structure; it does not establish historical truth or human consent.

Merge after applicable checks and review. The initial empty-repository rollout was separately authorised by Alexander and recorded in [rollout](rollout/STATUS.md); it is not general permission to bypass review.

### Handoff and navigation

Use the [handoff template](../templates/handoff.md) for deliverables, branch, exact files, actual checks, unresolved decisions and the continuation point. The next assistant starts from actual files and Git state, not another assistant's confident summary.

The [collaboration guide](guides/working-together.md) gives practical steps for multiple people and assistants. The [branch index](BRANCHES.md) points to work awaiting integration. When files are added or renamed, run `python tools/navigate.py build` and `python tools/navigate.py check` before handoff. Keep running the core validator as above.
