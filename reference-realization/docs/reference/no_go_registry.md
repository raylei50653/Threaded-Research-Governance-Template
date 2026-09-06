# NO-GO Registry

> **Purpose**: decision index for directions that were rejected, parked, or revived.
> This file should answer: **what was this for, what signal was found, and where is
> the evidence?** Do not expand full experiment narratives here.
>
> Module-level writeups remain the source of truth for full measurements.
> Optional long historical appendix: `no_go_registry_details.md` (create if needed).

## How To Use This Registry

- Use this page before opening a new experiment branch. If the same **use case** and
  **signal** already failed, do not repeat it unless the revival condition changed.
- Keep each row short: one use case, one signal verdict, links to evidence.
- If a result has valuable details, put them in a module `research/` document, then link it here.
- A neutral result is not automatically dead. Mark whether the signal is absent,
  blocked by a mechanism, or valid but not actionable.

## Signal Verdicts

| Verdict | Meaning | Revival rule |
|---------|---------|--------------|
| `harmful` | Metrics regress when enabled. | Only retry if the operating point or upstream assumption changes. |
| `no signal` | The proposed signal is near-random or physically unavailable. | Do not retry without a new modality or feature source. |
| `blocked` | Signal exists, but the current mechanism cannot expose it. | Retry only after the blocker is removed. |
| `not actionable` | Signal is measurable, but already dominated by a better proxy or cannot separate gain from harm. | Retry only with a different action point. |
| `cost-bound` | Signal may exist, but expected gain is too small for implementation/runtime cost. | Retry only if cost drops or the target metric changes. |
| `revived` | Former NO-GO that became useful after mechanism redesign. | Keep the old failure mode documented. |

## Registry

| # | Item | Use Case | Signal Verdict | Evidence |
|---|------|----------|----------------|----------|
| <a id="1"></a>1 | _example_ | Replace with a real rejected direction. | `no signal` | link research note |

Delete the example row when you add real entries.

## How to add

```text
1. Close the experiment in a research note (method + numbers + verdict).
2. Add one short row here.
3. Optional: evidence_ledger decision row if the outcome is cited in PRs.
4. Module README GO/NO-GO table: one-line mirror + link.
```
