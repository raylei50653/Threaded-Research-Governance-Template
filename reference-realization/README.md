# Reference realization — v1, frozen

<!-- frozen: the v1 artifact, 2026-07-10. Do not update it to match the current model. -->

> **Frozen at 2026-07-10.** One workable implementation of [the model](../MODEL.md),
> preserved as it was distilled. It states rules the model has since revised — most
> notably uniform WIP = 1
> ([why it was withdrawn](../docs/evolution/retracted/02-uniform-wip-1.md)). Updating it
> would erase the only concrete evidence that the model moved.
>
> Copy as an overlay: `cp -a reference-realization/. /path/to/your/repo/`
>
> Everything below is the original v1 README, with two links repointed where the
> move broke them (`LICENSE`, and the *Use this template* button). Nothing else changed.

---


**v1 · phase 1 complete** — a copyable docs-as-code governance template for research-heavy engineering repos.  
GitHub **template repository** · public · default branch `main`.

> **One home per fact · thin entrypoints · threaded task cards · explicit evidence promotion**
>
> 面向研究型工程專案的輕量文檔治理模板：單一事實來源、薄入口、連續任務母線、證據升格路徑。

```text
Threaded-Research-Governance-Template v1
= 可複製文檔治理模板
= 已有實際內容（非空殼）
= GitHub template repo
= phase 1 complete
```

Use this when your repo mixes **production code**, **multi-step experiments**, and **citable numbers** — and chat history is not a durable memory.

**Phase 2** (`check_doc_structure.py` and friends) is intentionally **not** here yet. v1 optimizes for:

> Can a user understand how to adopt this in **about five minutes**?

---

## Start here (5-minute adoption)

1. Copy this directory as an overlay (`cp -a reference-realization/. /path/to/your/repo/`) into your project / overlay onto an existing repo.
2. **Rename placeholders** — see [What to edit first](#what-to-edit-first).
3. **Define modules** under `docs/modules/` (rename or delete `module-a/b/c`; copy `_template/` for extras).
4. Keep **module `TODO.md` as WIP-lock only** — one sole active one-liner + links; no task novels.
5. **Create a thread only if** work crosses **≥2 doc homes** or **≥3 steps** (or will produce citable policy / audit).
6. **Promote citable numbers only** through `evidence_ledger` / `report_data` / `no_go_registry` — research notes alone are not citable outside themselves.

Then open [DEVELOPMENT.md](DEVELOPMENT.md) and pick a **D0–D4** level for the next change.

**Copying a module package:**

```bash
cp -a docs/modules/_template docs/modules/<your-module>
# edit README.md + TODO.md titles
# remove research/note_template.md OR replace it with a real note and index that note
# update DEVELOPMENT.md dashboard row + docs/modules/README.md
```

> Global search will still hit `module-a` inside *this* README and other instructional examples — that is expected. Real package paths under `docs/modules/` should not keep those names.

### What to edit first

| Order | File / path | What you change |
|:--|:--|:--|
| 1 | global search | `ProjectName` → your name |
| 2 | global search | `<baseline-preset>` → your default eval / run preset |
| 3 | `docs/modules/` | rename `module-a/b/c` or delete; copy `_template/` for more modules |
| 4 | `docs/TODO.md` | fill **one** baseline row (this is the `current-baseline` fact-owner) |
| 5 | `DEVELOPMENT.md` §4–5 | dashboard module table + hot-path file map + your smoke commands |
| 6 | (optional) | rename `report_data/` → `publication_assets/` if you prefer; update links |

| Placeholder | Meaning | Example |
|:--|:--|:--|
| `ProjectName` | Your project | `MyTracker` |
| `<baseline-preset>` | Default eval / run preset | `mainline_v1` |
| `module-a` / `module-b` / `module-c` | Real subsystem names | `detection`, `policy`, `runtime` |
| `report_data/` | Publication / paper asset home | keep or rename |
| `docs/research/decision-log/` | Closed policy / decision line home | create only when needed |

### Adoption checklist

```text
□ Placeholders renamed (ProjectName, baseline preset)
□ Real modules exist under docs/modules/ (not only examples)
□ Each module has README.md + TODO.md (WIP-lock shape)
□ Baseline has one fact-owner home (docs/TODO.md)
□ First research note indexed from owning README (same PR)
□ Threads only for multi-home / multi-step work
□ No number cited in PR/README/paper without ledger / no_go / report_data
```

Longer contract (after the 5-minute path): [docs/ownership/doc_structure_contract.md](docs/ownership/doc_structure_contract.md).

---

## Three selling points

1. **Thin entrypoint** — start from a task level (D0–D4), not from the whole repo.
2. **Thread cards** — preserve multi-step research context without creating second truths.
3. **Evidence promotion** — research numbers are not citable until promoted to ledger / report assets.

---

## Why this exists

Research engineering repos tend to lose memory in three ways:

1. **Entrypoint bloat** — `DEVELOPMENT.md` / README becomes an encyclopedia.
2. **Second truths** — the same metric appears in TODO, PR body, paper notes, and chat, then drifts.
3. **Context amnesia** — multi-step work has no mother line; every session re-derives “what was next.”

This template keeps a **small fixed topology** so agents and humans can re-enter without rereading the whole tree.

---

## Layout (v1)

```text
Threaded-Research-Governance-Template/
├── DEVELOPMENT.md                 # D0–D4 levels · read/write/verify packs · dashboard
├── docs/
│   ├── README.md                  # writing decision tree
│   ├── DOC_MAINTENANCE.md         # format · WIP=1 · fact-owner
│   ├── TODO.md                    # global WIP + baseline fact-owner
│   ├── ownership/
│   │   ├── README.md
│   │   ├── doc_structure_contract.md   # homes · threads · promotion (O1.5)
│   │   └── change_routing_matrix.md    # objective → checks
│   ├── research/
│   │   ├── README.md
│   │   ├── evidence_ledger.md
│   │   ├── threads/
│   │   │   ├── README.md
│   │   │   └── thread_template.md
│   │   └── eval/
│   │       └── signal_analysis_ledger.md
│   ├── modules/
│   │   └── _template/             # copy this for each module
│   │       ├── README.md
│   │       ├── TODO.md
│   │       └── research/
│   │           └── note_template.md
│   ├── reference/
│   │   └── no_go_registry.md
│   └── archive/
├── report_data/
│   ├── README.md
│   └── source_map.md
└── scripts/tools/                 # phase-2 checkers (planned only)
```

---

## Core loop

```text
pick D-level → open doc pack → change code / write note → verify for that level
```

| Artifact | Role | Must not |
|:--|:--|:--|
| `DEVELOPMENT.md` | Thin entry: level → pack → dashboard mirrors | Become an encyclopedia |
| module `TODO.md` | **WIP lock** (one sole active + links) | Task narrative / metrics dumps |
| `docs/research/threads/` | Continuous-task **navigation** cards | Evidence tables / second truth |
| module or global `research/*.md` | Facts, methods, commands, tables | Act as WIP lock |
| `evidence_ledger` / `no_go` / `report_data` | Promoted formal facts | Chat-only numbers |

---

## Minimal “good first week”

1. Copy `docs/modules/_template/` → `docs/modules/<your-module>/`.
2. Write one D1 research note with `doc-status` / `doc-promotion` markers.
3. Index it from the module README (same PR).
4. If multi-step: open a thread from [`thread_template.md`](docs/research/threads/thread_template.md).
5. If a number will be cited in a PR/README/paper: add a ledger or no_go row.

---

## Phase 2 (later)

Only after the adoption path is stable:

- `scripts/tools/check_doc_structure.py` (warn-only: research note missing from owning README)
- link / stale-path / freshness checkers
- optional `--strict` after index debt is paid

Until then, use the human checklist in [docs/DOC_MAINTENANCE.md](docs/DOC_MAINTENANCE.md).

---

## Design origin

Patterns distilled from a production research-heavy tracking codebase’s docs governance (task levels, WIP=1, thread cards, evidence promotion). This template is **project-agnostic** — no domain metrics or product names baked in.

---

## License

MIT — see [LICENSE](../LICENSE).
