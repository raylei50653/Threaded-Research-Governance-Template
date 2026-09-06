# Threaded Research Governance

**A reference model for managing state, intent, evidence, provenance and execution in
long-running, agent-assisted research engineering.**

> 面向長週期、agent 協作研究工程的參考模型：狀態、意圖、證據、來源與執行的權限分離。
> 這不是可複製的文檔模板——模板是其中一種實作，放在 [`reference-realization/`](reference-realization/)。

---

## What this is

Five invariants, the failure modes they prevent, and the record of how they were arrived at —
including three designs that were adopted and then withdrawn.

The primitives were not designed. They are what survived contact with a production research
codebase ([`raylei50653/saccade`](https://github.com/raylei50653/saccade), public), across
four rounds in which the simpler version broke.

```text
Execution  →  Artifact identity  →  Evidence  →  Accepted claim  →  Decision state
```

Every arrow is a promotion: an explicit act, a named home, a recorded acceptor. No arrow may
be skipped and none may be traversed backwards. The five primitives are what keep that chain
honest.

---

## The model

**→ [`MODEL.md`](MODEL.md)** · depth in [`docs/primitives/`](docs/primitives/)

| | primitive | invariant | prevents |
|:--|:--|:--|:--|
| **01** | [Authority separation](docs/primitives/01-authority-separation.md) | Writes flow upward only, through an acceptance event | *plan silently becoming fact* |
| **02** | [Identity](docs/primitives/02-identity.md) | Nameable before the first result byte | *artifacts that can be neither cited nor deleted* |
| **03** | [Evidence promotion](docs/primitives/03-evidence-promotion.md) | Citable only after an explicit promotion | *second truths; lost negative results* |
| **04** | [Transition admissibility](docs/primitives/04-transition-admissibility.md) | Rules give a candidate set; selection is separate | *mechanical execution mistaken for judgment* |
| **05** | [Projection](docs/primitives/05-projection.md) | Summaries are generated or are links | *authoritative-looking stale status pages* |

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

### Three retracted designs

**→ [`docs/evolution/retracted/`](docs/evolution/retracted/)**

| | withdrawn | why |
|:--|:--|:--|
| [Dispatch sidecars as execution authority](docs/evolution/retracted/01-dispatch-sidecars-as-execution-authority.md) | 2026-07-10 | restated facts GitHub already owned |
| [Uniform WIP = 1](docs/evolution/retracted/02-uniform-wip-1.md) | 2026-07-13 | constrained execution when it meant decisions |
| [Governance coupled to development](docs/evolution/retracted/03-governance-coupled-to-development.md) | *in flight* | one gate answering three questions |

A model whose history contains only additions has not been tested. These are the load-bearing
part of the artifact.

---

## One mechanical invariant

```bash
python3 scripts/tools/check_mainline_concurrency.py
```

Enforces exactly one primitive: at most one decision-changing charter per owner. It counts
charters and has no opinion on how many probes are in flight — constraining those was
[the retracted rule](docs/evolution/retracted/02-uniform-wip-1.md).

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

Copy it as an overlay if you want a starting point:

```bash
cp -a reference-realization/. /path/to/your/repo/
```

Then read [retracted/02](docs/evolution/retracted/02-uniform-wip-1.md) before you adopt its
WIP rule literally.

**These are reference policy, not invariants** — one workable implementation of the model,
and the part most likely to be wrong for your project:

```text
D0–D4 change levels · O0/O1/O1.5 layering · the docs/ topology
TODO ≤ 20 lines · "WIP = 1" literally · module package schema · ledger table format
```

---

## What this is not

- **Not a template to adopt.** Adopting the directory layout without the invariants gives you
  the shape of the thing.
- **Not a finished model.** v4 is open. There is no reason to think v5 does not exist.
- **Not a claim about outcomes.** Nothing here asserts the governance improved any research
  result. Under [primitive 03](docs/primitives/03-evidence-promotion.md) that claim would
  need evidence this repository does not have, and is therefore not made.

---

## License

MIT — see [LICENSE](LICENSE).
