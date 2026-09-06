# O-series: Ownership / Objective Isolation

**中文：** 模組目標隔離  
**Status:** template scaffold  
**Companion:** [doc_structure_contract.md](doc_structure_contract.md) · [change_routing_matrix.md](change_routing_matrix.md)

---

## Why this exists

Large modules hurt review not only because of LOC, but because **one owner / file
carries multiple competing objectives** at once:

```text
RUNTIME  CORRECTNESS  PERF  CONFIG  RESEARCH  BRIDGE  DEBUG  LEGACY
```

O-series isolates objectives so each module (and, where needed, each hot file)
has **one primary job**, explicit secondaries, and a clear **should-not-own** list.

---

## Phase map

| Phase | Name | Deliverable | Behavior? |
|:--|:--|:--|:--|
| **O0** | Workstream WIP Seal | WIP=1 per module owner | **No** (docs) — [DOC_MAINTENANCE § WIP](../DOC_MAINTENANCE.md) |
| **O1** | Module Objective Map | this directory + routing matrix | **No** (annotate only) |
| **O1.5** | Doc Structure Contract | [doc_structure_contract.md](doc_structure_contract.md) | **No** (homes / indexes / promotion) |
| **O2+** | Ownership notes / extraction | optional, project-specific | Later |

**O0 entry / dashboard:** [DEVELOPMENT.md 模組現狀總覽](../../DEVELOPMENT.md)  
**Dev entry (need levels D0–D4):** [DEVELOPMENT.md](../../DEVELOPMENT.md)

---

## Files in this tree

| File | Role |
|:--|:--|
| [doc_structure_contract.md](doc_structure_contract.md) | **O1.5** write-where / index / promotion / lifecycle |
| [change_routing_matrix.md](change_routing_matrix.md) | Objective touched → required checks |

Optional later (project-specific):

- `objective_template.md` — objective type catalog + card schema
- `module_objective_map.md` — primary / secondary / should-not-own per module
- `extraction_candidates.md` — what to extract later (reasons only)

---

## How to use in review

1. Identify **which objective** the PR primarily serves (use routing matrix).  
2. Require checks from [change_routing_matrix.md](change_routing_matrix.md).  
3. If the PR grows a second objective on the same owner, apply **O0 WIP=1** (park or finish first).  
4. RESEARCH + production default flip → **split PR**.

---

## One-liner

> Module-objective isolation: each module owns **one** primary goal so runtime, perf, research, config, debug, and legacy do not pull the same owner at once.
