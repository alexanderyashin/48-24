---
id: "PM-DECISION-LOG-001"
title: "Решения / Decision Log"
status: "draft"
version: "0.1.0"
owner: "alexanderyashin"
reviewers: []
updated: "2026-11-19"
language: "ru-en"
source: "Existing project log at 23d18f172cfee87129695c082f4846c1a00734e6"
ai_assistance: "ChatGPT: technical addition of required metadata only; historical body preserved; human review pending."
---

# Решения / Decision Log

## Русский

Это **указатель рабочих решений**, а не самостоятельный реестр утверждённого канона. Исторические исходные положения находятся в [decisions.csv](../../../../studio/registers/decisions.csv), реальные согласования двух соавторов — в [approvals](../../../../studio/approvals/README.md).

| ID | Рабочее решение | Статус | Основание / evidence |
| --- | --- | --- | --- |
| PM-D001 | Новые материалы и технические каталоги записывать непосредственно в `main` по указанию владельца | agreed-for-work | [workflow](../../../../studio/WORKFLOW.md); текущая сессия 2026-11-19 |
| PM-D002 | Для объектов разделять исторический REF, объект мира OBJ и художественный ART | implemented | [OBJECT_STANDARD](../../../../studio/OBJECT_STANDARD.md) |
| PM-D003 | Ввести L0–L3 готовности 3D и P0–P2 физической достоверности | implemented | [3D gates](../../../../studio/3D_READINESS_GATES.md), [physics governance](../../../../studio/PHYSICS_GOVERNANCE.md) |
| PM-D004 | Использовать типизированный JSON-контракт и профили адаптеров вместо предположения о прямом импорте Markdown в движок | implemented-as-documentation | [engine contract](../../../../studio/ENGINE_DATA_CONTRACT.md) |
| PM-D005 | Валидатор репозитория не запускать до конца текущей сессии | agreed-for-work | распоряжение владельца в текущей сессии |
| PM-D006 | Создать единый журнал проектной документации с решениями, вопросами, работой и дорожной картой | implemented | [этот раздел](README.md); распоряжение владельца в текущей сессии |

Ни одна строка не утверждает выбор игрового движка, готовность адаптера или канонизацию. / No entry claims an engine selection, a working adapter or canon approval.

## English

This is a navigational summary of **working decisions**, not the source of creative canon approvals. Statuses distinguish instructions, implemented documentation and verified deliverables. Refer to the linked authoritative records for evidence.
