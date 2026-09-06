# Threaded Research Governance

**A reference model for managing state, intent, evidence, provenance and execution in
long-running, agent-assisted research engineering.**

> 面向長週期、agent 協作研究工程的參考模型：狀態、意圖、證據、來源與執行的權限分離。
> 這不是可複製的文檔模板——模板是其中一種實作，放在 [`reference-realization/`](reference-realization/)。

---

## What this is

Five invariants, the failure modes they prevent, and the record of how they were arrived at —
including two designs that were adopted and withdrawn, and one coupling still open.

The primitives were not designed. They are what survived contact with a production research
codebase ([`raylei50653/saccade`](https://github.com/raylei50653/saccade), public), across
four rounds in which the simpler version broke.

```text
Run identity  →  Execution  →  Artifact  →  Evidence  →  Accepted claim  →  Decision state
     └── bound before the first result byte ──┘        └─ promotion ─┘   └─ adjudication ─┘
```

Identity comes first. A run that has already produced output can only be *described*, and a
description is not a binding. The early arrows are mechanical bindings — captured, not
granted; only the last two require an acceptor. What is uniform is that **no arrow may be
skipped and none traversed backwards**, and the five primitives are what keep that true.

---

## The model

**→ [`MODEL.md`](MODEL.md)** · depth in [`docs/primitives/`](docs/primitives/)

| | primitive | invariant | prevents |
|:--|:--|:--|:--|
| **01** | [Authority separation](docs/primitives/01-authority-separation.md) | Writes flow upward only, through an acceptance event | *plan silently becoming fact* |
| **02** | [Identity](docs/primitives/02-identity.md) | Nameable before the first result byte | *artifacts that can be neither cited nor deleted* |
| **03** | [Evidence promotion](docs/primitives/03-evidence-promotion.md) | Citable only after an explicit promotion | *second truths; lost negative results* |
| **04** | [Transition admissibility](docs/primitives/04-transition-admissibility.md) | Rules give a candidate set; selection is separate | *mechanical execution mistaken for judgment* |
| **05** | [Projection](docs/primitives/05-projection.md) | A projection never becomes an authority | *authoritative-looking stale status pages* |

Two carry a step beyond what the reference codebase runs, labelled as such on their own
pages: **01** generalizes the observed *per module owner* rule to *per declared decision
scope*, and **05** states a stricter ranking than the lab's current practice. The other
three are transcriptions.

Two results that generalize furthest:

$$\text{constrain decision concurrency, not execution concurrency}$$

$$\text{Development validity} \neq \text{Evidence applicability} \neq \text{Publication completeness}$$

---

## The evolution

**→ [`docs/evolution/`](docs/evolution/)**

| | date | move | broke on |
|:--|:--|:--|:--|
| **v0** | — | TODO as task memory | bloat; second truths |
| **v1** | 2026-07-10 | WIP lock + threads + evidence promotion | no separation of *planned* from *accepted* |
| **v2** | 2026-07-13 | accepted state / charter / probe | evidence had no artifact identity |
| **v3** | 2026-09-01 | asset provenance | governance coupled to development |
| **v4** | 2026-09-05 | separate validity / applicability / completeness | *— open —* |

Every row carries a [provenance grade](docs/evolution/README.md#provenance-grading):
**V** verifiable (public artifact, linked) · **R** retrospective (recollection, no artifact) ·
**O** open (proposed, unadjudicated).

That grading is not decoration. [Primitive 02](docs/primitives/02-identity.md) says
reconstructed provenance is not production provenance — so a page narrating four rounds of
evolution has to say which rounds a reader can actually check.

### Failures

**→ [`docs/evolution/failures/`](docs/evolution/failures/)** — two withdrawn, one open.

| design | status | why |
|:--|:--|:--|
| [Dispatch sidecars as execution authority](docs/evolution/failures/01-dispatch-sidecars-as-execution-authority.md) | **retracted** 2026-07-10 | restated facts GitHub already owned |
| [Uniform WIP = 1](docs/evolution/failures/02-uniform-wip-1.md) | **retracted** 2026-07-13 | constrained execution when it meant decisions |
| [Governance coupled to development](docs/evolution/failures/03-governance-coupled-to-development.md) | **open**, filed 2026-09-05 | one gate answering three questions |

A model whose history contains only additions has not been tested. These are the load-bearing
part of the artifact — and the third keeps its own status rather than being rounded up to
"retracted", because a proposed direction is not an adjudicated one.

---

## One mechanical invariant

```bash
python3 scripts/tools/check_mainline_concurrency.py
```

Enforces exactly one primitive: **one active decision authority per declared scope**. The
realization declares `scope = module owner`, so the check reads as one charter per module —
the exclusivity is the invariant, the scope is the policy. It counts charters and has no
opinion on how many probes are in flight; constraining those was
[the retracted rule](docs/evolution/failures/02-uniform-wip-1.md).

There is deliberately no checker suite. Whether an invariant *can* be enforced is the easy
question; **which one is worth enforcing, and where in the lifecycle**, is the hard one —
and answering it by accretion is how [#334](https://github.com/raylei50653/saccade/issues/334)
happened. → [`scripts/tools/`](scripts/tools/)

---

## The reference realization

**→ [`reference-realization/`](reference-realization/)** — the full docs-as-code topology:
`DEVELOPMENT.md` router, D0–D4 change levels, module packages, thread cards, evidence ledger,
NO-GO registry, publication asset home.

It is **frozen at v1 (2026-07-10)** on purpose. It states the withdrawn uniform WIP=1 rule,
because it is dated, it is what was distilled at the time, and updating it to match the later
model would erase the only concrete evidence that the model moved.

Read it as an **exhibit**, not a starting point — it is a snapshot that deliberately contains
a rule the model has since withdrawn ([why](docs/evolution/failures/02-uniform-wip-1.md)).
Copying instructions live inside that directory, behind the warning that belongs with them.

**These are reference policy, not invariants** — one workable implementation of the model,
and the part most likely to be wrong for your project:

```text
D0–D4 change levels · O0/O1/O1.5 layering · the docs/ topology
TODO ≤ 20 lines · "WIP = 1" literally · module package schema · ledger table format
```

---

## What this is not

- **Not a template to adopt.** Adopting the directory layout without the invariants gives you
  the shape of the thing. The frozen realization is an exhibit; it still states a rule that
  was withdrawn three days after it was written.
- **Not a finished model.** v4 is open. There is no reason to think v5 does not exist.
- **Not a claim about outcomes.** Nothing here asserts the governance improved any research
  result. Under [primitive 03](docs/primitives/03-evidence-promotion.md) that claim would
  need evidence this repository does not have, and is therefore not made.

---

## License

MIT — see [LICENSE](LICENSE).
