# Проверки предохранителей

Здесь находятся автоматические тесты валидатора репозитория. Они создают временный маленький репозиторий и проверяют реальные ошибки: удаление структуры, изменение архивной записи, неподтверждённый канон, несовпадение байтов с одобрением, неизвестные права на арт, сломанные ссылки и непереносимые имена.

Все имена, одобрения и доказательства внутри фикстур — искусственные тестовые данные. Они не являются решениями авторов 48/24.

Запуск из корня:

```bash
python3 -m unittest discover -s tools/tests -p 'test_*.py' -v
```

Новый тест нужен при изменении существенного правила валидатора или исправлении воспроизводимой ошибки. Изменение одного README само по себе не требует нового теста.

<!-- NAVIGATION:START -->
## Навигация / Navigation

> Автоматический указатель; текст раздела выше редактируется вручную. / Generated links; edit the section text above normally.

[Главная / Home](../../README.md) › [tools](../README.md) › [tests](README.md)

[По задаче / By task](../../studio/NAVIGATION.md) · [Карта / Map](../../studio/REPOSITORY_MAP.md) · [Материалы / Content](../../studio/CONTENT_CATALOG.md) · [Шаблоны / Templates](../../templates/README.md)

### Файлы рядом / Files here

- [test_navigate.py](test_navigate.py) — `test_navigate.py`.
- [test_validate_repo.py](test_validate_repo.py) — `test_validate_repo.py`.

Контекст для ИИ / AI reading list: `python tools/navigate.py context tools/tests`

<!-- NAVIGATION:END -->
