# Реестры проекта

| Файл | Содержание и правило |
| --- | --- |
| [content-index.csv](content-index.csv) | Рабочие документы из SPOT; ссылка на неизменяемый источник и статус каждой карточки |
| [source-register.csv](source-register.csv) | Источники и пределы их применения |
| [decisions.csv](decisions.csv) | Все исходные CAN с исходным авторским статусом; это не журнал новых approval |
| [open-questions.csv](open-questions.csv) | Открытые GAP и развилки DIV, без выдуманного закрытия |
| [asset-register.csv](asset-register.csv) | ID ресурсов, пути, внешние мастера, права, хеши и происхождение |
| [work-register.csv](work-register.csv) | Текущие задачи без Issue; Issue/PR остаётся основным журналом для задач на GitHub |
| [release-register.csv](release-register.csv) | Фактически согласованные и выпущенные версии продуктов |

Пустые реестры имеют только заголовки: фиктивных ресурсов, сроков и одобрений нет. Строки редактируются минимально; глобальное переформатирование CSV осложняет параллельную работу.

Реальные новые решения — в [approvals](../approvals/README.md); права сторонних материалов — в [юридическом реестре](../../legal/THIRD_PARTY_ASSETS.csv). [Как пользоваться импортом](../source-import-guide.md).
