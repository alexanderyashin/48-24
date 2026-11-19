# Журнал управления проектом / Project Management Log

Единая точка входа для оперативной истории 48/24. Не дублирует первичные реестры, GitHub Issues, коммиты или подтверждения канона. / Single entry point for project execution history. It does not duplicate source registers, GitHub Issues, commits, or canon approvals.

## Разделы / Sections

- [Решения / Decision log](DECISIONS.md) — что принято, кем и на каком основании / decisions and evidence
- [Открытые вопросы / Open issues](OPEN_ISSUES.md) — что требует решения / unresolved issues
- [Выполненная работа / Work log](WORK_LOG.md) — результаты и ссылки на GitHub / completed work and evidence
- [Дорожная карта / Roadmap](ROADMAP.md) — очередность и зависимости / priorities and dependencies
- [Сессии / Sessions](sessions/README.md) — срезы состояния и точки продолжения / session snapshots and handoffs

## Правила / Rules

1. **Одна запись — один ID и ссылка на первоисточник.** Для всех открытых вопросов используйте [open-questions.csv](../../../../studio/registers/open-questions.csv); для импортированных положений — [decisions.csv](../../../../studio/registers/decisions.csv); для подтверждений канона — [approvals](../../../../studio/approvals/README.md); для работы — GitHub Issues/commits или [work-register.csv](../../../../studio/registers/work-register.csv).
2. **Различайте** `proposed`, `agreed-for-work`, `implemented`, `verified`, `approved-canon`. Устное распоряжение Александра позволяет записать выполненную организационную работу, но не означает согласия Ивана с художественным каноном.
3. В конце сессии фиксируйте дату, выполненные изменения, ссылки, принятые рабочие решения, нерешённые вопросы, ограничения проверок и следующий шаг. Не выдавайте непроверенные утверждения за результаты.
4. **Не создавайте дубликаты** полных реестров в этой папке: разделы содержат краткие сводки и ссылки. Если вопрос закрыт, обновите исходную запись и затем сводку.
5. Работа в `main` не означает канонизацию. Валидатор запускается в конце сессии по текущему указанию владельца; здесь не фиксируется результат проверки, которой не было.

## English

Keep stable IDs and source links; distinguish proposals, implementation, verification and canon approval. Update authoritative registers first, then this index. Session handoffs record actual changes, unresolved questions, unperformed checks and the next action. Direct commits to main do not constitute creative canon approval.

<!-- unified-question-entrypoint:start -->

## Единый реестр вопросов / Unified question register

[Все вопросы — RU](../../../../studio/navigation/ru/open-questions/README.md) · [All questions — EN](../../../../studio/navigation/en/open-questions/README.md) · [Первичные записи / Master records](../../../../studio/registers/open-questions.csv) · [Адреса правки / Editing destinations](../../../../studio/registers/open-question-targets.csv)

Текущие статусы всех предметных, производственных и организационных вопросов ведутся в одном реестре. Вики показывают полные языковые представления, точные документы для ответа и обратный указатель по файлам. / Current states of all subject, production and organisational questions live in one register. The wikis provide full language views, exact answer documents and a reverse file index.

[Норматив ведения — Draft](../../../../studio/registers/proposals/open-question-register-v0-1.md) · [Maintenance rules — Draft](../../../../studio/registers/proposals/open-question-register-v0-1.en.md)

<!-- unified-question-entrypoint:end -->
