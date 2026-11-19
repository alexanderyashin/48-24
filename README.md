# 48/24

**Совместная разработка оригинального гримдарк-эпоса и его будущих адаптаций.**

Worldbuilding and development of an original grimdark universe inspired by Imperial Russia, Victorian industrialism, dark steampunk, and alternative history.

48/24 — рабочее обозначение проекта. Окончательное название эпоса ещё не утверждено. «Киберстолыпин» — прежнее рабочее название исходного документа, а не обязательное название будущих произведений.

Это публичная рабочая площадка Александра Яшина и Ивана Конюшкова. Здесь есть черновики, развилки, отвергнутые идеи и **спойлеры ко всему эпосу**. Публичность папки и нахождение в `main` не делают её содержимое каноном и не предоставляют свободную лицензию на материалы.

## Начать работу

1. Прочитайте [краткое руководство](studio/START_HERE.md).
2. Для совместной работы откройте [процесс задач и PR](studio/WORKFLOW.md); для ИИ — [AGENTS.md](AGENTS.md).
3. Выберите предметную область ниже и работайте в её `drafts` в отдельной ветке.
4. Перед передачей изменений выполните `python tools/validate_repo.py` и проверьте итоговый diff.

## Карта студии

| Раздел | Что находится внутри |
| --- | --- |
| [studio](studio/README.md) | Правила, команда, реестры, решения и организация работы |
| [world](world/README.md) | Библия мира, хронология, география, институты, фракции, общество, экономика, технологии |
| [narrative](narrative/README.md) | Логлайны, персонажи, арки, выпуски, сцены, диалоги |
| [art](art/README.md) | Арт-дирекшн, концепты, персонажи, окружение, предметы, символика, палитры, шрифты, карты, UI |
| [audio](audio/README.md) | Музыка, звуковая среда, голоса |
| [products](products/README.md) | Компьютерная игра, YouTube, настольная игра, книги |
| [research](research/README.md) | Исторические источники, визуальные ссылки, технические исследования |
| [community](community/README.md) | Фанатские истории, предложения и согласованные подборки |
| [production](production/README.md) | Планирование, выпуски, продвижение |
| [legal](legal/README.md) | Учёт прав, сторонних материалов и разрешений |
| [templates](templates/README.md) | Карточки материалов, задач, решений и ресурсов |
| [tools](tools/README.md) | Автоматическая проверка структуры и метаданных |

В каждой творческой области: **drafts → canon → archive**. Отвергнутый черновик также перемещается сразу из `drafts` в `archive`. Подробности — в [правилах канона](studio/CANON_POLICY.md).

## Текущая основа

- [Импорт исходного SPOT 0.1](world/world-bible/drafts/spot-0-1-import.md): авторские позиции сохранены, согласование импорта ещё не выполнялось.
- [Премиса](narrative/premise/drafts/premise-v0-1.md), [варианты логлайна](narrative/premise/drafts/logline-options-v0-1.md), [визуальные принципы](art/art-direction/drafts/art-direction-v0-1.md).
- [Реестр открытых вопросов](studio/registers/open-questions.csv), [положения исходного документа](studio/registers/decisions.csv), [план запуска](production/planning/drafts/launch-roadmap-v0-1.md).
- [Состояние организационного rollout](studio/rollout/STATUS.md): что настроено, а что требует административного действия.

## Права и участие

Официальные материалы предоставляются на условиях [LICENSE](LICENSE). **All rights reserved**, с ограниченными разрешениями для фанатского творчества и работы над этим проектом.

Самостоятельную бесплатную некоммерческую фанпрозу можно публиковать с атрибуцией по [Fan Content Policy](FAN_CONTENT_POLICY.md). Использование официальных иллюстраций, визуальных ресурсов и коммерческие проекты требуют отдельного разрешения там, где закон требует согласия правообладателя. Право просмотра и форка GitHub сохраняется.

Для предложений в проект: [CONTRIBUTING](CONTRIBUTING.md) и [условия конкретного вклада](CONTRIBUTOR_TERMS.md). Публикация фанфика сама по себе не передаёт нам права на него. Права соавторов не перераспределяются этим репозиторием.

## Вики проекта / Project wikis

**[Русская вики](studio/navigation/ru/README.md) · [English wiki](studio/navigation/en/README.md)**

Предметные нормативы SPOT находятся в своих разделах, все в статусе Draft. Вики связывают полные русские и английские версии, исходный консенсус, обсуждения, белые пятна и каталог каждого файла. / SPOT specifications remain in their subject areas, all as Draft. The wikis connect full Russian and English editions, source consensus, discussions, open gaps, and the catalogue of every file.

[Правило обязательной каталогизации](studio/navigation/proposals/cataloguing-standard-v0-1.md) · [Mandatory cataloguing rule](studio/navigation/proposals/cataloguing-standard-v0-1.en.md) · [Полный каталог / Full catalogue](studio/navigation/file-catalog.csv)

<!-- unified-question-entrypoint:start -->

## Единый реестр вопросов / Unified question register

[Все вопросы — RU](studio/navigation/ru/open-questions/README.md) · [All questions — EN](studio/navigation/en/open-questions/README.md) · [Первичные записи / Master records](studio/registers/open-questions.csv) · [Адреса правки / Editing destinations](studio/registers/open-question-targets.csv)

Текущие статусы всех предметных, производственных и организационных вопросов ведутся в одном реестре. Вики показывают полные языковые представления, точные документы для ответа и обратный указатель по файлам. / Current states of all subject, production and organisational questions live in one register. The wikis provide full language views, exact answer documents and a reverse file index.

[Норматив ведения — Draft](studio/registers/proposals/open-question-register-v0-1.md) · [Maintenance rules — Draft](studio/registers/proposals/open-question-register-v0-1.en.md)

<!-- unified-question-entrypoint:end -->
