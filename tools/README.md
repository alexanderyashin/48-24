# Инструменты репозитория / Repository tools

## Русский

Для работы нужны Python 3.11+ и Git; дополнительные библиотеки не требуются. Команды выполняются из корня. Если интерпретатор называется `python3`, используйте это имя вместо `python`.

| Инструмент | Назначение |
| --- | --- |
| [navigate.py](navigate.py) | Выбор места, поиск материалов, список чтения и обновление навигации |
| [validate_repo.py](validate_repo.py) | Проверка структуры, метаданных, ссылок, архива и записей о правах |
| [Тесты](tests/README.md) | Проверка поведения инструментов при их изменении |
| [Справочник проверок](../studio/repository-checks.md) | Форматы, ограничения и причины ошибок |

### Найти место, материал или контекст

```bash
python tools/navigate.py where "сюжет"
python tools/navigate.py where "шрифт"
python tools/navigate.py find ARC025
python tools/navigate.py find "пустоши" --limit 25
python tools/navigate.py context narrative/episodes/drafts
```

`where` сопоставляет запрос со словарём русских и английских синонимов в [маршрутах](../studio/navigation.json). «Сюжет» предложит длинную арку и отдельную историю с объяснением различия. Если маршрут не найден, откройте [путеводитель](../studio/NAVIGATION.md), [карту](../studio/REPOSITORY_MAP.md) или [inbox](../studio/inbox/README.md).

`find` ищет в путях, названиях, ID и тексте. Точное совпадение ID идёт первым, затем могут идти ссылки на него. Настоящие паспорта `*.asset.json` тоже дают ID и статус. Производные указатели и README-блоки исключены из поиска текста. Содержимое файлов больше 128 КиБ по умолчанию пропускается; для поиска внутри SPOT добавьте `--all-text`. Файлы больше 2 МиБ и бинарные файлы по содержимому не индексируются.

`context` выводит порядок чтения: общие правила, инструкции по пути, профильные документы и файлы canon выбранной области. Затем автор/ИИ самостоятельно выбирает связанные ID, вопросы и черновики. Для корня используйте `context .`. Пути пишутся через `/`, включая Windows. Все три команды поддерживают `--json` для нейронок и скриптов:

```bash
python tools/navigate.py find "искомая фраза" --all-text
python tools/navigate.py where scene --json
python tools/navigate.py find CHAR001 --json
python tools/navigate.py context narrative/characters/drafts --json
```

Другой корень задаётся до команды: `python tools/navigate.py --root /path/to/repo find ARC025`. `where`, `find`, `context` и `check` только читают локальную рабочую копию, без интернета. Коды возврата: `0` — успех, `1` — нет совпадений или указатели устарели, `2` — ошибка данных/чтения.

### Обновить указатели

```bash
python tools/navigate.py build
python tools/navigate.py check
python tools/validate_repo.py
```

`build` обновляет [карту](../studio/REPOSITORY_MAP.md), [каталог](../studio/CONTENT_CATALOG.md) и блоки между `<!-- NAVIGATION:START -->` и `<!-- NAVIGATION:END -->` во всех README. При первом запуске блок добавляется в конец; далее заменяется на месте. Ручной текст вне блока сохраняется. Карточки произведений, паспорта ресурсов и подтверждения команда не редактирует.

Перед сборкой завершите параллельные правки README. У новой папки сначала напишите README с назначением; инструмент не сочиняет его. Исправляйте исходные карточки, заголовки README или маршруты, затем пересобирайте указатели. Не редактируйте производные таблицы вручную и не добавляйте их в `.gitignore`. Существующий рукописный файл на месте производной карты/каталога не перезаписывается. Проверьте diff после сборки.

Если вы работаете только в браузере и CI сообщает об устаревшей навигации, передайте свою ветку помощнику или участнику с рабочей копией. Ему нужно выполнить `build`, проверить diff и сохранить обновлённые указатели в той же ветке. CI проверяет результат, но сам не делает commit.

В Git-копии учитываются отслеживаемые и новые неигнорируемые файлы. Для распакованной копии без Git есть резервный обход с исключением служебных кешей, но `.gitignore` тогда не применяется: для проекта используйте Git-копию. Символические ссылки и выход за корень отклоняются.

Каталог показывает Markdown-карточки с front matter и настоящие паспорта `*.asset.json`, сохраняя названия и статусы источников. Примеры из `templates` не считаются материалами. Каталог не заменяет реестры источников, решений, задач и вкладов; включение в каталог или `main` не утверждает канон.

### Добавить маршрут

[navigation.json](../studio/navigation.json) — вспомогательный индекс с `schema_version: 1`. Структуру определяет [structure.json](../studio/structure.json), правила — [AGENTS](../AGENTS.md) и профильные политики. Поля записи `routes`:

| Поле | Значение |
| --- | --- |
| `id` | Уникальный стабильный ID: строчные ASCII-буквы, цифры, дефисы |
| `title`, `description` | Полноценные строки `ru` и `en` |
| `aliases` | Слова и фразы на обоих языках |
| `target` | Существующая папка или документ |
| `templates` | Подходящие формы; допускается пустой список |
| `context` | Профильные документы для чтения |

Все пути относительны корню, без `..`. После правки выполните `build` и `check`. Маршрут не создаёт новую область и не меняет согласование. Если выбор зависит от контекста, объясните это в `description`.

### Проверить инструменты

```bash
python -m unittest discover -s tools/tests -p 'test_*.py' -v
python tools/validate_repo.py --root .
```

Для проверки против базы PR используйте `python tools/validate_repo.py --base FULL_BASE_SHA` с настоящим SHA. Перед проверкой удаления/переноса проиндексируйте намеренные изменения в Git и проверьте diff; не добавляйте случайные локальные файлы. CI проверяет содержимое коммита.

Тесты навигации проверяют сохранение ручного текста, повторяемость сборки, устаревшие указатели, поиск, паспорта ресурсов, два языка, игнорируемые файлы, пути и ссылки. Они не доказывают качество сюжета, согласие людей или права. Изменения проверок и workflows требуют объяснения и сохранения защит; ошибки исправляются по существу, проверку нельзя отключать ради зелёного результата.

## English

Use Python 3.11+ and Git; no third-party packages are required. Run commands from the root. If your interpreter is called `python3`, use that instead of `python`.

| Tool | Purpose |
| --- | --- |
| [navigate.py](navigate.py) | Route tasks, find records, list context and refresh navigation |
| [validate_repo.py](validate_repo.py) | Check structure, metadata, links, archives and rights records |
| [Tests](tests/README.md) | Verify tool behavior when tools change |
| [Check reference](../studio/repository-checks.md) | Formats, limitations and causes of errors |

### Find a destination, record or context

```bash
python tools/navigate.py where "plot"
python tools/navigate.py where "font"
python tools/navigate.py find ARC025
python tools/navigate.py find "wasteland" --limit 25
python tools/navigate.py context narrative/episodes/drafts
```

`where` matches a query against Russian and English synonyms in the [routing index](../studio/navigation.json). “Plot” offers a long arc and a standalone story and explains the difference. If no route matches, open the [hub](../studio/NAVIGATION.md), [map](../studio/REPOSITORY_MAP.md) or [inbox](../studio/inbox/README.md).

`find` searches paths, titles, IDs and text. Exact ID matches come first; references can follow. Real `*.asset.json` sidecars also provide IDs and statuses. Generated indexes and README navigation blocks are excluded from body search. Bodies larger than 128 KiB are skipped by default; add `--all-text` to search inside SPOT. Files over 2 MiB and binary files are not indexed by body text.

`context` lists shared rules, instructions along the path, domain documents and canon files in the chosen area. The author/AI then selects related IDs, questions and drafts. Use `context .` for the root. Write paths with `/`, including on Windows. All three commands support `--json` for AI assistants and scripts:

```bash
python tools/navigate.py find "search phrase" --all-text
python tools/navigate.py where scene --json
python tools/navigate.py find CHAR001 --json
python tools/navigate.py context narrative/characters/drafts --json
```

Set another root before the command: `python tools/navigate.py --root /path/to/repo find ARC025`. `where`, `find`, `context` and `check` only read the local working tree, without network access. Exit codes: `0` success, `1` no matches or stale navigation, `2` input/read error.

### Refresh indexes

```bash
python tools/navigate.py build
python tools/navigate.py check
python tools/validate_repo.py
```

`build` updates the [map](../studio/REPOSITORY_MAP.md), [catalogue](../studio/CONTENT_CATALOG.md), and blocks between `<!-- NAVIGATION:START -->` and `<!-- NAVIGATION:END -->` in every README. The first run appends a block; later runs replace it in place. Manual text outside the block is retained. The command does not edit creative records, asset sidecars or approvals.

Finish concurrent README edits before building. Write a purpose-specific README for each new folder first: the tool does not invent one. Update source records, README titles or routes, then rebuild. Do not hand-edit generated tables or ignore them in `.gitignore`. An existing handwritten file at a generated map/catalogue destination is not overwritten. Inspect the resulting diff.

If you work only in the browser and CI reports stale navigation, hand your branch to an assistant or contributor with a working copy. They should run `build`, inspect the diff and commit the refreshed indexes to the same branch. CI checks the result but does not commit changes automatically.

In Git, inventory includes tracked and new nonignored files. An extracted non-Git copy has a fallback scan excluding tool caches, but `.gitignore` is not interpreted: use a Git copy for project work. Symlinks and paths outside the root are rejected.

The catalogue includes Markdown records with front matter and actual `*.asset.json` sidecars, retaining source titles and statuses. Template examples are excluded. It does not replace source, decision, task or contribution registers; inclusion in the catalogue or `main` does not establish canon.

### Add a route

[navigation.json](../studio/navigation.json) is a helper index with `schema_version: 1`. [structure.json](../studio/structure.json) defines structure; [AGENTS](../AGENTS.md) and domain policies define rules. Each `routes` entry has:

| Field | Meaning |
| --- | --- |
| `id` | Unique stable lowercase ASCII letters, digits and hyphens |
| `title`, `description` | Complete `ru` and `en` strings |
| `aliases` | Words and phrases in both languages |
| `target` | Existing folder or document |
| `templates` | Appropriate forms; an empty list is allowed |
| `context` | Domain documents to read |

All paths are relative to the root without `..`. Run `build` and `check` after editing. A route does not establish a domain or change approval requirements. Explain context-dependent placement in `description`.

### Check tools

```bash
python -m unittest discover -s tools/tests -p 'test_*.py' -v
python tools/validate_repo.py --root .
```

To check against a PR base, use `python tools/validate_repo.py --base FULL_BASE_SHA` with the actual SHA. Before checking deletions or moves, stage intended changes and inspect the diff; avoid adding incidental local files. CI checks committed files.

Navigation tests verify manual-text preservation, repeatable builds, stale indexes, searches, asset sidecars, both languages, ignored files, paths and symlinks. They do not establish story quality, human consent or legal rights. Changes to checks and workflows need an explanation and preserved safeguards; fix the cause rather than disabling a check to obtain a green result.

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../README.md) › [tools](README.md)

[По задаче / By task](../studio/NAVIGATION.md) · [Карта / Map](../studio/REPOSITORY_MAP.md) · [Материалы / Content](../studio/CONTENT_CATALOG.md) · [Шаблоны / Templates](../templates/README.md)

### Подразделы / Subfolders

- [Проверки предохранителей](tests/README.md) — `tests/`.

### Файлы рядом / Files here

- [Инструменты: контекст для помощника / Tooling assistant context](AGENTS.md) — `AGENTS.md`.
- [navigate.py](navigate.py) — `navigate.py`.
- [validate_repo.py](validate_repo.py) — `validate_repo.py`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context tools`

<!-- NAVIGATION:END -->
