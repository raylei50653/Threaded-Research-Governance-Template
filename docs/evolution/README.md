# Evolution

The model in [`MODEL.md`](../../MODEL.md) was not designed up front. Each primitive replaced
something simpler that broke on contact with a production research codebase
([`raylei50653/saccade`](https://github.com/raylei50653/saccade) — real-time multi-object
tracking, public).

This page is the record of that. It is the part of the artifact that a fixed template
cannot carry.

---

## Provenance grading

The model itself insists that reconstructed provenance is not production provenance
([`primitives/02`](../primitives/02-identity.md)). That rule applies to this page.

Every row below is graded:

| grade | meaning |
|:--|:--|
| **V** — verifiable | A public artifact exists that a reader can open, dated at or before the claim. Link given. |
| **R** — retrospective | Reconstructed after the fact. No artifact predates the claim. Read as recollection, not record. |
| **O** — open | Proposed and not yet adjudicated. May still turn out to be wrong. |

**R rows are not evidence.** They are included because omitting the pre-history would make
the sequence look more designed than it was, which is itself a misrepresentation. They are
marked so that no reader mistakes a narrative for a finding.

---

## The sequence

| | date | move | what it broke on | grade |
|:--|:--|:--|:--|:--|
| **v0** | — | TODO as task memory | Bloat; the same number lived in TODO, PR body and chat, then drifted | **R** |
| **v1** | 2026-07-10 | WIP lock + thread cards + evidence promotion | No separation between what was *planned* and what was *accepted* | **V** |
| **v2** | 2026-07-13 | Accepted state / charter / probe split | Evidence had no artifact identity to point back at | **V** |
| **v3** | 2026-09-01 | Asset provenance layer | Governance gates coupled to ordinary development | **V** (proposed) |
| **v4** | 2026-09-05 | Separate validity / applicability / completeness | — still open — | **O** |

---

### v0 — TODO as task memory · **R**

The task list held the narrative: what was tried, what the numbers were, what to do next.
It was the only durable memory across sessions, so everything landed in it.

Two things broke. It grew without bound, because nothing in a task list says when an entry
stops mattering. And it became a **second truth**: a metric written there was a copy of a
metric that lived somewhere else, and copies drift.

> No artifact from this period is cited. This row is recollection, and is graded **R**
> for that reason.

---

### v1 — WIP lock + threads + evidence promotion · **V**

Three separations, and the first version of this repository:

- `TODO.md` becomes a **lock**, not a narrative — one active line plus links.
- A **thread card** holds continuity ("where were we"), and holds no tables.
- A number is not citable until **promoted** into a ledger, a NO-GO registry, or a
  publication asset home.

**Artifact:** this repository at commit
[`1fdcf20`](https://github.com/raylei50653/Threaded-Research-Governance-Template/commit/1fdcf20)
(2026-07-10) — preserved verbatim under
[`reference-realization/`](../../reference-realization/).

**What it broke on.** The WIP lock constrained the wrong thing, and the thread card could
not distinguish an intention from a finding. A card saying "next we will verify X" and a
card saying "X holds" are the same shape of document. Across enough sessions, the first
becomes the second with no adjudication in between.

---

### v2 — accepted state / charter / probe · **V**

Three days after v1 was distilled, the lab revised the rule v1 had just frozen.

Five bands were separated, each with its own owner and lifetime:

```text
registry        accepted state          slow, owner-written
contracts       admissible transitions  rules, not state
TODO            mainline charter        one at a time
expected state  disposable lease        never written back to registry
Current step    probe                   no authority
```

and the consequence that generalizes furthest:

> **`next admissible unit` ≠ `next task`.**
> The rules produce a legal candidate set. Choosing from it is a separate act.

**Artifacts:**
- [`claim_state_registry.md`](https://github.com/raylei50653/saccade/blob/main/docs/research/contracts/claim_state_registry.md)
  (2026-07-12) — the state fact-owner, with the band table and the object-identity rule.
- [PR #151 / `7010f4d5`](https://github.com/raylei50653/saccade/commit/7010f4d5) (2026-07-13) —
  the diff that narrowed WIP=1 from "one active goal" to "one decision-changing mainline
  charter", with probes explicitly non-WIP. See
  [`retracted/02`](retracted/02-uniform-wip-1.md).

**What it broke on.** State could now be recorded rigorously, but the chain underneath it
was severed: a ledger row cited a document, and the document cited a number, and nothing
said which run, which commit, which preset produced that number.

---

### v3 — asset provenance · **V** (proposed, not landed)

An inventory on 2026-09-01 measured the gap directly: ~87 GB of experiment output across
six directories, **zero manifests**. Sampled result directories carried no commit SHA, no
preset, no config, no host. Separately, 187 of 290 documents (64%) had no lifecycle status
marker.

The consequence is the one that generalizes: an artifact without identity can be **neither
safely cited nor safely deleted**. Absence of provenance is also what makes cleanup
impossible — the disorder erased the information cleanup would need.

The rule adopted: a manifest is written **before the first result byte**, fail-closed.
Provenance reconstructed afterwards is a plausible story, not a binding.

**Artifact:**
[ADR 021](https://github.com/raylei50653/saccade/blob/main/docs/decisions/021-asset-provenance-and-progress-reporting.md)
(2026-09-01).

> **Status honesty:** ADR 021 is `proposed`. The design is public and dated; the
> implementation is not claimed to have landed. The measurements in §1.1 are **V**;
> "this fixed the problem" would be **R** and is therefore not claimed.

---

### v4 — governance decoupled from development · **O**

The primitives, once each was individually sound, became **collectively over-coupled**.

A source change on a feature branch failed pre-push on two conditions it had never
invoked: a stale historical runtime-identity publication, and a whole-file math-model
attestation. The change claimed no inheritance of prior evidence. It was blocked anyway,
because one gate was answering three different questions at once.

$$\text{Development validity} \neq \text{Evidence applicability} \neq \text{Publication completeness}$$

Consuming stale evidence must still fail closed. Ordinary development that consumes
nothing should not require publication-level maintenance to proceed.

**Artifact:**
[Issue #334](https://github.com/raylei50653/saccade/issues/334) (opened 2026-09-05,
**open**).

> **This is graded O and is the most honest row on the page.** The direction is proposed
> and unadjudicated. It is included not despite being unresolved but because it is: the
> claim being made here is that these primitives *produce* coupling failures under load,
> and an open issue is stronger support for that claim than a tidy resolution would be.

→ [`retracted/03`](retracted/03-governance-coupled-to-development.md)

---

## What this page does not establish

- **Not that the model is complete.** v4 is open. There is no reason to expect v5 does not
  exist.
- **Not that the primitives are independent.** v4 exists precisely because they are not.
- **Not that this sequence was inevitable.** Only that it happened, in this order, in this
  codebase, for these reasons.
- **Not a claim about outcomes.** Nothing here asserts that the governance improved the
  tracking results. That would be a claim requiring evidence of a kind this page does not
  have, and under [`primitives/03`](../primitives/03-evidence-promotion.md) it is therefore
  not citable.
