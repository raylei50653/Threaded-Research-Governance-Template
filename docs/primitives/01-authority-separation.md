# 01 · Authority separation

> **Invariant.** Writes flow upward only, and only through an acceptance event.
> Expectation and execution carry no authority.

---

## The bands

```text
band              holds                          lifetime      may write to
────────────────────────────────────────────────────────────────────────────
accepted state    what is true                   slow          —
intent            what we chose to change        per charter   state (via acceptance)
expectation       where we think it will land    disposable    nothing
execution         what we are currently trying   disposable    nothing
acceptance        what was adjudicated           event         state
```

Read as a sequence of non-identities:

```text
what is true      ≠  what we intend
what we intend    ≠  what we expect
what we expect    ≠  what we are currently trying
what we tried     ≠  what was accepted
```

Each `≠` is a place where a real system silently collapses the two sides.

## Cardinality belongs to the intent band

At most one **decision-changing** charter may be open per owner. That is the whole
constraint. Probes, backfill, engineering follow-up and documentation work are execution
and are unbounded.

$$\text{constrain decision concurrency, not execution concurrency}$$

The reason the bound exists at all is that two open decision lines produce a state the
registry cannot represent: two owners, each believing their line is the one that will be
accepted, both writing back. The bound is not about focus or productivity. It is about
keeping the acceptance event unambiguous.

## Failure mode: epistemic leakage

```text
session n      "next we will verify X"          expectation
session n+3    "assuming X, we now try Y"       expectation, load-bearing
session n+9    "we know X"                      state
```

Nothing adjudicated X. The drift is invisible because each step is a reasonable reading of
the previous one.

This is the characteristic failure of **agent-assisted** work specifically. A human
re-reading their own notes usually retains the memory that X was never checked. An agent
re-reading the same notes has only the text — and a planning note and a finding are the
same shape of document unless the structure makes them different objects.

The structural fix is not better writing. It is that the expectation band must live in a
document the state band cannot read, with a **discard condition** attached: the lease says
in advance what would end it.

## Observed instance · **V**

[`claim_state_registry.md`](https://github.com/raylei50653/saccade/blob/main/docs/research/contracts/claim_state_registry.md)
(2026-07-12) states the band table and the prohibition directly: the registry must not
record expected or hoped-for state, must not record a running probe, and must not update
its transition timestamp merely because work started or stopped. Only an owner accepting a
state change writes back.

The cardinality narrowing arrived with
[PR #151](https://github.com/raylei50653/saccade/commit/7010f4d5) (2026-07-13) —
see [retracted/02](../evolution/retracted/02-uniform-wip-1.md).

## What this does not require

- **Not five files.** It requires five *authorities*. They may share a file if the file
  makes the bands structurally distinct and the write rules are enforceable.
- **Not a registry with a YAML schema.** That is one realization. The invariant is that
  accepted state has exactly one owner and that the owner is not the planning surface.
- **Not "WIP = 1".** That is the rule's literal form in one codebase. The invariant is the
  cardinality bound on the intent band.
- **Not a prohibition on planning.** Expectation is a legitimate, useful band. It is
  required to be *disposable* and *unreadable by state*, not absent.
