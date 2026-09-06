# 04 · Transition admissibility

> **Invariant.** State plus transition rules produce a **candidate set**. Selecting from it
> is a separate act, owned by the intent band.

---

## `next admissible unit` ≠ `next task`

An object can have two legal successors at once — say, obtaining the transfer evidence a
claim still needs, *or* stopping work on it because its decision relevance has gone to zero.
Both are admissible. Which is worth doing is not something the rules can answer.

A system that collapses the two has not automated judgment. It has replaced *mechanically
climbing a ladder* with *mechanically executing `next_admissible_unit`* — the same
pathology with better vocabulary, and harder to notice because the output now looks
principled.

So the split is:

```text
rules      →  candidate set        "what is legal"       mechanical
intent     →  one selection        "what we will do"     judgment, bounded to one
```

## Blockers must be typed

Two things that both read as "blocked" have opposite orchestration semantics:

| type | meaning | scheduler action |
|:--|:--|:--|
| `inadmissibility` | illegal in the current state | **exclude** — do not queue, do not retry |
| `dependency` | legal, but something must precede it | **expand** — put the dependency in the candidate set |

Untyped, both become "wait", and an inadmissible unit sits in a queue forever looking like
it is making progress. The distinction is what lets a scheduler make progress at all:
dependencies generate work, inadmissibility removes it.

## Evidence type must match the transition layer

A claim about a safety gate and a claim about a ranking score require different *kinds* of
evidence, not merely different thresholds. Retention and coverage evidence does not
establish a ranking claim; margin and top-1 evidence does not establish a safety bound.

When a unit presents evidence of the wrong kind, it is **inadmissible regardless of how
rigorous the statistics are** — and the fix is to change the layer being claimed, not to
strengthen the statistics.

## Substrate does not inherit

Evidence obtained on one substrate does not transfer to another by default. Proven offline
is not thereby proven online; proven on a proxy is not proven on the target.

This must be represented as *state*, not as two separate objects: the same decision object
is accepted at one level on one substrate and unproven on another. Splitting it into two
objects loses the thing you most need to track — that a claim is migrating between
substrates and has not arrived.

**"Authorized" ≠ "admissible."** Permission to proceed is not evidence that proceeding is
legal under the transition rules.

## Failure mode: gate coupling · **O**

Individually correct checks, merged into a single gate, block work that invoked none of
them.

$$\boxed{\text{Development validity} \neq \text{Evidence applicability} \neq \text{Publication completeness}}$$

| question | strict when |
|:--|:--|
| **Development validity** | always — tests, config consistency, regressions |
| **Evidence applicability** | only when prior evidence is being consumed as current |
| **Publication completeness** | only when publishing or promoting |

The asymmetry that keeps it safe: ordinary development that consumes no evidence must not
require publication-level maintenance; attempts to consume stale evidence, or to claim
current attestation falsely, must still **fail closed**.

A second symptom of the same coupling is a **recovery path that requires its own
postcondition**: producing fresh coordinates required current coordinates, so the gate that
detected staleness could not be satisfied without first passing itself.

**Observed:** [Issue #334](https://github.com/raylei50653/saccade/issues/334), opened
2026-09-05, **open**. Direction proposed, not adjudicated. See
[retracted/03](../evolution/retracted/03-governance-coupled-to-development.md).

## What this does not require

- **Not a formal transition system.** Missing rules are a legal state — an object whose
  transition semantics are `unavailable` is representable, and making that explicit is more
  useful than pretending the ladder is complete.
- **Not that every check be separate.** It requires that checks answering different
  questions not share an exit code. Grouping by question is fine; grouping by convenience
  is what produced #334.
- **Not automated selection.** The candidate set may be derived mechanically. The selection
  should not be.
