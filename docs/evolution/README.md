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
| **V** — verifiable | A public artifact exists that a reader can open, dated at or before the claim. Link given, **pinned to a commit SHA**. |
| **R** — retrospective | Reconstructed after the fact. No artifact predates the claim. Read as recollection, not record. |
| **O** — open | Proposed and not yet adjudicated. May still turn out to be wrong. |

**V links point at blobs, not at `main`.** A citation that resolves through a moving branch
lets the artifact change after the claim was made — which is the same failure as
reconstructed provenance, one layer up. Issue links are the exception and cannot be pinned;
they carry the date on which their state was read.

The pinned SHAs, for anyone checking:

| artifact | pinned at |
|:--|:--|
| `claim_state_registry.md` | [`d1b32b58`](https://github.com/raylei50653/saccade/blob/d1b32b588fe1a1f49989d9ffff1d907685f148be/docs/research/contracts/claim_state_registry.md) |
| ADR 021 | [`ef3030c0`](https://github.com/raylei50653/saccade/blob/ef3030c0953171e8719eecd45f8b854972d0cb01/docs/decisions/021-asset-provenance-and-progress-reporting.md) |
| `DEVELOPMENT.md` | [`563d57b8`](https://github.com/raylei50653/saccade/blob/563d57b882ddc6bfd69ca414648ab18fdf4757f2/DEVELOPMENT.md) |

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
| **v3** | 2026-09-01 | Asset provenance layer | Governance gates coupled to ordinary development | **V** (landed, [`3973d0db`](https://github.com/raylei50653/saccade/commit/3973d0db8c3afa2948e7a2deead74ee984341494)) |
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
- [`claim_state_registry.md`](https://github.com/raylei50653/saccade/blob/d1b32b588fe1a1f49989d9ffff1d907685f148be/docs/research/contracts/claim_state_registry.md)
  (2026-07-12) — the state fact-owner, with the band table and the object-identity rule.
- [PR #151 / `7010f4d5`](https://github.com/raylei50653/saccade/commit/7010f4d5) (2026-07-13) —
  the diff that narrowed WIP=1 from "one active goal" to "one decision-changing mainline
  charter", with probes explicitly non-WIP. See
  [`failures/02`](failures/02-uniform-wip-1.md).

**What it broke on.** State could now be recorded rigorously, but the chain underneath it
was severed: a ledger row cited a document, and the document cited a number, and nothing
said which run, which commit, which preset produced that number.

---

### v3 — asset provenance · **V**

An inventory on 2026-09-01 measured the gap directly: ~87 GB of experiment output across
six directories, **zero manifests**. Sampled result directories carried no commit SHA, no
preset, no config, no host. Separately, 187 of 290 documents (64%) had no lifecycle status
marker.

The consequence is the one that generalizes: an artifact without identity can be **neither
safely cited nor safely deleted**. Absence of provenance is also what makes cleanup
impossible — the disorder erased the information cleanup would need.

The rule adopted: a manifest is written **before the first result byte**, fail-closed.
Provenance reconstructed afterwards is a plausible story, not a binding.

The refinement that arrived with it is the part worth stealing. Reconstruction is not
banned — an artifact predating the discipline still needs a name — so the **mode is written
into the file**, and the required field set differs by mode. A reconstructed manifest must
name a source for every field it carries and must omit the rest rather than infer them.
Without that, the two shapes are indistinguishable and downstream extends the trust the
recorded ones earned to all of them.

**Artifact:**
[ADR 021](https://github.com/raylei50653/saccade/blob/ef3030c0953171e8719eecd45f8b854972d0cb01/docs/decisions/021-asset-provenance-and-progress-reporting.md)
(2026-09-01).

**Landed:** the ADR document still carries `doc-status: proposed` — it is a planning
document and was never flipped — but the implementation merged the same day:
[`3973d0db`](https://github.com/raylei50653/saccade/commit/3973d0db8c3afa2948e7a2deead74ee984341494)
(merge of [#330](https://github.com/raylei50653/saccade/pull/330), AP-1 + AP-2, *claim
artifact directories before writing results*), followed by the inventory projection and a
schema bump that added `provenance_mode`. The manifest writer is fail-closed: no manifest,
no results.

> The witness is the **merge commit**, not the PR. A pull request is a stable identifier
> whose body can be edited afterwards; the commit cannot. Same rule as the blob pins above.

> **What is still not claimed.** That the ~87 GB was reduced, or that any orphan was
> disposed of. Identity is the precondition for disposal
> ([primitive 02](../primitives/02-identity.md)), and this row establishes only that
> new artifacts have names. "This fixed the problem" would be **R**.

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

→ [`failures/03`](failures/03-governance-coupled-to-development.md) — filed under `failures/`, not `retracted/`: a proposed direction is not an adjudicated one.

---

## What this page does not establish

- **Not that the model is complete.** v4 is open. There is no reason to expect v5 does not
  exist.
- **Not that the primitives are independent.** v4 exists precisely because they are not.
- **Not that this sequence was inevitable.** Only that it happened, in this order, in this
  codebase, for these reasons.
- **Not that every primitive is a transcription.**
  [Projection](../primitives/05-projection.md) is stated stricter than the lab runs it — the
  three conditions are observed, the tier ranking is a correction. It says so on the page.
- **Not a claim about outcomes.** Nothing here asserts that the governance improved the
  tracking results. That would be a claim requiring evidence of a kind this page does not
  have, and under [`primitives/03`](../primitives/03-evidence-promotion.md) it is therefore
  not citable.
