# report_data — publication / paper assets

Paper-facing evidence and rebuildable tables/figures for **ProjectName**.

This line is **method / publication assets**.  
Decision / production narrative lives under `docs/research/` (e.g. outline + [evidence_ledger](../docs/research/evidence_ledger.md)).  
**Cross-link both; do not overwrite each other.**

Doc homes: [docs/ownership/doc_structure_contract.md](../docs/ownership/doc_structure_contract.md) C5.

---

## Start here

1. [source_map.md](source_map.md) — map research notes → manuscript sections / evidence roles
2. Add `paper_direction.md` / `tables/` / `figures/` as your project needs them

## Evidence classes (suggested)

| Class | Meaning |
|---|---|
| A | Publication-grade held-out result |
| B | Controlled development ablation |
| C | Historical replication evidence |
| D | Negative-result / limitation evidence |

## Rules

- Prefer rebuildable CSV / scripts over screenshots alone.
- Every claim should point back to a research note or ledger row.
- Runtime engineering docs stay under `docs/`; only **paper-facing** extracts live here.
