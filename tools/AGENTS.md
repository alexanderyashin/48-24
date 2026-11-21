# Инструменты: контекст для помощника / Tooling assistant context

## Русский

Область: `tools/` и вложенные папки. Это дополнение к [корневому AGENTS.md](../AGENTS.md); его требования и действующие политики сохраняются. Прочитайте [README](README.md), [описание проверок](../studio/repository-checks.md), [структуру](../studio/structure.json) и текущие тесты затрагиваемого поведения.

- Здесь сопровождение репозитория. Игровая логика и производственные прототипы относятся к `products/video-game`.
- Сохраняйте защитные свойства валидатора, сравнение с базой, ограничения путей и проверку прав. Исправляйте причину ошибки в пределах задачи; не удаляйте проверку ради зелёного результата.
- Навигация читает фактические файлы и метаданные. Генератор меняет только документированные производные файлы и помеченные блоки; авторский текст, статусы, лицензии и структура не переписываются автоматически.
- Для изменения инструмента проверьте полезное поведение и ошибки: недопустимые пути, несвежие данные, сохранность текста, повторный запуск. Запустите `python tools/validate_repo.py` и `python -m unittest discover -s tools/tests -v` из корня; для сравнения используйте реальный полный SHA базы.
- Объясняйте ограничения проверки. Успешный поиск, тест или CI не доказывает историческую истину, права или согласие соавтора.

## English

Scope: `tools/` and descendants. This supplements the [root AGENTS.md](../AGENTS.md); its requirements and authoritative policies still apply. Read this area's [README](README.md), [check documentation](../studio/repository-checks.md), [structure](../studio/structure.json) and relevant tests.

- Repository maintenance belongs here; game logic and production prototypes belong in `products/video-game`.
- Preserve validator protections, base comparisons, path constraints and rights checks. Fix the cause of failure within scope rather than removing the check.
- Navigation reads actual files and metadata. Generation changes only documented derived files and marked blocks; it must preserve authored prose, statuses, licenses and structure.
- Test meaningful behavior and failure cases, including unsafe paths, stale data, prose preservation and repeat runs. Run `python tools/validate_repo.py` and `python -m unittest discover -s tools/tests -v` from the root; use the actual full base SHA for comparison.
- State check limitations. Search, tests and CI do not establish historical truth, rights or human consent.
