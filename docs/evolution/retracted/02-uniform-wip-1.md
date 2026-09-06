# Retracted: uniform WIP = 1

**Withdrawn:** 2026-07-13 · **Grade:** V ·
**Artifact:** [PR #151 / `7010f4d5`](https://github.com/raylei50653/saccade/commit/7010f4d5)

---

## The design

> At most one concurrent active goal per module owner.

One line in each module's task file. Anything in flight consumed the slot.

This is the rule as this repository froze it on 2026-07-10. The lab revised it three days
later.

## Why it was withdrawn

The rule was applied to **execution**, and it meant to apply to **decisions**. Applied
uniformly, it made ordinary work contend for a slot that exists to protect something else:

```text
fixing a typo in a doc          consumed WIP
adding one regression test      consumed WIP
running a throwaway probe       consumed WIP
backfilling a dataset           consumed WIP
```

None of those can change decision state. Blocking them bought nothing and cost the owner a
choice between working and staying compliant — the reliable precondition for a governance
rule being quietly ignored, which is worse than not having it.

## The correction

From the diff:

```diff
- | O0 WIP=1 | At most one concurrent active goal per module owner |
+ | O0 WIP=1 | At most one decision-changing mainline charter per module owner;
+             probe / evidence / close may be non-WIP |
```

```diff
- | TODO.md | WIP=1 lock: sole active one-liner + link |
+ | TODO.md | WIP=1 lock: one decision-changing charter one-liner + link |
+           | must not hold: expected state, probe details, ... |
```

The same commit introduced the band separation that became
[primitive 1](../../primitives/01-authority-separation.md), including the rule that an
expected-state lease is disposable and is never written back as accepted state.

## What generalizes

$$\boxed{\text{constrain decision concurrency, not execution concurrency}}$$

The invariant is not *"the task file may contain one line."* It is:

> **At most one authority may change decision state at a time.**

Everything else may run concurrently, subject to one condition: it must not quietly become
a second decision line. That condition is what the charter marker is for — the marker is not
a status badge, it is a claim to the decision slot.

## Note on this repository

v1 of this repository (2026-07-10) states the withdrawn form of the rule, and
[`reference-realization/`](../../../reference-realization/) preserves it that way
deliberately. It is dated, it is what was distilled at the time, and rewriting it to match
the later model would erase the only concrete evidence that the model moved.
