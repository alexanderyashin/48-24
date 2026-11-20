# Tabular source-record template guidance

Use a new row in [sources.csv](sources.csv), following [data-dictionary.csv](data-dictionary.csv). This replaces the earlier bilingual standalone source-card template for the present English-only, tabular research phase.

| Record block | Required content |
| --- | --- |
| Identity | Stable `source_id`, title, creator, publisher/custodian, publication date, type, canonical and verification URLs |
| Scope | Historical years when known, period qualifications, geography, source languages and proposed use |
| Assessment | Authority basis, reliability scope, limits, verification date/method/status |
| Access and rights | Access/full-text status, licence status and scope, licence URL if established, rights notes |
| Workflow | Source role, admission status, item-selection requirement and human-review status |

Add separate rows in [evidence-log.csv](evidence-log.csv) for the checks and in [source-topic-map.csv](source-topic-map.csv) for each planned topic use. Store page or item locators in the mapping, and unresolved requirements in `remaining_work` and the gap register. Do not add a historical-facts section to a source-planning record.

An unknown optional identifier, licence URL or numeric coverage bound remains empty. Required descriptive fields should explain what is known and what is unresolved. Check the registry before reserving a new ID; example IDs are not reservations.
