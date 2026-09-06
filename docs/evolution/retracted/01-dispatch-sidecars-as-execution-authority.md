# Retracted: dispatch sidecars as execution authority

**Withdrawn:** 2026-07-10 · **Grade:** V ·
**Artifact:** [`0c794712`](https://github.com/raylei50653/saccade/commit/0c794712) ·
[current prohibition](https://github.com/raylei50653/saccade/blob/main/DEVELOPMENT.md)

---

## The design

Per-task `*.dispatch.yaml` sidecar files, maintained alongside the work, carrying the
authoritative record of an agent-executed unit:

```text
branch            which branch this unit runs on
ancestor          what it forked from
start-protocol    preconditions and setup
return-packet     what came back
```

The intent was reasonable: give a chat-driven agent workflow a durable, structured handoff
so that a session boundary does not lose the execution context.

## Why it was withdrawn

Every field in that list is a fact that **GitHub already owns authoritatively**. Head and
base branch, merge base, head SHA, changed files, CI status, review findings, update
history — these are not facts the repository needs to record. They are facts the repository
needs to *read*.

The sidecar was therefore a hand-maintained copy of an authoritative source: a second truth
about execution metadata, with all the usual properties. It was correct when written. It
diverged silently. And because it was structured and specific, it read as more authoritative
than the system it was copying.

## The primitive it violated

[**Projection**](../../primitives/05-projection.md) — a surface that summarizes state must
be generated or must link. Never restate.

The corrected split, now stated in the entry document:

| authority | owns |
|:--|:--|
| **GitHub PR metadata** | branch, merge base, head SHA, changed files, CI/test status, review findings, update history |
| **Research documents** | research gate, accepted priors, normative inputs, authorized scope, claim boundaries, acceptance, next-stage authorization |

And the lock that keeps them apart:

> **PR merge ≠ research acceptance.** Engineering-ready ≠ evidence promotion.

## What generalizes

Before building a durable record of execution state, ask which system already owns each
field authoritatively. A handoff artifact should carry **only** what no system owns —
which, for agent workflows, is usually intent and adjudication, not mechanics.

The prohibition is stated in the negative and kept in the entry document, because a
retracted design that leaves no trace gets reinvented:

> *Retired: direct Chat↔agent `*.dispatch.yaml` sidecars are not active execution
> authority. Do not recreate them.*
