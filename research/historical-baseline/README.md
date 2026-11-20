# Historical baseline: source inventory, 1910–1940

This area prepares a documented historical research corpus for the Russian Empire, its successor jurisdictions and the wider world. The current stage records **sources and planned extractions only**. It contains no completed historical baseline, approved historical claims or fictional canon.

The source inventory and all new research tables are in English, as explicitly requested for this task. Earlier bilingual taxonomy descriptions remain where they were already present.

## Start here

| Document | Purpose |
| --- | --- |
| [Source registry](_catalog/sources.csv) | Bibliography, authority, scope, access, rights and verification for each distinct source |
| [Source-to-topic map](_catalog/source-topic-map.csv) | Planned source uses with locators and remaining work |
| [Source plan index](_catalog/source-plan-index.csv) | Source-first navigation: every source and all its destination topics |
| [Topic coverage](_catalog/coverage.csv) | Plans for all registered topics; counts describe planning, not verified historical coverage |
| [Current inventory status](_catalog/catalog-status.json) | Generated totals, source roles and coverage qualifications |
| [Research gaps](_catalog/research-gaps.csv) | Explicit unresolved depth, geographic, access and item-selection requirements |
| [Research protocol](_catalog/research-protocol.md) | Admission criteria, limitations and the next extraction stage |
| [Evidence log](_catalog/evidence-log.csv) | URLs, dates and scope of the checks actually made |
| [Search log](_catalog/search-log.csv) | Recorded search queries and selection decisions |
| [Data dictionary](_catalog/data-dictionary.csv) | Table fields, types, nulls and interpretation |

## Subject navigation

Each domain, group and individual topic has an English `source-plan.csv`. These are generated views of the shared registry and mapping table. Edit the central tables, then regenerate; source metadata has one authoritative home.

| Domain | Domain source plan |
| --- | --- |
| [Chronology and periodization](chronology/README.md) | [CSV](chronology/source-plan.csv) |
| [Geography and territory](geography/README.md) | [CSV](geography/source-plan.csv) |
| [Climate and environment](climate-environment/README.md) | [CSV](climate-environment/source-plan.csv) |
| [Population and migration](population-migration/README.md) | [CSV](population-migration/source-plan.csv) |
| [State and government](state-government/README.md) | [CSV](state-government/source-plan.csv) |
| [Politics and ideologies](political-life/README.md) | [CSV](political-life/source-plan.csv) |
| [Law and justice](law-justice/README.md) | [CSV](law-justice/source-plan.csv) |
| [International relations](international-relations/README.md) | [CSV](international-relations/source-plan.csv) |
| [Military affairs and warfare](military-warfare/README.md) | [CSV](military-warfare/source-plan.csv) |
| [Security and intelligence](security-intelligence/README.md) | [CSV](security-intelligence/source-plan.csv) |
| [Economy and finance](economy-finance/README.md) | [CSV](economy-finance/source-plan.csv) |
| [Commerce and trade](commerce-trade/README.md) | [CSV](commerce-trade/source-plan.csv) |
| [Industry and manufacturing](industry-manufacturing/README.md) | [CSV](industry-manufacturing/source-plan.csv) |
| [Mining and raw materials](mining-resources/README.md) | [CSV](mining-resources/source-plan.csv) |
| [Agriculture and food](agriculture-food/README.md) | [CSV](agriculture-food/source-plan.csv) |
| [Infrastructure and utilities](infrastructure-utilities/README.md) | [CSV](infrastructure-utilities/source-plan.csv) |
| [Transport and logistics](transport-logistics/README.md) | [CSV](transport-logistics/source-plan.csv) |
| [Energy and fuels](energy-fuels/README.md) | [CSV](energy-fuels/source-plan.csv) |
| [Engineering and technology](engineering-technology/README.md) | [CSV](engineering-technology/source-plan.csv) |
| [Science and research](science-research/README.md) | [CSV](science-research/source-plan.csv) |
| [Medicine and health](medicine-health/README.md) | [CSV](medicine-health/source-plan.csv) |
| [Education and knowledge](education-knowledge/README.md) | [CSV](education-knowledge/source-plan.csv) |
| [Social structure](social-structure/README.md) | [CSV](social-structure/source-plan.csv) |
| [Labor and professions](labor-professions/README.md) | [CSV](labor-professions/source-plan.csv) |
| [Religion and belief](religion-belief/README.md) | [CSV](religion-belief/source-plan.csv) |
| [Media and communication](media-communication/README.md) | [CSV](media-communication/source-plan.csv) |
| [Arts and culture](arts-culture/README.md) | [CSV](arts-culture/source-plan.csv) |
| [Architecture and urbanism](architecture-urbanism/README.md) | [CSV](architecture-urbanism/source-plan.csv) |
| [Everyday life](everyday-life/README.md) | [CSV](everyday-life/source-plan.csv) |
| [Visual and material culture](visual-material-culture/README.md) | [CSV](visual-material-culture/source-plan.csv) |
| [Crises and disasters](crises-disasters/README.md) | [CSV](crises-disasters/source-plan.csv) |
| [Russian Empire](russian-empire/README.md) | [CSV](russian-empire/source-plan.csv) |
| [Soviet Russia and USSR](soviet-union/README.md) | [CSV](soviet-union/source-plan.csv) |
| [Countries and comparative history](regional-comparisons/README.md) | [CSV](regional-comparisons/source-plan.csv) |
| [People and biographies](people-biographies/README.md) | [CSV](people-biographies/source-plan.csv) |
| [Statistics and measurements](statistics-data/README.md) | [CSV](statistics-data/source-plan.csv) |
| [Languages and ethnography](languages-ethnography/README.md) | [CSV](languages-ethnography/source-plan.csv) |

## Reading the inventory correctly

The date window concerns the historical subject, not the publication date of a modern research book. Apply the actual jurisdiction and document date; the umbrella Russian scope must not turn every record after 1917 into an Imperial Russian record. Exact legal transitions, border changes and calendar conversions require source-level checking during extraction.

An authoritative catalogue verifies that a source or item exists and describes its provenance. It does not verify every statement in that source. A museum object establishes an attested example; it does not by itself establish mass production, a regulation or common usage. A standard describes a specification; adoption and actual manufacture require separate evidence.

The bibliography covers every taxonomy topic but is not claimed to exhaust all relevant scholarship, countries, archives or objects. Open gaps and row-level `remaining_work` fields preserve that distinction. All extraction statuses remain `not-started` and all human review statuses remain `pending`.

## Maintenance

See the [catalogue instructions](_catalog/README.md) and [machine-readable taxonomy](taxonomy.json). Southeast Asia and Oceania have dedicated topics so these geographic areas can be investigated explicitly.

From the repository root:

```bash
python research/historical-baseline/_catalog/manage_catalog.py
python research/historical-baseline/_catalog/manage_catalog.py --check
```

Only original bibliographic descriptions, research plans and links are stored in this pass. Any later import of photographs, scans, audio or other third-party files must follow the [asset workflow](../../studio/ASSET_WORKFLOW.md) and the recorded item-specific rights.
