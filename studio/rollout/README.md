# Развёртывание защиты GitHub

[Фактическое состояние](STATUS.md) отделено от подготовленной конфигурации. Файл JSON в репозитории сам по себе не меняет настройки сервера.

## Два готовых режима

| Файл | Когда применять | Правила |
| --- | --- | --- |
| [main-protection-bootstrap.json](main-protection-bootstrap.json) | Пока подтверждён только один GitHub-аккаунт | PR обязателен, repository-checks обязателен, актуальная база, закрытые обсуждения; запрещены удаление main и force push; число обязательных review — 0 |
| [main-protection-two-authors.json](main-protection-two-authors.json) | После добавления Ивана и обоих логинов в CODEOWNERS | Те же требования + одно review другого автора, code-owner review, отзыв устаревшего review и проверка последней правки |

Для PR одного из двух авторов его явная инициатива плюс подтверждение второго дают два авторских решения; две внешние approving reviews для двух человек потребовали бы третьего участника. Для стороннего канонического PR запись решения всё равно должна содержать обоих авторов. Один CODEOWNERS review сам по себе не проверяет эту смысловую границу.

Bootstrap сохраняет возможность одному владельцу сливать собственные PR после CI. Это не двухстороннее одобрение. После подключения Ивана замените bootstrap рабочим режимом, не заявляя старый режим полноценной защитой от единоличного решения.

## Порядок включения

1. Убедиться, что workflow `repository-checks` существует в main и хотя бы один раз завершился успешно.
2. В Settings → Rules → Rulesets использовать импорт JSON, либо задать те же правила в интерфейсе. Область — `refs/heads/main`, Enforcement — Active, список bypass — пустой.
3. Выбрать фактическую проверку `repository-checks` и её источник GitHub Actions, если интерфейс предлагает источник.
4. Для режима двух авторов сначала подтвердить логин Ивана, предоставить соответствующий доступ и включить обоих в CODEOWNERS. Ник и приглашение не подставлять предположением.
5. Сохранить настройки, прочитать созданный ruleset и записать его ID/режим в STATUS.md.

Владелец с уже настроенным GitHub CLI может применить файл из корня командой ниже. Команда меняет реальные настройки; выполняется один раз для нового ruleset. Для существующего ruleset используйте обновление его ID, а не создавайте дубли.

```bash
gh api --method POST repos/alexanderyashin/48-24/rulesets --input studio/rollout/main-protection-bootstrap.json
```

Конфигурации не включают платных сервисов и не меняют видимость репозитория. Администратор технически может менять правила, поэтому авторские договорённости и история решений остаются необходимыми.

## Основания

- [GitHub — создание ruleset](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository).
- [GitHub — REST API правил](https://docs.github.com/en/rest/repos/rules).
- [GitHub — CODEOWNERS и границы review](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).

Поля и поведение сверены с первичной документацией 2026-11-19.
