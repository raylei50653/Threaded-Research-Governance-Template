# Change routing matrix (O1)

**Goal:** review by **objective touched**, not only by file path.  
**Companion:** [README.md](README.md) · [doc_structure_contract.md](doc_structure_contract.md)

If a PR touches multiple objectives, satisfy the **union** of rows. If one of those
objectives is on the same module’s **should-not-own** list, stop and re-scope.

---

## Matrix

| Objective touched | Typical paths | Required checks | Notes |
|:--|:--|:--|:--|
| **RUNTIME** | pipeline, evaluator, hot-path sources | **Smoke** at minimum; full suite if identity/default path | Prefer `<baseline-preset>` |
| **CORRECTNESS** | match / score / lifecycle knobs; metrics emit | Smoke + metric-sensitive suite when metrics can move; unit tests for pure helpers | Cite evidence_ledger if claiming a number |
| **PERF** | graphs, batching, stage timing | Perf smoke / stage profile; do not claim FPS without method | Attribution docs are RESEARCH if no code path change |
| **CONFIG** | presets, inject map, CLI flags | Headline / contract checker if you have one | Headline must not enable NO-GO items |
| **RESEARCH** | `docs/research/*`, ablation reports, default-off probes | **No metric requirement**; **citation / evidence source** required for numbers | Must not flip production defaults in the same PR |
| **BRIDGE** | language bindings, FFI, packing | Build + unit; smoke if API surface changes | ABI renames need migration note |
| **DEBUG** | dumps, diagnostics, env probes | **Default-off**; bit-exact or “no metric delta” when claimed | Prefer env flags over preset defaults |
| **LEGACY** | old presets, shims, compatibility aliases | Smoke on still-supported path; document deprecation | Do not expand LEGACY without owner |

---

## Composite rules

| Situation | Route |
|:--|:--|
| CONFIG + RUNTIME | contracts **and** smoke |
| BRIDGE + RUNTIME | build + smoke |
| RESEARCH + any production default flip | **split PR** — research docs first or behavior second, not both |
| DEBUG probe left default-on | fail review |
| Closed decision-line default change | **not casual O-series**; needs named decision line + evidence |

---

## Suggested command anchors

```bash
# CONFIG / headline contract (if present)
# python scripts/tools/check_headline_contract.py

# RUNTIME / CORRECTNESS smoke (example)
# python scripts/eval/run.py --preset <baseline-preset> --smoke
```

---

## Review checklist (short)

```text
□ Primary objective named in PR description
□ Checks from matrix run (or waived with reason)
□ O0 WIP=1: same module not opening a second active goal
□ No drive-by preset default flip in a “docs” PR
□ Citable numbers have ledger / no_go / report_data home
```
