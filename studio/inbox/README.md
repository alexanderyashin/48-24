# Входящие творческие фрагменты / Creative Inbox

## Русский

Это временный накопитель разрозненных идей проекта 48/24: сюжетных эпизодов, набросков оружия, костюмов, механизмов, диалогов, описаний мест, ссылок на референсы и смешанных концептов. Не требуется заранее выбирать окончательную предметную область.

1. Создайте отдельную Markdown-карточку по [шаблону](../../templates/idea-fragment.md). Сохраните исходную формулировку, автора, дату и ссылку на источник, если он доступен.
2. Назначьте уникальный ID вида `IDEA-0001` (проверьте отсутствие совпадений в репозитории). Укажите типы, темы и предполагаемые связи. Неизвестные связи оставляйте пустыми; не придумывайте факты.
3. Смешанный фрагмент храните в одной карточке. Укажите несколько типов или связанных ID, не копируя материал по разным папкам.
4. После разбора создайте профильные карточки в `world/`, `narrative/`, `art/` или `research/`. В обе стороны укажите ID и относительные ссылки. Исходную карточку оставьте как запись происхождения с состоянием `routed`.
5. Для отвергнутого материала используйте `discarded` с причиной, не удаляя историю. `captured`, `triaged`, `routed`, `discarded` — **состояния обработки входящих**, не статусы художественного канона.
6. Не загружайте в публичный GitHub чужие изображения без прав, приватные переписки и большие бинарные исходники. Для ресурсов применяйте [правила хранения](../ASSET_WORKFLOW.md). Если прав нет, храните только допустимое описание и ссылку.

Карточки в этой папке не становятся каноном автоматически. Для профильных материалов действуют `drafts → canon → archive` и [правила утверждения](../CANON_POLICY.md).

## English

This is a temporary intake area for miscellaneous creative fragments: plot ideas, weapons, costumes, machinery, dialogue, locations, reference links, and mixed concepts. No final domain classification is needed at capture time.

1. Create one Markdown record using the [template](../../templates/idea-fragment.md). Preserve original wording, author, date, and a source link where available.
2. Assign a unique `IDEA-0001`-style ID after checking the repository. Add types, topics, and possible links; do not invent unknown facts.
3. Keep a mixed concept in one record, with multiple types and related IDs rather than duplicate files.
4. On triage, create domain records under `world/`, `narrative/`, `art/`, or `research/`; cross-link both directions. Retain the original intake record as provenance, marked `routed`.
5. Mark rejected intake as `discarded` with a reason. `captured`, `triaged`, `routed`, and `discarded` are intake workflow states, **not canon statuses**.
6. Do not upload unlicensed references, private chats, or large binaries to this public repository. Follow the [asset policy](../ASSET_WORKFLOW.md); retain a permissible description or link when rights are unresolved.

Inbox items are not canon. Domain records still follow `drafts → canon → archive` and the [canon policy](../CANON_POLICY.md).

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../../README.md) › [studio](../README.md) › [inbox](README.md)

[По задаче / By task](../NAVIGATION.md) · [Карта / Map](../REPOSITORY_MAP.md) · [Материалы / Content](../CONTENT_CATALOG.md) · [Шаблоны / Templates](../../templates/README.md)

Пока здесь только инструкция. / This folder currently contains instructions only.

### Подходящие формы / Relevant forms

[idea-fragment.md](../../templates/idea-fragment.md)

Контекст для ИИ / AI reading list: `python tools/navigate.py context studio/inbox`

<!-- NAVIGATION:END -->
