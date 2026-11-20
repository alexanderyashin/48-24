# Metadata vocabulary

The authoritative field definitions are in [data-dictionary.csv](data-dictionary.csv); headers and required fields are in [catalog-schema.json](catalog-schema.json).

| Concept | Rule |
| --- | --- |
| Stable identity | `source_id` is unique; duplicate IDs are retired through `source-id-aliases.csv` |
| Dates | `publication_date` is descriptive; `coverage_start` and `coverage_end` are integer years or empty; qualifications belong in `period_coverage_notes` |
| Geographic scope | Preserve the source's jurisdiction, territory, locality and classification limits; do not silently substitute modern boundaries |
| Admission | `accepted-for-source-planning`, `discovery-route-only` or `method-support-only`; none means claim verification |
| Reliability | Read `authority_basis`, `reliability_scope` and `limitations` together; there is no unsupported numeric confidence score |
| Access | `access_status` and `full_text_status` describe what can be obtained and what was actually inspected |
| Rights | `license_status`, `license_url`, `license_scope` and `rights_notes` are read together; unknown rights remain `not-established` |
| Collection selection | `needs_item_selection` is `true` or `false`; even a specific book may still need page selection |
| Research stage | Every mapping is `not-started`; human review is `pending` in this inventory |
| Priority | `high`, `medium` or `low` describes the proposed research task, not the truth of a source |
| Missing data | Empty optional fields are null; never interpret them as zero, unrestricted access or public-domain status |

CSV files use UTF-8, a header row, standard quoted fields and LF record terminators. JSON-array cells are named with `_json`. Parse them as JSON after parsing CSV; do not split on commas inside a quoted field. IDs are strings. Source-type and verification descriptions remain detailed text because they preserve institution-specific distinctions.
