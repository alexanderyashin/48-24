---
id: PRODUCT-SASHA-PNEUMOTHERMAL-CONTROLS
title: "Пневмотермическое оружие — управление / Pneumothermal weapons — controls"
status: draft
owner: alexanderyashin
updated: 2026-11-20
source: IDEA-SASHA-WEAPONS-FOUNDATION
ai_assistance: "ChatGPT; GPT-6 Astra Pro; drafting and translation"
version: v0-1
reviewers: []
languages: ["ru", "en"]
translation_status: draft-unreviewed
canon_refs: []
related_ids: ["WLD-SASHA-PNEUMOTHERMAL-FAMILY", "OBJ-SASHA-PNEUMOTHERMAL-GL", "OBJ-SASHA-PNEUMOTHERMAL-SR", "ART-SASHA-PNEUMOTHERMAL-GL-BRIEF"]
---

# Управление пневмотермическим оружием / Pneumothermal weapon controls

## Русский

### Статус и границы

Ранняя игровая намётка Александра Яшина, сохранённая по его поручению как **Draft**. Основание — [запись решений](../../../../studio/inbox/idea-sasha-weapons-foundation-v0-1.md). Текст описывает намерение для компьютерной игры; реализация, плейтесты, баланс и согласование соавторов не заявляются. Название «пневмотермическое» рабочее.

База адаптации — [черновик семейства](../../../../world/technology/drafts/weapons-systems/pneumothermal-family-v0-1.md) и [гранатомёт OBJ-SASHA-PNEUMOTHERMAL-GL](../../../../world/technology/drafts/weapons-systems/pneumothermal-grenade-launcher-v0-1.md); утверждённая каноническая база для этой механики пока отсутствует. Игровые кнопки принадлежат этой карточке, свойства предмета — OBJ.

### Заданные действия и индикация

| Элемент | Рабочее решение |
| --- | --- |
| Правая кнопка мыши, ПКМ | Нагнетание давления в камеру сгорания |
| Левая кнопка мыши, ЛКМ | Поджиг |
| Первый индикатор | Давление газа в баллоне |
| Второй индикатор | Давление в камере сгорания |

Это основа узнаваемого взаимодействия с семейством, обсуждённая на примере гранатомёта. Два индикатора показывают разные состояния системы; конкретные шкалы, величины и анимация ещё не заданы. Изменение силы выстрела относится к замыслу семейства, но зависимость от ввода игрока и игровых значений не специфицирована.

Для гранатомёта задано заряжание через дуло. В исходной терминологии загружаемый элемент назван «метательным зарядом», хотя ранее боеприпас отделён от энергетического обеспечения. Значение термина остаётся открытым; эта запись не задаёт состав загружаемого элемента. Способ заряжания остальных моделей не установлен.

### Открытые вопросы

- ПКМ удерживается или нажимается повторно; как действие прекращается и сохраняется ли подготовленное состояние.
- Управление прицеливанием при занятой ПКМ, в том числе у [дорогой снайперской намётки](../../../../world/technology/drafts/weapons-systems/pneumothermal-precision-rifle-v0-1.md).
- Команда и анимация перезарядки; сброс, отмена действия и переключение оружия.
- Тайминги, расход игровых ресурсов, численные шкалы, баланс и условия доступности действий.
- Игровое выражение зависимости гранатомёта от погоды и ухода: состояния, обратная связь, эффекты отказа. Его ограничения не переносятся автоматически на всю линейку.
- Звук, визуальные эффекты, расположение индикаторов и поддержка других устройств ввода.

Ни для одного пункта не выбран вариант по умолчанию. Испытаний нет; движок и программная реализация не выбраны. Следующая редакция должна закрывать вопросы отдельными решениями, сохраняя связь с OBJ и [арт-брифом](../../../../art/props/drafts/weapons/pneumothermal-grenade-launcher-brief-v0-1.md). Порядок фиксации — [черновой стандарт](../../../../studio/WEAPONS_DRAFT_STANDARD.md).

## English

### Status and scope

An early gameplay outline by Alexander Yashin, recorded at his request as **Draft**. Its source is the [decision capture](../../../../studio/inbox/idea-sasha-weapons-foundation-v0-1.md). This text records an intention for the video game; implementation, playtesting, balance, and coauthor approval are not claimed. “Pneumothermal” is a working name.

The adaptation baseline is the [family draft](../../../../world/technology/drafts/weapons-systems/pneumothermal-family-v0-1.md) and [grenade launcher OBJ-SASHA-PNEUMOTHERMAL-GL](../../../../world/technology/drafts/weapons-systems/pneumothermal-grenade-launcher-v0-1.md); no approved canon baseline for this mechanic is available yet. Input bindings belong in this record; object properties belong in the OBJ.

### Specified actions and indicators

| Element | Working decision |
| --- | --- |
| Right mouse button, RMB | Build pressure in the combustion chamber |
| Left mouse button, LMB | Ignition |
| First indicator | Gas pressure in the cylinder |
| Second indicator | Pressure in the combustion chamber |

This is the foundation of the family's recognizable interaction, discussed through the grenade launcher example. The two indicators represent different system states; their scales, values, and animation have not been specified. Variable shot strength belongs to the family concept, but its relationship to player input and game values is unspecified.

Muzzle loading is specified for the grenade launcher. The original terminology calls the loaded element a “метательный заряд” (“propelling charge”), although ammunition was previously separated from the energy supply. The term remains unresolved; this record does not define the loaded element's composition. Loading methods for other models remain unspecified.

### Open questions

- Whether RMB is held or pressed repeatedly; how the action stops and whether a prepared state persists.
- Aiming controls while RMB is assigned, including for the [expensive sniper-rifle outline](../../../../world/technology/drafts/weapons-systems/pneumothermal-precision-rifle-v0-1.md).
- Reload input and animation; reset, cancellation, and weapon switching.
- Timing, game-resource consumption, numeric scales, balance, and action-availability conditions.
- Gameplay expression of the launcher's sensitivity to weather and maintenance: states, feedback, and failure effects. Its limitations do not automatically apply to the whole family.
- Sound, visual effects, indicator placement, and support for other input devices.

No default choice has been made for any of these questions. No tests exist; the engine and software implementation are undecided. Future revisions should resolve questions through separate decisions while maintaining links to the OBJ and [art brief](../../../../art/props/drafts/weapons/pneumothermal-grenade-launcher-brief-v0-1.md). Recording guidance: [draft standard](../../../../studio/WEAPONS_DRAFT_STANDARD.md).
