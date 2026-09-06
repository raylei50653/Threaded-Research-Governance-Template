# 05 · Projection

> **Invariant.** A projection must never become an authority.

**Status: distilled correction.** Unlike the other four, this primitive is stated *stricter
than the practice it came from*. The reference codebase still runs hand-written navigation
projections; what it enforces is the three conditions below, not the top tier. Read this as
where the evidence points, not as a transcription of what a production repo does.

---

## The three conditions, then the ranking

Non-negotiable, for every summarizing surface:

```text
1. it owns nothing            no fact has its only home here
2. the owner wins             on conflict, the fact owner is right by construction
3. it says which it is        a projection that does not declare itself will be read as an owner
```

Given those, the forms are **ranked, not binary**:

| tier | form | drift risk |
|:--|:--|:--|
| **1** | **generated** — derived from the owners on demand | none; there is no stored copy |
| **2** | **mechanically reconciled** — hand-written, equality with the owner checked | bounded by what the checker covers |
| **3** | **link-only** — carries no content | none; nothing to drift |

Tier 2 is the honest middle, and the reason the primitive is a ranking: some navigation
surfaces are genuinely easier to write than to generate, and a checked hand-written page is
not the same object as an unchecked one. What is never acceptable is tier 2 *without* the
check — that is tier 4, and tier 4 is the failure mode below.

---

## Why unchecked hand-written status pages are worse than none

A hand-written progress page is correct on the day it is written and wrong thereafter. That
alone would make it merely useless. What makes it harmful is that it is *structured*: it
reads as authoritative, it is the easiest thing to find, and a reader — human or agent —
arriving cold will trust it over the fact owners it silently diverged from.

So the answer to "we should write a summary of where things stand" is: yes — and then pick
a tier and pay for it. Generate it, or check it against the owners, or reduce it to links.
A page that says *"the current baseline lives here →"* is permanently correct and costs
nothing to maintain, which is why tier 3 is a legitimate destination and not a consolation
prize.

## Corollary: thin entrypoints

The top-level entry document is a **router**: level → document pack → action. It composes
links.

Entry documents bloat by a predictable mechanism. Each individual addition is justified —
someone needed that fact and could not find it. But each absorbed fact becomes a copy, and
after enough of them the entry document is an encyclopedia that is also a second truth, and
the fastest way to be wrong about the project is to read it.

The discipline is that "someone could not find X" is a routing failure. The repair is a
better link, not a copy.

## Corollary: navigation is not evidence

A continuity artifact — the card that answers *"where were we, what is next"* — is
legitimate and, for long-running agent-assisted work, close to essential. It has one hard
boundary:

```text
may hold     open question, next step, discard condition, links to the real homes
must not     result tables, accepted numbers, conclusions
```

The moment it carries a result it has become a second truth, and a particularly durable one,
because it is the document people actually open.

## Corollary: derived values must be labelled derived

A cached derivation — "given the current state and rules, these units are admissible" — is
useful and is not a fact. It goes stale when the rules change, when a dependency completes,
or when an adjudication updates.

So it carries what it was derived from and when it was last reviewed, and it is marked as
derived. A derived value that has lost its provenance is indistinguishable from a fact, and
will be treated as one.

## Observed instances

**The gap this primitive states beyond.** The reference codebase declares the three
conditions — projections own no terminal, evidence or WIP state; the owner wins on conflict;
some projection equalities have checkers — and still runs manual navigation surfaces. So the
conditions are **V**; the tier ranking is a correction this model makes on top of them, and
is not claimed to have been proven in production.

**Retracted · V.** The `*.dispatch.yaml` sidecars restated branch, merge base, head SHA and
CI status — all owned authoritatively by GitHub. Withdrawn 2026-07-10;
see [failures/01](../evolution/failures/01-dispatch-sidecars-as-execution-authority.md).

**Diagnosed · V.** The only one-page progress snapshot in the lab was hand-written and, at
the time of the 2026-09-01 inventory, nearly two months stale. ADR 021's conclusion was not
"update it" but that the reporting surface **must be generated** from the existing fact
owners — because state already had an owner, and any second hand-written page would drift
by construction.

## What this does not require

- **Not that generation exist before the discipline does.** Links first. Generation when it
  is worth building. Tier 3 today beats tier 4 forever.
- **Not that summaries be forbidden.** Generated summaries are the *goal*. The prohibition
  is on a stored restatement that nothing reconciles.
- **Not that hand-writing is disqualifying.** A hand-written page with a checker is tier 2
  and is a legitimate steady state. A hand-written page without one is the failure mode.
- **Not a single entry point.** Several routers are fine. Several *copies of the same fact*
  are not.
