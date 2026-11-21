# Звук: контекст для помощника / Audio assistant context

## Русский

Область: `audio/` и вложенные папки. Это дополнение к [корневому AGENTS.md](../AGENTS.md); его требования и действующие политики сохраняются. Прочитайте [README](README.md), README выбранной области и [ASSET_WORKFLOW](../studio/ASSET_WORKFLOW.md).

- Музыкальный замысел и дорожки относятся к `music/drafts`, шумы и атмосферы — к `sound-design/drafts`, голосовые характеристики и записи — к `voices/drafts`.
- Связывайте материал с персонажем, сценой, местом или продуктом по ID. Текст реплики хранится в `narrative/dialogue`, её запись — здесь; используйте ссылку на точную редакцию.
- Указывайте назначение, длительность, формат, версию, происхождение, автора/исполнителя, использованные инструменты и ограничения. Для бинарных ресурсов используйте [паспорт](../templates/asset.example.json).
- Проверяйте права на композицию, запись, исполнение и исходные сэмплы; безопасная ссылка на разрешение не заменяется приватным договором в публичной папке. Генерация и загрузка звука выполняются только в рамках поставленной задачи.
- Состояния `draft/canonical` и пригодность дорожки к выпуску различаются; передача в продукт описана в [руководстве](../studio/guides/assets-and-products.md).

## English

Scope: `audio/` and descendants. This supplements the [root AGENTS.md](../AGENTS.md); its requirements and authoritative policies still apply. Read this area's [README](README.md), the target README and [ASSET_WORKFLOW](../studio/ASSET_WORKFLOW.md).

- Route music to `music/drafts`, effects and ambience to `sound-design/drafts`, and voice descriptions/recordings to `voices/drafts`.
- Link character, scene, location or product IDs. Keep dialogue text in `narrative/dialogue` and reference its exact version from the recording.
- Record purpose, duration, format, version, sources, author/performer, tools and limitations. Give binaries an [asset sidecar](../templates/asset.example.json).
- Check composition, recording, performance and sample rights. Keep private agreements outside this public repository. Generate or upload sound only within the assigned task.
- Creative status and release readiness are distinct; follow the [asset/product guide](../studio/guides/assets-and-products.md) for handoff.
