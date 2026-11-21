---
id: PM-SESSION-2026-11-21-NAVIGATION
title: "Навигация и инструкции / Navigation and instructions"
status: draft
version: "0.1.0"
owner: alexanderyashin
updated: "2026-11-21"
source: "Alexander's request to improve repository navigation and instructions; base 23d18f172cfee87129695c082f4846c1a00734e6"
ai_assistance: "ChatGPT: documentation, navigation tooling, translation and verification; no coauthor approval inferred."
reviewers: []
---

# Навигация и инструкции / Navigation and instructions

## Русский

**Задача:** сделать проект понятным для людей и ИИ: точки входа, инструкции по типам работы, местные указатели и поддержание навигации при росте репозитория. Ветка: `work/sasha/repository-navigation`; база: `23d18f172cfee87129695c082f4846c1a00734e6`.

### Результат

- [Начало работы](../../../../../studio/START_HERE.md), [навигатор задач](../../../../../studio/NAVIGATION.md), [карта](../../../../../studio/REPOSITORY_MAP.md) и [каталог](../../../../../studio/CONTENT_CATALOG.md).
- [Руководства](../../../../../studio/guides/README.md) для сюжетов, совместной работы, ресурсов/адаптаций и заданий ИИ; полные RU/EN версии новых инструкций.
- 13 локальных AGENTS дополняют корневые требования; 229 README получают автоматически обновляемые навигационные блоки.
- 35 двуязычных маршрутов, локальный поиск по ID/теме, список контекста, детерминированная генерация и проверка указателей. Команды — в [tools](../../../../../tools/README.md).
- Дополнительная проверка актуальности навигации в существующем CI; прежний валидатор, тесты защит и минимальные права workflow сохранены.
- [Указатель веток](../../../../../studio/BRANCHES.md) с датированными ссылками на Draft PR #5, #6 и #7. Их творческие материалы не интегрировались этой задачей.

### Совместимость и проверка

В исходном `main` пять старых документов журнала не имели обязательных метаданных. Использовано то же исправление заголовков, которое уже присутствовало в [PR #6](https://github.com/alexanderyashin/48-24/pull/6), чтобы избежать конкурирующих ID при будущей интеграции. Исторический текст всех пяти документов сохранён побайтно; прежняя запись о сетевой блокировке остаётся исторической записью.

Локально проверены валидатор относительно фактической базы, актуальность навигации, `git diff --check` и **49 тестов**: 19 навигационных и 30 существовавших. Все завершились успешно. Дополнительно проверено сохранение рукописного текста, отказ от опасной перезаписи, целостность исходного SPOT, лицензий, структуры, команды и прежнего кода проверок.

Это запись об организационной работе. Художественный канон, согласие Ивана, окончательная приёмка переводов и запуск игровых производств не заявляются. Публикация конкретной редакции подтверждается содержащим её Git-коммитом/PR и соответствующим запуском [Actions](https://github.com/alexanderyashin/48-24/actions), а не одним локальным результатом.

### Продолжение

Использовать [руководство автора](../../../../../studio/guides/writing.md) для первой истории. При добавлении материалов или объединении веток пересобрать указатели, просмотреть diff и выполнить проверки. Состояние серверной защиты main проверяется отдельно; для этой настройки уже открыт [issue #2](https://github.com/alexanderyashin/48-24/issues/2).

## English

**Task:** make the project easier for humans and AI to navigate through entry points, practical guides, local links and maintainable generated indexes. Branch: `work/sasha/repository-navigation`; base: `23d18f172cfee87129695c082f4846c1a00734e6`.

### Deliverables

- [Start here](../../../../../studio/START_HERE.md), [task navigator](../../../../../studio/NAVIGATION.md), [map](../../../../../studio/REPOSITORY_MAP.md) and [catalogue](../../../../../studio/CONTENT_CATALOG.md).
- Complete RU/EN [guides](../../../../../studio/guides/README.md) for writing, collaboration, assets/adaptations and AI briefs.
- 13 scoped AGENTS supplement root requirements; all 229 READMEs receive generated local navigation.
- 35 bilingual task routes, local ID/topic search, context lists, deterministic generation and freshness checks; commands are documented in [tools](../../../../../tools/README.md).
- An additive navigation freshness step in CI, preserving the accepted validator, guard tests and minimal workflow permissions.
- A dated [branch index](../../../../../studio/BRANCHES.md) pointing to Draft PRs #5, #6 and #7. Their creative material was not integrated by this task.

### Compatibility and verification

The starting main had five project-log documents missing mandatory metadata. Their headers reuse the correction already present in [PR #6](https://github.com/alexanderyashin/48-24/pull/6), avoiding competing IDs during future integration. All five historical bodies were preserved byte for byte; the old network-blocker entry remains a historical record.

Local verification passed: the repository validator against the actual base, navigation freshness, `git diff --check`, and **49 tests** comprising 19 navigation and 30 existing guard tests. Additional review confirmed preservation of manual prose, safe refusal of destructive overwrites and unchanged SPOT, licences, structure, team and prior guard code.

This records organisational work, not creative canon, Ivan's approval, final human translation acceptance or a launched game production. Publication of a particular revision is evidenced by its containing Git commit/PR and matching [Actions run](https://github.com/alexanderyashin/48-24/actions), not by local checks alone.

### Handoff

Use the [writing guide](../../../../../studio/guides/writing.md) for a first story. After adding content or integrating branches, rebuild navigation, inspect the diff and run checks. Server-side protection of main is a separate setting already tracked in [issue #2](https://github.com/alexanderyashin/48-24/issues/2).
