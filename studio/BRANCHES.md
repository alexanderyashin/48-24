# Работа в ветках / Work in branches

[Все открытые PR / Live open PRs](https://github.com/alexanderyashin/48-24/pulls) · [Совместная работа / Collaboration](guides/working-together.md) · [Навигатор / Navigator](NAVIGATION.md)

## Русский

Материал может уже существовать в ветке или PR и ещё не входить в `main`. Перед новой большой задачей проверьте список открытых PR: так проще найти подготовленный текст, избежать повторной работы и заметить пересечение файлов.

Ниже — **снимок обнаруженной работы на 2026-11-21**, а не автоматически обновляемый статус. Текущее состояние смотрите по ссылке PR; ветка может измениться, быть слита или закрыта. Ссылка на черновик не означает его принятие, утверждение новых правил или канонизацию.

| PR | Что находится в работе | Где начать |
| --- | --- | --- |
| [#5 — SPOT и две вики](https://github.com/alexanderyashin/48-24/pull/5) | Предметная декомпозиция SPOT, полные RU/EN пары, вики и расширенный реестр вопросов | Описание PR и входные ссылки на RU/EN wiki |
| [#6 — вооружение](https://github.com/alexanderyashin/48-24/pull/6) | Черновые авторские решения по оружию, объектные карточки, игровой ввод и текстовый арт-бриф | Описание PR и `world/technology/drafts/weapons-systems/` в его ветке |
| [#7 — историческая база](https://github.com/alexanderyashin/48-24/pull/7) | Историческая таксономия, библиография и планы извлечения сведений за 1910–1940 годы | Описание PR и `research/historical-baseline/README.md` в его ветке |

Все три PR при проверке были открыты и отмечены Draft. Их содержимое не включается автоматически в основной каталог: навигатор строится по файлам текущей рабочей копии. Для изучения PR откройте его вкладку файлов или нужную ветку; для продолжения работы сначала сверьте её фактический head, владельца задачи и затронутые пути. Не переносите весь PR в другую задачу только ради одной ссылки или исправления.

При интеграции ветки сохраните ручные инструкции в README, разрешите содержательные конфликты и затем заново выполните `python tools/navigate.py build`, `python tools/navigate.py check` и `python tools/validate_repo.py`. Новый указатель должен отражать уже объединённое дерево. Само пересобирание навигации не согласует новые правила или творческие решения.

## English

Material may already exist in a branch or PR before it appears on `main`. Check [open PRs](https://github.com/alexanderyashin/48-24/pulls) before starting a substantial task to discover prepared work and overlapping files.

This is a **snapshot observed on 2026-11-21**, not a live status feed. Follow each PR for its current state; it may change, merge or close. Linking a draft does not approve its content, proposed rules or creative canon.

| PR | Work in progress | Entry point |
| --- | --- | --- |
| [#5 — SPOT and two wikis](https://github.com/alexanderyashin/48-24/pull/5) | Subject decomposition, complete RU/EN pairs, wikis and an expanded open-question register | PR description and its RU/EN wiki links |
| [#6 — weapons](https://github.com/alexanderyashin/48-24/pull/6) | Draft weapon decisions, object records, game input and written art brief | PR description and its branch's `world/technology/drafts/weapons-systems/` |
| [#7 — historical baseline](https://github.com/alexanderyashin/48-24/pull/7) | Historical taxonomy, bibliography and extraction plans for 1910–1940 | PR description and its branch's `research/historical-baseline/README.md` |

All three were open Draft PRs when checked. Their contents are not automatically included in the main catalogue: navigation indexes the current working tree. Inspect the PR files or branch, then confirm its actual head, task owner and affected paths before continuing work. Do not import an entire PR into another task merely to reuse a link or correction.

When integrating a branch, preserve hand-written README instructions, resolve substantive conflicts and rerun `python tools/navigate.py build`, `python tools/navigate.py check` and `python tools/validate_repo.py`. The rebuilt navigation should describe the combined tree. Rebuilding it does not approve governance changes or creative decisions.
