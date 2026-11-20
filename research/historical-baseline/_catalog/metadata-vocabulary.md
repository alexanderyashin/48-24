# Метаданные / Metadata vocabulary

| Поле / Field | Смысл / Meaning |
| --- | --- |
| `id` | Неизменный ID источника / Stable source ID |
| `kind` | `primary-document`, `secondary-study`, `photo`, `map`, `drawing`, `patent`, `catalog`, `newspaper`, `statistical-series`, `oral-history`, `artifact`, `other` |
| `source_date` | Историческая дата создания, не дата загрузки / Historical creation date, not ingestion date |
| `period_start, period_end` | Годы, к которым относятся сведения / Historical coverage years |
| `geography` | Исторические названия, современная привязка при необходимости / Historical names; modern equivalents where useful |
| `topic_tags` | Дополнительные темы без дублирования файла / Cross-topic tags without copying files |
| `evidence_status` | `unreviewed`, `source-verified`, `claim-corroborated`, `contested`, `rejected` |
| `rights_status` | `pending`, `public-domain`, `licensed`, `permission-on-file`, `project-authorized`, `link-only` |
| `related_ids` | Связи между карточками / Cross-references |

**RU:** `source-verified` означает проверку существования/происхождения документа; `claim-corroborated` требует независимых подтверждений конкретного вывода. Даже статус `claim-corroborated` не утверждает художественный канон. Термины прав в этом справочнике описывают реестр ссылок; для закоммиченного бинарного файла используйте разрешённые значения из `studio/ASSET_WORKFLOW.md`.

**EN:** `source-verified` means the document and its provenance were checked; `claim-corroborated` requires independent support for a specific claim. Neither status authorizes fictional canon. These rights terms describe source-link records; committed binary files must follow `studio/ASSET_WORKFLOW.md`.
