# Engine Implementation Profile / Профиль реализации для движка

Fill one profile per **engine + exact version + adapter version**. Linked JSON manifest must pass the project schema. This is an implementation mapping, not a claim of direct native import.

- Object/ART/PHYS IDs:
- Engine / Движок: unreal | unity | godot
- Exact engine version / Версия:
- Adapter ID/version and source path / Адаптер:
- Platform, physics backend, fixed timestep, substeps / Платформа, решатель:
- Units and axes conversion / Конверсия единиц и осей:
- Mesh import format, asset GUID/path / Формат и ID ресурса:
- Material/shader mappings and texture channels / Материалы:
- Collision shapes, layers/masks and filters / Коллизии:
- Rigid body mass, inertia, damping, CCD / Твёрдое тело:
- Joint types and solver-specific settings / Соединения:
- Deformation/cloth/soft body support and fallback / Гибкость:
- Fracture preparation and cluster/fragment support / Разрушение:
- Damage zones → events → state transitions → gameplay functions / Повреждения:
- Mesh/material/VFX/SFX swap mapping / Визуальные последствия:
- Replication/determinism and networking / Сеть:
- Unsupported features and explicit fallback / Неподдерживаемое:
- Import log, reproducible test scene, expected/actual / Тест импорта:
- Reviewer and gate decision / Решение:

**Mapping table**
| Contract JSON path | Native component/property or script | Conversion | Supported? | Test evidence |
| --- | --- | --- | --- | --- |
| `parts[].mass_kg` | pending | pending | pending | pending |
| `parts[].collision` | pending | pending | pending | pending |
| `damage_zones[]` | pending | pending | pending | pending |
| `transitions[]` | pending | pending | pending | pending |
| `fracture` | pending | pending | pending | pending |

**Unreal:** map to Chaos bodies, constraints, Physical Materials, Geometry Collections/fields as supported by selected version. **Unity:** map to Rigidbody/Collider/PhysicMaterial/Joint and explicitly implemented damage/fracture/soft-body systems where not native. **Godot:** map to physics bodies, CollisionShape, PhysicsMaterial, joints and scripts; fracture/tearing require a selected implementation. Do not infer support solely from the existence of a field.
