# Автоматические проверки / Automated checks

## Русский

[repository-checks.yml](repository-checks.yml) запускается для Pull Request в `main`, push в `main` и ручного запуска. Имя проверки для настройки GitHub — **`repository-checks`**.

Порядок: принятый валидатор из базового коммита с `--base`; валидатор предлагаемого дерева; `python tools/navigate.py check`; тесты инструментов. Навигационная проверка ищет устаревшие указатели и некорректные маршруты. Она не записывает исправления: выполните `python tools/navigate.py build` в своей ветке, просмотрите изменения и сохраните их commit.

Workflow использует только `contents: read`, не сохраняет токен в checkout, не загружает submodules/LFS и не использует `pull_request_target`. Проверка базовой версией сохраняется: замена нового скрипта не отменяет проверку прежних правил. Для первоначального коммита без базового валидатора проверяется текущее дерево и тесты.

Защита ветки, обязательность checks и ограничения обхода настраиваются отдельно в GitHub Rulesets. Зелёная проверка не является доказательством согласия человека, канона, авторских прав или работающего продукта.

`actions/checkout` сохранён на SHA `3d3c42e5aac5ba805825da76410c181273ba90b1`, который был сверён с официальным `v7.0.1` через [GitHub API](https://api.github.com/repos/actions/checkout/git/ref/tags/v7.0.1) 2026-11-19. Обновление версии оформляется отдельной задачей.

## English

[repository-checks.yml](repository-checks.yml) runs for pull requests into `main`, pushes to `main` and manual dispatch. The check name used in GitHub settings is **`repository-checks`**.

It runs the accepted base validator with `--base`, the proposed-tree validator, `python tools/navigate.py check`, and tool tests. The navigation check detects stale indexes and invalid routes. It does not write fixes: run `python tools/navigate.py build` in your task branch, review the diff and commit the changes.

Permissions remain `contents: read`; checkout does not retain credentials or fetch submodules/LFS; the workflow does not use `pull_request_target`. The accepted base validator remains active so changing the proposed script does not remove prior checks. An initial commit without a base validator checks the current tree and tests.

Branch protection, required checks and bypass restrictions are configured separately in GitHub Rulesets. A successful check does not establish human consent, canon approval, rights or a working product.

`actions/checkout` remains pinned to `3d3c42e5aac5ba805825da76410c181273ba90b1`, recorded as verified against official `v7.0.1` through the [GitHub API](https://api.github.com/repos/actions/checkout/git/ref/tags/v7.0.1) on 2026-11-19. Updating it is a separate task.

[Проверки / Checks](../../studio/repository-checks.md) · [Команды навигации / Navigation commands](../../tools/README.md).

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../../README.md) › [.github](../README.md) › [workflows](README.md)

[По задаче / By task](../../studio/NAVIGATION.md) · [Карта / Map](../../studio/REPOSITORY_MAP.md) · [Материалы / Content](../../studio/CONTENT_CATALOG.md) · [Шаблоны / Templates](../../templates/README.md)

### Файлы рядом / Files here

- [repository-checks.yml](repository-checks.yml) — `repository-checks.yml`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context .github/workflows`

<!-- NAVIGATION:END -->
