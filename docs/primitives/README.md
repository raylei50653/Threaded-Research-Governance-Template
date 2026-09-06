# Primitives

Five invariants. Each file states what must hold, what breaks without it, the observed
instance that produced it (with a [provenance grade](../evolution/README.md#provenance-grading)),
and — importantly — what the invariant does *not* require.

| | primitive | one-line invariant |
|:--|:--|:--|
| **01** | [Authority separation](01-authority-separation.md) | Writes flow upward only; one decision authority per declared scope |
| **02** | [Identity](02-identity.md) | Nameable before the first result byte, or not citable |
| **03** | [Evidence promotion](03-evidence-promotion.md) | An observation is citable only after an explicit promotion |
| **04** | [Transition admissibility](04-transition-admissibility.md) | Rules produce a candidate set; selection is a separate act |
| **05** | [Projection](05-projection.md) | A projection never becomes an authority (generated ≻ reconciled ≻ link-only) |

Each file ends with **"what this does not require"**, because the most common way to
misapply this model is to implement the reference realization's *policy* and believe the
invariant has been satisfied.

**01–04 are stated at the strictness the reference codebase runs. 05 is stated stricter** —
a distilled correction rather than a transcription, and its page says so up front.
