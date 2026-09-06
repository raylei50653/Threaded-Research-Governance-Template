# 02 · Identity

> **Invariant.** Anything that may later be cited carries an identity written **before the
> first result byte**. Provenance reconstructed afterwards is not production provenance.

---

## What an identity contains

Two groups, with different obligations:

```text
── producer identity ─────────────── required, before the first result byte ──
commit          which source produced this
dirty state     was the tree clean — recorded, not assumed
preset          which configuration
dataset         which inputs
host            which machine
cmdline         the invocation, verbatim
producer        which entry point, from a closed vocabulary
started_at      when

── claim linkage ────────────────── optional at creation, required before citation ──
claims          which decision objects this run supports — ids only, never verdicts
```

**Claim linkage cannot be required at creation, and requiring it would be a bug.** An
exploratory run does not know what it will end up supporting; demanding the answer up front
either forces a guess or forces the researcher to decide the conclusion before running. The
obligation belongs at the other end of the chain: nothing may be **cited** without a claim
link, which is exactly where [primitive 03](03-evidence-promotion.md) already puts an
explicit act.

The field carries ids and nothing else. A manifest that carries a verdict has become a
second truth about the result it merely produced.

## Why "before the first byte" is the whole rule

A manifest generated after a run completes is assembled from whatever the environment still
reports. It is a **plausible reconstruction**, and the difference between that and a binding
is invisible downstream: both are a JSON file next to some results.

That invisibility is the reason the ordering has to be structural rather than a convention.
Once reconstruction is permitted anywhere and looks the same, no consumer can tell which
manifests were recorded and which were inferred — so downstream extends the trust the
recorded ones earned to all of them, and none can be relied on.

### The fix is labelling, not prohibition

Reconstruction is sometimes the only option — an artifact that predates the discipline still
needs a name. So the mode goes **in the file**, and the required set differs by mode:

| mode | required | meaning |
|:--|:--|:--|
| `production` | the full producer identity | written by the run itself, before the first result byte |
| `reconstructed` | commit + **named source for every field** | assembled afterwards; fields with no named source are *absent*, not inferred |

The asymmetry is the point. A reconstructed manifest may not carry a field it cannot source,
and may not carry one whose value was derived by a rule — a closed-vocabulary field like
`producer` is the clearest case, because only the run knows which term applies, and
back-inferring it dresses an inference as an observed fact.

Observed refinement: this two-mode schema replaced a single-shape manifest in the reference
codebase for exactly this reason
([ADR 021 §2, schema v2](https://github.com/raylei50653/saccade/blob/ef3030c0953171e8719eecd45f8b854972d0cb01/docs/decisions/021-asset-provenance-and-progress-reporting.md)).

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
[ADR 021 §1.1](https://github.com/raylei50653/saccade/blob/ef3030c0953171e8719eecd45f8b854972d0cb01/docs/decisions/021-asset-provenance-and-progress-reporting.md):

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
- **Not claim-first research.** Claim linkage is optional at creation by design. An
  identity discipline that forces you to name the conclusion before the run has stopped
  being provenance and started being a hypothesis lock.
- **Not that byte changes imply semantic changes.** A version identity is useful precisely
  because it is cheap; it is not evidence that behavior changed. Treating it as such is how
  identity checking turns into [gate coupling](04-transition-admissibility.md).
- **Not immediate cleanup.** Identity is the *precondition* for disposal, not disposal.
  Give things names first; decide what to remove after.
