# Реестры проекта

| Файл | Содержание и правило |
| --- | --- |
| [content-index.csv](content-index.csv) | Рабочие документы из SPOT; ссылка на неизменяемый источник и статус каждой карточки |
| [source-register.csv](source-register.csv) | Источники и пределы их применения |
| [decisions.csv](decisions.csv) | Все исходные CAN с исходным авторским статусом; это не журнал новых approval |
| [open-questions.csv](open-questions.csv) | Единый текущий учёт GAP, DIV, PM-Q и новых OQ; точные адреса ответа — в open-question-targets.csv |
| [asset-register.csv](asset-register.csv) | ID ресурсов, пути, внешние мастера, права, хеши и происхождение |
| [contribution-register.csv](contribution-register.csv) | Пообъектный учёт творческих вкладов, типов участия и происхождения без вывода имущественных долей |
| [work-register.csv](work-register.csv) | Текущие задачи без Issue; Issue/PR остаётся основным журналом для задач на GitHub |
| [release-register.csv](release-register.csv) | Фактически согласованные и выпущенные версии продуктов |

Пустые реестры имеют только заголовки: фиктивных ресурсов, сроков и одобрений нет. Строки редактируются минимально; глобальное переформатирование CSV осложняет параллельную работу.

Реальные новые решения — в [approvals](../approvals/README.md); права сторонних материалов — в [юридическом реестре](../../legal/THIRD_PARTY_ASSETS.csv). [Как пользоваться импортом](../source-import-guide.md).

## Текущие рабочие места и языки / Current working locations and languages

[Две вики / Two wikis](../navigation/README.md) связывают полные предметные документы. / The wikis connect full subject documents.

- `content-index.csv`: одна строка на предметную сущность, пути RU/EN и готовность перевода / one row per subject entity, RU/EN paths and translation state.
- `decisions.csv`, `open-questions.csv`: исходные поля сохранены; `working_path_ru` и `working_path_en` ведут к текущим редакциям / source fields retained; working paths lead to current editions.
- [По каждому файлу / Every file](../navigation/file-catalog.csv): полный состав репозитория, включая служебные материалы / complete repository inventory, including infrastructure.

Добавление ссылок не изменяет статуса согласования или открытости вопроса. / Adding links does not change agreement status or close a question.

<!-- unified-question-entrypoint:start -->

## Единый реестр вопросов / Unified question register

[Все вопросы — RU](../navigation/ru/open-questions/README.md) · [All questions — EN](../navigation/en/open-questions/README.md) · [Первичные записи / Master records](open-questions.csv) · [Адреса правки / Editing destinations](open-question-targets.csv)

Текущие статусы всех предметных, производственных и организационных вопросов ведутся в одном реестре. Вики показывают полные языковые представления, точные документы для ответа и обратный указатель по файлам. / Current states of all subject, production and organisational questions live in one register. The wikis provide full language views, exact answer documents and a reverse file index.

[Норматив ведения — Draft](proposals/open-question-register-v0-1.md) · [Maintenance rules — Draft](proposals/open-question-register-v0-1.en.md)

<!-- unified-question-entrypoint:end -->
