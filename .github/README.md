# Настройки GitHub / GitHub configuration

Здесь находятся CODEOWNERS, шаблон PR, формы Issue и CI. Изменения рассматриваются как работа с управлением проектом. / This area holds CODEOWNERS, the PR template, Issue forms and CI. Changes are reviewed as repository governance work.

| Файл или папка / File or folder | Назначение / Purpose |
| --- | --- |
| [CODEOWNERS](CODEOWNERS) | Кто участвует в рассмотрении; не приглашение и не выдача прав / Review ownership; not an invitation or permission grant |
| [pull_request_template.md](pull_request_template.md) | Цель, изменения, реальные проверки и передача / Goal, changes, actual checks and handoff |
| [ISSUE_TEMPLATE](ISSUE_TEMPLATE/README.md) | Формы задач, решений и вопросов / Task, decision and question forms |
| [workflows](workflows/README.md) | Проверки репозитория и актуальности навигации / Repository and navigation freshness checks |

[Начать работу / Start](../studio/START_HERE.md) · [Куда положить материал / Routes](../studio/NAVIGATION.md) · [Совместная работа / Collaboration](../studio/guides/working-together.md).

Серверная защита ветки настраивается отдельно в GitHub. Сам файл workflow не запрещает прямую запись; фактическое состояние описывается с датой в [rollout](../studio/rollout/STATUS.md). / Server-side branch protection is configured separately in GitHub. A workflow file alone does not prohibit direct pushes; dated observations belong in [rollout](../studio/rollout/STATUS.md).

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../README.md) › [.github](README.md)

[По задаче / By task](../studio/NAVIGATION.md) · [Карта / Map](../studio/REPOSITORY_MAP.md) · [Материалы / Content](../studio/CONTENT_CATALOG.md) · [Шаблоны / Templates](../templates/README.md)

### Подразделы / Subfolders

- [Шаблоны задач / Issue templates](ISSUE_TEMPLATE/README.md) — `ISSUE_TEMPLATE/`.
- [Автоматические проверки / Automated checks](workflows/README.md) — `workflows/`.

### Файлы рядом / Files here

- [GitHub: контекст для помощника / GitHub assistant context](AGENTS.md) — `AGENTS.md`.
- [CODEOWNERS](CODEOWNERS) — `CODEOWNERS`.
- [pull_request_template.md](pull_request_template.md) — `pull_request_template.md`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context .github`

<!-- NAVIGATION:END -->
