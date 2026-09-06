# 02 · Identity

> **Invariant.** Anything that may later be cited carries an identity written **before the
> first result byte**. Provenance reconstructed afterwards is not production provenance.

---

## What an identity contains

```text
commit          which source produced this
dirty state     was the tree clean — recorded, not assumed
preset          which configuration
dataset         which inputs
host            which machine
cmdline         the invocation, verbatim
producer        which script or entry point
claims          which decision objects this run is intended to support
```

The last field is the one usually missing and the one that makes the rest useful. Without
it, an artifact can be traced backward to its cause but never forward to its consequence —
so nothing can answer *"if I delete this, what claim loses its support?"*

## Why "before the first byte" is the whole rule

A manifest generated after a run completes is assembled from whatever the environment
still reports. It is a **plausible reconstruction**, and the difference between that and a
binding is invisible downstream: both are a JSON file next to some results.

That invisibility is the reason the ordering has to be structural rather than a convention.
Once reconstruction is permitted anywhere, no consumer can tell which manifests were
recorded and which were inferred, so none of them can be relied on.

Writing first also makes the check **fail-closed** in the useful direction: a run that
crashes before producing output still leaves a manifest saying what was attempted, which is
exactly the case where reconstruction is impossible.

## Failure mode: the unreferenceable, undeletable artifact

An output directory without identity cannot answer either question that matters:

- *Which accepted claim rests on this?* → it cannot be safely **cited**.
- *Is anything still using this?* → it cannot be safely **deleted**.

So it is kept. All of it, forever. And the mechanism is self-reinforcing: the absence of
provenance is precisely what erases the information a cleanup would need, so the longer it
runs the less recoverable it becomes.

Deleting without provenance is not conservative and is not cleanup. It is a bet.

## Observed instance · **V**

Inventory of 2026-09-01, recorded in
[ADR 021 §1.1](https://github.com/raylei50653/saccade/blob/main/docs/decisions/021-asset-provenance-and-progress-reporting.md):

| directory | size | top-level entries | provenance |
|:--|--:|--:|:--|
| `runs/` | 82 G | 229 | none |
| `results/` | 3.1 G | 681 | none |
| `out/` | 1.3 G | 174 | none |
| `output/` | 282 M | 106 | none |
| `scratch/` | 794 M | 42 | none |
| `logs/` | 16 M | 88 | none |

Sampled result directories contained tracking output, FPS summaries and latency profiles —
and no commit SHA, no preset, no config, no host.

The broken link was stated precisely: the evidence ledger cites *documents*, documents cite
*numbers*, and the segment from "which directory and which commit produced this number" was
missing entirely.

> ADR 021 is `proposed`. The measurements are **V**. That the fix landed is not claimed.

## Three identities, not one

They are separable and are commonly confused:

| identity | answers | stable across |
|:--|:--|:--|
| **run** | which execution | — (unique per run) |
| **artifact** | which bytes | copies, moves |
| **implementation** | which behavior | reruns of the same code |

A claim binds to *implementation* identity; an artifact binds to *run* identity. Conflating
them produces the error where re-running the same code appears to invalidate a claim, or
where changing the code appears not to.

## What this does not require

- **Not a hashing framework.** Recording the commit, preset, host and cmdline covers most
  of the value. Semantic-equivalence hashing is a much larger project and solves a
  different problem.
- **Not that byte changes imply semantic changes.** A version identity is useful precisely
  because it is cheap; it is not evidence that behavior changed. Treating it as such is how
  identity checking turns into [gate coupling](04-transition-admissibility.md).
- **Not immediate cleanup.** Identity is the *precondition* for disposal, not disposal.
  Give things names first; decide what to remove after.
