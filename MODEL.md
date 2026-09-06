# The Model

Five primitives for managing **state, intent, evidence, provenance, and execution** in
long-running, agent-assisted research engineering.

Each primitive is stated as an **invariant** (what must hold), a **failure mode** (what
goes wrong without it), and a **provenance grade** for the claim that it matters.
Depth, worked examples and the observed failures live in [`docs/primitives/`](docs/primitives/).

> **Scope.** This is a model, not a methodology. It says what must stay separated and
> which direction information may flow. It does not say how many directories you need.
> One realization is included under [`reference-realization/`](reference-realization/);
> it is an example, not the model.

---

## The chain

Everything in the model exists to keep one chain unbroken and one-directional:

```text
Run identity  →  Execution  →  Artifact  →  Evidence  →  Accepted claim  →  Decision state
     └── bound before the first result byte ──┘        └─ promotion ─┘   └─ adjudication ─┘
```

Identity comes **first**, not after execution: a run that has already produced output can
only be described, and a description is not a binding ([primitive 2](docs/primitives/02-identity.md)).

The arrows are not all the same kind, and the difference matters:

| arrow | kind | requires |
|:--|:--|:--|
| identity → execution → artifact | **mechanical binding** | that it be recorded, in order. No acceptor; identity is captured, not granted. |
| artifact → evidence | **interpretation** | a method and its conditions, stated |
| evidence → accepted claim | **promotion** | an explicit act, a named home, a recorded acceptor |
| accepted claim → decision state | **adjudication** | an owner accepting that the claim changes what is true |

What the model enforces is uniform even though the arrows are not: **no arrow may be
skipped, and none may be traversed backwards.** The five primitives are the constraints
that keep that true.

---

## 1. Authority separation

> *五種東西不是同一種東西，也不能互相寫入。*

Five bands, each with a different owner, a different lifetime, and a different truth value:

```text
band              holds                          lifetime      may write to
────────────────────────────────────────────────────────────────────────────
accepted state    what is true                   slow          —
intent            what we have chosen to change  per charter   state (on acceptance)
expectation       where we think it will land    disposable    nothing
execution         what we are currently trying   disposable    nothing
acceptance        what was adjudicated           event         state
```

**Invariant.** Writes flow upward only, and only through an acceptance event.
Expectation and execution have **no** authority: an expected state may never be written
back into accepted state, and a probe that ran is not a claim that was accepted.

**Cardinality is a property of the intent band only.** At most one active decision
authority per **declared decision scope** — the exclusive-writer rule, not a work-in-progress
limit. Probes, data backfill, engineering follow-up and documentation cleanup are unbounded;
they are execution, not intent.

The scope is a choice, and declaring it is part of adopting the model. The reference
realization sets `scope = module owner`, which is why its rule reads "one charter per
module" — that is policy, not the invariant.

$$\text{constrain decision concurrency, not execution concurrency}$$

**Failure mode — epistemic leakage.** Without the band separation, a plan becomes a fact
across sessions:

```text
session n     "next we will verify X"        (expectation)
session n+k   "we know X"                    (state)
```

Nothing in between ever adjudicated X. This is the single most common failure in
agent-assisted work, because an agent re-reading its own planning notes cannot tell an
intention from a finding unless the document structure makes them different objects.

→ [`docs/primitives/01-authority-separation.md`](docs/primitives/01-authority-separation.md)

---

## 2. Identity

> *不能被命名的東西，不能被引用，也不能被安全刪除。*

**Invariant.** Anything that may later be cited must carry an identity written **before
the first result byte**: the commit, the dirty state, the preset, the dataset, the host,
the command line, the producer, and the claims it is intended to support.

**Provenance reconstructed after the fact is not production provenance.** Deriving a
manifest for an artifact that already exists produces a plausible story, not a binding —
and the difference is invisible downstream, which is exactly why it must be structural.

**Failure mode — the unreferenceable, undeletable artifact.** Without identity, an output
directory can answer neither "which claim rests on this?" nor "is anything still using
this?" It therefore can be neither safely cited nor safely deleted, and the store only
grows. Absence of identity is *also* the reason cleanup is impossible: the disorder erases
the information cleanup would need.

→ [`docs/primitives/02-identity.md`](docs/primitives/02-identity.md)

---

## 3. Evidence promotion

> *觀察不等於主張。研究筆記本身不可被外部引用。*

**Invariant.** An observation becomes citable only by an explicit promotion into a named
home. Absent that step, a number exists only inside the document that produced it.

**Negative closure is a first-class terminal.** "Not identifiable", "structural premise
failed", "no separation at the achievable sample size" are *results*. A model that can only
record success will silently re-run the same dead end, because nothing durable records that
it was walked.

**Failure mode — second truths.** The same metric appears in a task list, a PR body, a
paper draft and a chat log, then drifts. Each copy is individually defensible and the set
is collectively wrong. Promotion with a single owning home is the only structural fix;
review discipline is not one.

→ [`docs/primitives/03-evidence-promotion.md`](docs/primitives/03-evidence-promotion.md)

---

## 4. Transition admissibility

> *合法 ≠ 值得做。`next admissible unit` ≠ `next task`。*

**Invariant.** State and transition rules together produce a **candidate set** of legal
next moves. Selecting one is a separate act, governed by the intent band (§1). A system
that collapses the two has replaced "mechanically climbing a ladder" with "mechanically
executing `next_admissible_unit`" — the same pathology with better vocabulary.

**Blockers must be typed**, because the orchestration semantics differ:

| type | meaning | what the scheduler does |
|:--|:--|:--|
| `inadmissibility` | illegal in the current state | **exclude** — not queue |
| `dependency` | legal, but something must precede it | **expand** — add the dependency |

**Substrate does not inherit.** Evidence obtained on one substrate does not transfer to
another by default; a claim proven offline is not thereby proven online.

**Failure mode — gate coupling.** When admissibility checks are merged into one gate,
ordinary work is blocked by conditions it never invoked. Three distinct questions must
stay distinct:

$$\text{Development validity} \neq \text{Evidence applicability} \neq \text{Publication completeness}$$

A source change that claims no inheritance of prior evidence should not require
publication-level maintenance to pass. Attempts to *consume* stale evidence must still fail
closed. These are not the same check and must not share an exit code.

→ [`docs/primitives/04-transition-admissibility.md`](docs/primitives/04-transition-admissibility.md)

---

## 5. Projection

> *導覽面永遠不能變成 authority；生成 ≻ 機械對帳 ≻ 只放連結。*

**Invariant.** A projection must never become an authority. Any surface that summarizes
state — a dashboard, a status page, a progress report, a thread card — is subject to three
non-negotiable conditions: it owns nothing, the fact owner wins every conflict, and it
declares which it is.

Given those, the forms are ranked, not binary:

```text
1. generated               derived on demand; cannot drift
2. mechanically reconciled  hand-written, but equality with the owner is checked
3. link-only                permanently correct, carries no content
```

> **Stated stricter than observed.** This ranking is a distilled correction, not a
> transcription: the lab still runs hand-written navigation projections at tier 2. See the
> primitive's Status note.

An **unreconciled** hand-written status page — tier 2 without the check — is a second truth
with a timestamp on it. It is correct on the day it is written and wrong thereafter, and it
is *more* dangerous than no page at all, because it is structured, it is the easiest thing
to find, and a reader arriving cold will trust it over the owners it silently left behind.

**Corollary — thin entrypoints.** The top-level entry document is a router: level →
document pack → action. It composes links. It does not accumulate an encyclopedia, because
every fact it absorbs becomes a copy that drifts.

**Corollary — navigation is not evidence.** A continuity artifact ("where were we, what is
next") is legitimate and valuable, but it holds no tables and settles no numbers. The
moment it carries a result, it has become a second truth.

→ [`docs/primitives/05-projection.md`](docs/primitives/05-projection.md)

---

## What is deliberately *not* in the model

These are one workable implementation. They are reference policy, not invariants:

```text
D0–D4 change levels              a routing scheme, not a primitive
O0 / O1 / O1.5 layering          local vocabulary
the docs/ directory topology     one realization
TODO ≤ 20 lines                  a bloat heuristic
"WIP = 1" per module            scope = module owner is a choice; the invariant is exclusivity
module package schema            convenient, not necessary
a specific ledger table format   a home must exist; its columns are local
```

The distinction matters because the abstraction generalizes and the rule does not.
The core is not *"the TODO file may contain one line."* The core is:

> **At most one active writer per decision-state scope.**

---

## How this model was arrived at

It was not designed. It is what survived four rounds of contact with a production research
codebase, including designs that were adopted and then failed. That history — with
each step graded by how far a reader can verify it — is the other half of this artifact:

- [`docs/evolution/`](docs/evolution/) — v0 → v4, and what broke at each step
- [`docs/evolution/failures/`](docs/evolution/failures/) — two designs withdrawn, one coupling still open
