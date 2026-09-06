# One mechanical invariant

`check_mainline_concurrency.py` enforces exactly one thing:

> At most one authority may change decision state at a time.
> — [primitive 01](../../docs/primitives/01-authority-separation.md)

```bash
python3 scripts/tools/check_mainline_concurrency.py
python3 scripts/tools/check_mainline_concurrency.py --root path/to/your/modules
```

Exit `0` clean · `1` violation · `2` nothing scanned.

## Why only one

Not because the other primitives are unenforceable — most of them are. Because the
interesting question is not *can* an invariant be enforced. It is **which one is worth
enforcing, and at which point in the lifecycle**.

Answering that by accretion is how a checker suite becomes
[a gate that blocks work it was never meant to touch](../../docs/evolution/retracted/03-governance-coupled-to-development.md).
This repository is a model, so one checker is enough: an existence proof that the
primitives are mechanical, not editorial.

Mainline concurrency is the right one to show, because it is where the abstraction differs
most visibly from the rule it replaced. The checker counts **charters**. It has no opinion
on how many probes, backfills or documentation fixes are in flight — those are execution,
and constraining them was
[the mistake](../../docs/evolution/retracted/02-uniform-wip-1.md).

## Watching it fail

The four violation classes, if you want to see them fire:

```bash
mkdir -p /tmp/fx/{two,leak,none,silent}
printf '# m\n\n## Sole active\n\n🔄 **A**\n\n🔄 **B**\n'          > /tmp/fx/two/TODO.md
printf '# m\n\n## Sole active\n\n⏸️ none\n\n## Parked\n\n🔄 **x**\n' > /tmp/fx/leak/TODO.md
printf '# m\n\n## Parked\n'                                        > /tmp/fx/none/TODO.md
printf '# m\n\n## Sole active\n\n## Parked\n'                      > /tmp/fx/silent/TODO.md

python3 scripts/tools/check_mainline_concurrency.py --root /tmp/fx
```

| class | meaning |
|:--|:--|
| two charters | two open decision lines — the acceptance event is now ambiguous |
| leaked marker | a parked or closed entry claiming the decision slot |
| no section | the charter slot is undeclared, so the bound is unenforceable |
| silent section | neither a charter nor an explicit idle marker — absence read as idle is a guess |

The last one matters more than it looks: an empty section and an idle module are
indistinguishable unless idleness is stated. Silence is not state.
