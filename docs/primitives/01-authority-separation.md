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

> **At most one active decision authority per declared decision scope.**

This is an **exclusive-writer** rule, not a work-in-progress limit. Probes, backfill,
engineering follow-up and documentation work are execution and are unbounded.

$$\text{constrain decision concurrency, not execution concurrency}$$

The bound exists because two open decision lines over the same scope produce a state the
registry cannot represent: two authorities, each believing their line is the one that will
be accepted, both writing back. It is not about focus or productivity. It is about keeping
the acceptance event unambiguous.

### Declaring the scope is part of adopting this

The invariant is silent on how coarse the scope is, and it has to be — that is a property
of the state, not of the method. One owner holding two genuinely independent decision
objects can safely run two decision lines; one owner holding two lines that could both
write the same object cannot, no matter how disciplined they are.

```text
scope = the set of decision-state slots a single acceptance event may write
```

| scope choice | one writer per… | fits |
|:--|:--|:--|
| module owner | module | few coupled subsystems; the reference realization's choice |
| decision object | registry object | many independent claims under one owner |
| substrate | coordinate system | claims migrating between offline and runtime |

The reference realization picks `scope = module owner` and therefore states the rule as
"one charter per module". That is **policy**. Picking a finer scope is not a relaxation of
the invariant; it is a different, equally valid declaration of what the slots are.

What is *not* valid is leaving it undeclared — then "one at a time" has no referent, and
the rule silently becomes whatever the current file layout happens to enforce.

> **Provenance note.** The observed correction
> ([PR #151](https://github.com/raylei50653/saccade/commit/7010f4d5)) says *per module
> owner*. Generalizing that to *per declared scope* is this model's step, not a
> transcription — the exclusivity is what the acceptance event requires; "module" is one
> way to draw the boundary.

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

[`claim_state_registry.md`](https://github.com/raylei50653/saccade/blob/d1b32b588fe1a1f49989d9ffff1d907685f148be/docs/research/contracts/claim_state_registry.md)
(2026-07-12) states the band table and the prohibition directly: the registry must not
record expected or hoped-for state, must not record a running probe, and must not update
its transition timestamp merely because work started or stopped. Only an owner accepting a
state change writes back.

The cardinality narrowing arrived with
[PR #151](https://github.com/raylei50653/saccade/commit/7010f4d5) (2026-07-13) —
see [failures/02](../evolution/failures/02-uniform-wip-1.md).

## What this does not require

- **Not five files.** It requires five *authorities*. They may share a file if the file
  makes the bands structurally distinct and the write rules are enforceable.
- **Not a registry with a YAML schema.** That is one realization. The invariant is that
  accepted state has exactly one owner and that the owner is not the planning surface.
- **Not "WIP = 1 per module".** That is the rule under one scope declaration. The invariant
  is exclusivity per scope; the scope is yours to choose and yours to state.
- **Not a prohibition on planning.** Expectation is a legitimate, useful band. It is
  required to be *disposable* and *unreadable by state*, not absent.
