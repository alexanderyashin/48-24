# Research protocol and provenance

## Scope and current result

The assignment is a source inventory and extraction plan for historical knowledge about 1910–1940, with detailed Russian Imperial and successor-state coverage and international comparison across all social, material, scientific and environmental subjects in the taxonomy. Historical baseline facts are deliberately outside this stage.

Current source, mapping, verification, query, topic, group and domain counts are generated in [catalog-status.json](catalog-status.json). Per-topic counts and qualifications are in [coverage.csv](coverage.csv); they measure the source plan, not completed historical knowledge.

The workflow was source-first: identify and assess the source; establish a stable registry record; then enumerate its proposed uses in the appropriate topic documents. Research was divided by subject for collection, then consolidated, checked for duplicate identity and joined into a common mapping table. The published tables are the maintained record; temporary research scripts and working notes are not additional sources of truth.

## Admission criteria

| Source role | Why it can be admitted | Evidentiary boundary |
| --- | --- | --- |
| Scholarly analysis | Specialist scholarship at university presses, peer-reviewed journals or established scholarly reference works | Conclusions remain attributed interpretations; review methods, citations and relevant passages before accepting a claim |
| Edited primary source | Scholarly documentary edition with identifiable editors and provenance | Distinguish original record, transcription, translation, selection and editorial commentary |
| Primary document or object | An identified official publication, technical report, accessioned object or archival item held by a recognized institution | High provenance is not automatic accuracy, representativeness, compliance or proof of common usage |
| Reference collection or series | A recognized archive, museum, library, official statistical series or documentary collection | A discovery route until a dated volume, item, issue, table, file or folio is selected |
| Scientific data | Documented institutional or scholarly dataset with identifiable release or methods | Respect reconstruction uncertainty, revisions, variable definitions, geography and missing observations |
| Discovery index | A standards directory, bibliography, finding aid or verified parent-volume lead | Locates potential sources; it cannot support a historical assertion without the underlying item |
| Method support | An authoritative computational service used for a specifically defined calculation | Calculated quantities are not observations or contemporary testimony; retain model inputs and assumptions |

Unattributed summaries, commercial listings, search-engine generated summaries and unsourced popular pages are not admitted as historical evidence. Search results are used to discover and verify an authoritative record, and any reliance on an indexed record instead of an opened page is stated. A publisher or library record can verify edition identity even when a full-text copy is unavailable.

There is no numerical reliability score. Such a score would conflate provenance, method, factual accuracy and representativeness. Each registry record instead states its authority basis, the exact scope in which it can be relied upon, and its limits. `accepted-for-source-planning` does not mean that a historical claim has passed review.

## What was verified

Source records contain a canonical link, the verification route, the date of checking and a description of the check. Where available, DOI, ISBN, accession or catalogue identifiers are recorded. Publication date is kept separate from historical coverage. Titles of non-English publications may be supplied English translations or transliterations; the `languages` field records the language of the source itself.

Checks range from an official indexed catalogue record to opened abstracts, contents, full-text routes, PDFs, object records and rights statements. These levels are not interchangeable. No registry entry claims systematic full-text extraction. Access failures, script-only viewers, reading-room restrictions and purchase or subscription requirements are retained rather than silently treated as open access.

The [evidence log](evidence-log.csv) records observed bibliographic and access evidence. A tool reference is an auxiliary research trace; the public URL and institution/edition identifier are the durable rechecking route. It is not a citation to a historical fact. Search rows may share a batch and retained results; they are not a complete ranking of web results. English translations of Russian search terms are labelled as translations.

## Mapping rules

Each mapping states the topic, source ID, locator or locator-finding route, proposed fields or questions, expected material, geographic and chronological focus, mapping basis and remaining work. Exact page numbers are included only where checked. A statement that pages must be found is preferable to an invented page reference.

General histories provide orientation and bibliographic leads. They do not automatically supply every narrow technical detail. A dated article, legal edition, statistical volume, technical publication or accessioned object provides a more specific route; actual passages, specifications and images still require examination. Museum dating phrases such as associated date, manufacture date and approximate date must remain distinct.

Mappings are proposals based on verified title, description, contents, institutional scope or inspected metadata. They are not claims that every proposed variable has already been located. All rows explicitly have `extraction_status=not-started`. A collection mapping requires item selection. A narrow topic with only discovery routes stays visibly marked in [coverage.csv](coverage.csv).

## Coverage and unresolved work

The taxonomy is a practical organizational structure, not proof that all human activities have been exhaustively classified. Every current leaf has a source plan, but geographic depth and evidentiary precision vary. Country-level syntheses do not replace local archives; European and North American technical standards are not evidence of Russian adoption; postwar memoirs need retrospective-source criticism.

The [gap register](research-gaps.csv) records specific open requirements. Its row count is not the total amount of remaining work: every mapping also has a `remaining_work` field, including full-text, page, object and edition checks. Zero explicit gap rows for a topic does not mean that its research is complete.

Continuous series must be selected by year and documented boundaries. Do not join changing national territories, units, currencies, classifications, price bases or reconstructed and directly observed values without an explicit method. A modern publication date is allowed when the subject is historical; material outside 1910–1940 is contextual and must not silently enter the target baseline.

## Access and reuse

Reading access and reuse permission are separate fields. A public catalogue or downloadable scan does not establish an open licence. Where a licence was verified, the record states its scope and links to the applicable page; third-party illustrations may have separate terms. `not-established` is an honest research status, not a prohibition or a permission. Only links and original research metadata are included in this pass.

## Next authorized stage boundary

The present deliverable ends at source planning. A later extraction stage would select the exact page, table, article, object view or archive folio; verify its date and context; record the source's statement and qualifications; corroborate the proposed claim; and preserve a claim-to-locator link. It would keep transcription, translation, inference and creative interpretation distinct. None of those claim records have been created here.

## AI and human provenance

| Field | Value |
| --- | --- |
| Requested by | Alexander Yashin |
| Research and assembly | ChatGPT, GPT-6 Astra Pro, with parallel research agents |
| Research date | 2026-11-20 |
| Inputs | Existing repository taxonomy; publicly accessible scholarly and institutional records linked in the registry and evidence log |
| Task branch | `work/sasha/historical-baseline-taxonomy` |
| Scope | `research/historical-baseline/`; registry, extraction plans, documentation and two additional regional topics |
| Language instruction | The user explicitly requested English-only research deliverables; this task-specific instruction takes precedence over default bilingual production for these new tables and guides |
| Human review | Pending; Alexander is the task owner. No coauthor approval or claim review is represented as completed |
| Substantive human edits | None recorded in this AI-produced pass |
| Canon status | Research planning only; no fictional canon decision or jointly approved historical baseline |
| Limits | Full source texts not systematically reviewed; catalogue checks, collection routes, unresolved rights and depth gaps are explicitly labelled |

Repository-wide validation has five pre-existing missing-front-matter errors in project-management planning drafts outside this task. Catalogue validation is independent and does not suppress those failures. The final handoff reports the checks actually run.
