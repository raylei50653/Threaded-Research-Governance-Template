# In flight: governance coupled to development

**Status:** open · **Grade:** O ·
**Artifact:** [Issue #334](https://github.com/raylei50653/saccade/issues/334)
(opened 2026-09-05)

> Not a retraction yet. A coupling identified, with a proposed direction and no
> adjudication. Listed with the retractions because it is the same *kind* of finding: a
> primitive that is individually correct and collectively wrong.

---

## What happened

A commit on a feature branch added explicit postprocessing order and stage diagnostics.
Single-stage compatibility was verified. `pre-push` failed on two conditions:

1. a historical **runtime-identity publication** was stale, and
2. a whole-file **math-model source attestation** was stale.

The change claimed no inheritance of prior evidence. It was blocked anyway.

## Why this is a governance failure and not a checker bug

Each check is defensible on its own. Together they answer three different questions through
one exit code:

| question | when it should be strict |
|:--|:--|
| **Development validity** — do the tests pass, is the config consistent? | always |
| **Evidence applicability** — may this implementation inherit that evidence? | only when evidence is being consumed as current |
| **Publication completeness** — is the source/config/input/environment/probe binding whole? | only when publishing or promoting |

A source change that consumes no evidence was made to satisfy publication-level maintenance
before it could proceed. That is not conservatism; it is a category error with a false
sense of safety attached, because the check that *did* fire was not the check that protects
anything about this change.

The recovery path had the same shape: producing fresh coordinates required current
coordinates, so the gate that detected staleness could not be satisfied without passing
itself.

## The abstraction

$$\boxed{\text{Development validity} \neq \text{Evidence applicability} \neq \text{Publication completeness}}$$

With the asymmetry that keeps it safe:

- Ordinary development that consumes nothing must not require publication maintenance.
- Attempts to **consume** stale evidence, or to claim current attestation falsely, must
  still **fail closed**.
- "New implementation, not yet attested" must be **representable**, rather than forcing a
  choice between overwriting a complete publication with an incomplete one and being
  blocked.

## Why this belongs in the artifact

The claim this repository makes is not that these primitives compose cleanly. It is that
they are the right primitives — including the part where combining them produces coupling
failures that only appear under sustained load, in a repository large enough to have both
historical publications and ordinary daily commits.

An open issue supports that claim better than a resolution would. A resolved issue shows a
fix. An open one shows the failure mode is real, was found from the inside, and is hard.

→ [primitive 4: transition admissibility](../../primitives/04-transition-admissibility.md)
