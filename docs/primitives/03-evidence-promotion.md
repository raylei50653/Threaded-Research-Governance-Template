# 03 · Evidence promotion

> **Invariant.** An observation becomes citable only through an explicit promotion into a
> named home. Absent that step, a number exists only inside the document that produced it.

---

## The rule

```text
research note        a number here is true of this note and nothing else
      │
      │  promotion — explicit act, named home, recorded acceptor
      ▼
ledger / registry    citable in a PR, a README, a paper
```

A research note is a complete, honest, useful document. It is simply **not an authority
outside itself**. This is not a quality judgment on the note; it is a statement about
scope. The note records what one investigation found under its own conditions. Promotion is
where someone decides those conditions generalize.

The promotion record must name: what is claimed, which note supports it, who accepted it,
under what limits, and on what date. A promotion with no acceptor is a copy.

## Negative closure is a terminal, not an absence

```text
NOT IDENTIFIABLE            the design cannot separate the effect at any sample size
STRUCTURAL PREMISE FAILED   an assumption the approach requires does not hold
NO SEPARATION               measured, within noise, at the achievable N
NOT PURSUED                 admissible, but decision relevance is zero
```

These are **results**. They took work, they constrain the future, and they are the most
frequently lost category of knowledge in research engineering — because a system that only
records success has nowhere to put them.

The cost of losing them is specific: the same dead end gets re-walked, usually by someone
who has read all the documentation, because nothing durable says it was walked. And the
second traversal is often more expensive than the first, since the obvious approach has
already been eliminated informally and the re-attempt starts from a more elaborate variant.

Note also that `NOT PURSUED` is not failure. A claim can be perfectly admissible and simply
not worth proving — decision relevance is a separate axis from legality
([primitive 4](04-transition-admissibility.md)).

## Failure mode: second truths

The same metric appears in the task list, the PR body, the paper draft and a chat log.
Each copy was correct when written. One gets updated. Now:

- every copy is individually defensible,
- the set is collectively wrong,
- and there is no procedure that finds the inconsistency, because no copy is marked as the
  original.

Review discipline does not fix this — reviewers check whether a number is plausible, not
whether it is the same number as three other places. The only structural fix is that
exactly one location owns each fact and every other mention is a link.

## Observed instance

The promotion discipline is v1 of this model and is preserved in
[`reference-realization/`](../../reference-realization/): the evidence ledger, the NO-GO
registry, and the publication asset home, with the rule that no number appears in a PR,
README or paper without a row in one of them.

What v3 found missing was the segment *beneath* this one — the ledger cited documents and
documents cited numbers, but nothing bound a number to the run that produced it. The chain
is only as strong as its lowest link, which is why [identity](02-identity.md) is a separate
primitive and not a detail of this one.

## What this does not require

- **Not a specific table format.** The invariant is that a home exists and has one owner.
  Columns are local.
- **Not that every number be promoted.** Most should not be. Promotion is for numbers that
  will be *cited*; the filter is the point.
- **Not a review board.** The acceptor may be the same person who wrote the note. What is
  required is that acceptance be a distinct, recorded act — not that it be performed by a
  different party.
