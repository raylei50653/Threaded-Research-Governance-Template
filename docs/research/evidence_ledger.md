# Evidence Ledger

**Purpose:** single table for **citable** decision-layer / baseline results used in
README, PRs, and technical report drafting.  
**Rule:** every row must name **date, commit (or frozen tag), preset, protocol notes,
and source doc**. Prefer linking over re-copying long tables.

Update when a new **decision-relevant** or **baseline** run lands. Do not dump
every probe; this is a ledger, not a lab notebook.

**Doc home contract:** [../ownership/doc_structure_contract.md](../ownership/doc_structure_contract.md) C5.

---

## Protocol defaults (unless a row says otherwise)

| Item | Default |
|:--|:--|
| Benchmark / suite | `<your-suite>` |
| Preset | `<baseline-preset>` |
| Metrics | `<metric-1>` / `<metric-2>` / … |
| Host notes | record host / GPU when claiming throughput |

Noise floor guidance for decision knobs: define your own Δ-metric ≈ noise threshold
and stick to it in conclusions.

---

## Ledger

| Date | Commit / tag | Preset | metric-1 | metric-2 | Conclusion | Source |
|:--|:--|:--|--:|--:|:--|:--|
| YYYY-MM-DD | `<sha>` | `<baseline-preset>` | — | — | Headline baseline (example row — replace) | [docs/TODO.md](../TODO.md) |

---

## Decision outcomes (not raw metrics)

| Date | Topic | Decision | Source |
|:--|:--|:--|:--|
| YYYY-MM-DD | example | keep / reject / default-off | link research note |

---

## How to add a row

```text
1. Run with pinned SHA, preset, protocol flags.
2. Record host/GPU when relevant.
3. Fill metrics from the official OVERALL (or named aggregate).
4. One-sentence conclusion (what decision it supports).
5. Link source markdown (or PR); prefer not pasting only into chat.
```

**Do not** promote chat-only numbers. Research notes may hold probes; this ledger
holds what others may **cite**.
