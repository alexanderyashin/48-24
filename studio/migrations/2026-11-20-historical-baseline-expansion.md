# Historical baseline — план расширения / Expansion proposal

**Дата / Date:** 2026-11-20
**Инициатор / Task owner:** Alexander (Sasha) — explicitly requested structural expansion
**Ветка / Branch:** `work/sasha/historical-baseline-taxonomy`
**Статус / Status:** prepared for coauthor review; NOT approved or merged

## Цель / Goal

RU: Развернуть в `research/` многоуровневую классификацию исторических справок, изображений, документов, первоисточников и сравнительных сведений за 1910–1940 годы. Не смешивать реальную историю и художественный канон.

EN: Establish a multi-level classification within `research/` for 1910–1940 historical documents, photographs, primary sources, and comparative research without conflating history with fictional canon.

## Изменения путей / Path changes

- **NEW:** `research/historical-baseline/` — 37 domains, 74 thematic groups, 375 leaf topics, bilingual README files, source catalog, and machine-readable taxonomy.
- **UPDATE:** `research/README.md` — one new navigation row.
- **NEW:** this reviewed migration proposal.
- **UNCHANGED:** `research/history/`, `research/visual-references/`, `world/`, `studio/structure.json`, all existing content.
- **Old → new:** none; this is additive, not a move. No legacy links need rewriting.

## Контроль и обратимость / Controls and rollback

RU: Новая структура является организационной полкой, не новым зарегистрированным `content_area` и не новым статусом lifecycle. В этом PR `structure.json` не меняется. Старые пути продолжают работать. Для отмены не сливать PR или удалить исключительно добавленные пути отдельным согласованным изменением, сохранив git-историю. Права на изображения проверяются при наполнении. Если в будущем рубрика будет объявлена самостоятельной зарегистрированной предметной областью — нужен отдельный план и согласование.

EN: This is a nested organizational reference shelf, not a new registered `content_area` or lifecycle. The manifest remains unchanged. Existing links and paths remain valid. Roll back by declining the PR or a later reviewed removal of solely new paths while retaining Git history. Image-rights checks apply upon ingestion. Future promotion to a registered content area requires a separate decision.

## Согласования / Approvals

- Alexander: structural task explicitly requested in chat; this does not imply approval of the final diff.
- Ivan: **pending**. No approval is claimed.

**Handoff:** review taxonomy coverage, naming, routing, rights, link checks, and the final diff; run `python tools/validate_repo.py --base 23d18f172cfee87129695c082f4846c1a00734e6` before merging.
