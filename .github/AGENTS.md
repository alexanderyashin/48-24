# GitHub: контекст для помощника / GitHub assistant context

## Русский

Область: `.github/` и вложенные папки. Это дополнение к [корневому AGENTS.md](../AGENTS.md); его требования и действующие политики сохраняются. Прочитайте [README](README.md), [WORKFLOW](../studio/WORKFLOW.md), [проверки](../studio/repository-checks.md) и [состояние rollout](../studio/rollout/STATUS.md).

- Здесь CODEOWNERS, формы Issue, шаблон PR и автоматические проверки. Поддерживайте ссылки на актуальные инструкции; формулировки форм должны соответствовать действующим правилам.
- Сохраняйте минимальные разрешения workflow, безопасную обработку недоверенных изменений и выполнение обязательных проверок. Не подменяйте проверку содержимого флагом успешного результата.
- Изменение файла CODEOWNERS не приглашает человека и не предоставляет доступ. Файл конфигурации защиты не означает включённую защиту ветки; состояние проверяется в GitHub.
- Не отмечайте review, согласие или завершённый выпуск от имени другого человека. Технический результат CI и человеческое решение различаются.
- Если форма добавляет маршрут к инструкции, проверьте ссылку и соответствие обеих языковых версий. Подробности совместной работы — в [руководстве](../studio/guides/working-together.md).

## English

Scope: `.github/` and descendants. This supplements the [root AGENTS.md](../AGENTS.md); its requirements and authoritative policies still apply. Read this area's [README](README.md), [WORKFLOW](../studio/WORKFLOW.md), [check documentation](../studio/repository-checks.md) and [rollout status](../studio/rollout/STATUS.md).

- This area holds CODEOWNERS, Issue forms, the PR template and automated checks. Keep links current and form wording consistent with policy.
- Preserve minimal workflow permissions, safe handling of untrusted changes and required checks. Do not replace content validation with a success flag.
- Editing CODEOWNERS neither invites users nor grants access. A protection configuration file does not mean branch protection is enabled; verify actual GitHub state.
- Do not claim another person's review, consent or release approval. CI results and human decisions are distinct.
- Verify instruction links and both language versions when adding routes. See the [collaboration guide](../studio/guides/working-together.md).
