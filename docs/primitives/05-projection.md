# 05 · Projection

> **Invariant.** Any surface that summarizes state is **generated** from the fact owners or
> contains **only links**. It never restates a fact it does not own.

---

## Why hand-written status pages are worse than none

A hand-written progress page is correct on the day it is written and wrong thereafter. That
alone would make it merely useless. What makes it harmful is that it is *structured*: it
reads as authoritative, it is the easiest thing to find, and a reader — human or agent —
arriving cold will trust it over the fact owners it silently diverged from.

So the answer to "we should write a summary of where things stand" is: yes, and it must be
generated. A projection is a query over the owners, rendered on demand. It has no stored
copy to drift.

If generation is not available, the fallback is a page of links and nothing else. A page
that says *"the current baseline lives here →"* is permanently correct.

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

**Retracted · V.** The `*.dispatch.yaml` sidecars restated branch, merge base, head SHA and
CI status — all owned authoritatively by GitHub. Withdrawn 2026-07-10;
see [retracted/01](../evolution/retracted/01-dispatch-sidecars-as-execution-authority.md).

**Diagnosed · V.** The only one-page progress snapshot in the lab was hand-written and, at
the time of the 2026-09-01 inventory, nearly two months stale. ADR 021's conclusion was not
"update it" but that the reporting surface **must be generated** from the existing fact
owners — because state already had an owner, and any second hand-written page would drift
by construction.

## What this does not require

- **Not that generation exist before the discipline does.** Links first. Generation when it
  is worth building.
- **Not that summaries be forbidden.** Generated summaries are the *goal*. The prohibition
  is on stored restatements.
- **Not a single entry point.** Several routers are fine. Several *copies of the same fact*
  are not.
