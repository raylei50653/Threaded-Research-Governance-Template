---
doc-status: active-thread
doc-promotion: navigation-only; not evidence
owner-module: <module-a|module-b|cross|ownership>
created: YYYY-MM-DD
---

# <short title>

> **One-line:** <what is true right now and what is the only next move>

## Status

- Research: `active | closed | parked`
- Online / e2e / production: state clearly (e.g. **blocked**, **default-off**, **not preset**)
- Candidate id (if any): `<id>`

```text
candidate_id: <optional>
  = research_state
  ≠ production preset   # keep inequalities explicit when useful
```

## Current boundary

What is in scope for the next step only. What is frozen. What must not change.

## Read first

1. [canonical research note](../../modules/<m>/research/<note>.md)
2. [related contract / ledger](../evidence_ledger.md)
3. [module TODO](../../modules/<m>/TODO.md)

## Artifacts

- Paths to configs, study dirs, policy json, PRs — **pointers only**
- Ledger / signal ids if any

## Current step

```text
Do exactly one next engineering / analysis step.
Acceptance criteria in the next section.
```

## Acceptance

- [ ] …
- [ ] production default **unchanged** (unless this is a D3 PR with evidence)

## Must not

- Long tables or second evidence home in this card
- Silent reopen of a closed decision line
- Flipping headline preset in a research-only step

## History

| Date | Event |
|:--|:--|
| YYYY-MM-DD | thread opened |
