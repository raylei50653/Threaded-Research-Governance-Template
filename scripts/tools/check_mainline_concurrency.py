#!/usr/bin/env python3
"""Mechanical check for one invariant: mainline decision concurrency.

    At most one active decision authority per declared decision scope.
        -- docs/primitives/01-authority-separation.md

Exclusivity is the invariant. The *scope* is a declaration, and the reference
realization declares `scope = module owner` -- which is why this file scans
module TODOs and allows one charter each. A project declaring a finer scope
(per decision object, say) would legitimately run several charters under one
owner and would need a different query, not a weaker rule.

This is the only enforced invariant in this repository, and it is here as an
existence proof: the primitives in docs/primitives/ are not purely editorial.
It is deliberately not a governance suite. Deciding *which* invariant is worth
enforcing, and at which point in the lifecycle, is the hard part -- see
docs/evolution/failures/03-governance-coupled-to-development.md for what
happens when that question is answered by accretion.

What it enforces
    Under `scope = module owner`: each module TODO declares at most one
    decision-changing mainline charter, marked with the charter glyph, inside
    its "Sole active" section.

What it deliberately does NOT enforce
    Concurrency of probes, backfill, engineering follow-up or documentation
    work. Those are execution, not intent, and are unbounded by design. This
    checker counts charters; it has no opinion on how much work is in flight.

Exit status
    0  every scanned file holds at most one charter, correctly placed
    1  at least one violation
    2  nothing was scanned (bad --root, or no module TODOs found)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHARTER = "\N{ANTICLOCKWISE DOWNWARDS AND UPWARDS OPEN CIRCLE ARROWS}"  # a claim on the decision slot
IDLE = "\N{DOUBLE VERTICAL BAR}"  # explicit "no active charter"
SECTION = "Sole active"

DEFAULT_ROOT = "reference-realization/docs/modules"

# Commented-out template examples legitimately contain a charter marker.
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$")


def strip_comments(text: str) -> str:
    """Blank out HTML comments, preserving line numbering."""

    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))

    return HTML_COMMENT.sub(blank, text)


def sole_active_span(lines: list[str]) -> tuple[int, int] | None:
    """Return [start, end) line indices of the Sole active section body."""
    start = None
    for i, line in enumerate(lines):
        heading = HEADING.match(line)
        if not heading:
            continue
        if start is None:
            if heading.group(1).strip().lower() == SECTION.lower():
                start = i + 1
        else:
            return (start, i)
    return None if start is None else (start, len(lines))


def check_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root.parent if root.parent != path else root)
    lines = strip_comments(path.read_text(encoding="utf-8")).splitlines()

    span = sole_active_span(lines)
    if span is None:
        return [f"{rel}: no '## {SECTION}' section -- the charter slot is undeclared"]

    start, end = span
    inside = [i for i in range(start, end) if CHARTER in lines[i]]
    outside = [
        i for i in range(len(lines)) if CHARTER in lines[i] and not (start <= i < end)
    ]

    problems: list[str] = []
    if len(inside) > 1:
        where = ", ".join(f"line {i + 1}" for i in inside)
        problems.append(
            f"{rel}: {len(inside)} mainline charters in '{SECTION}' ({where}) -- "
            f"one active decision authority per scope; scope here is the module"
        )
    for i in outside:
        problems.append(
            f"{rel}:{i + 1}: charter marker outside '{SECTION}' -- "
            f"parked and closed entries must not claim the decision slot"
        )
    if not inside and not outside and IDLE not in "\n".join(lines[start:end]):
        problems.append(
            f"{rel}: '{SECTION}' declares neither a charter nor an explicit idle marker"
        )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        default=DEFAULT_ROOT,
        help=f"directory holding module packages (default: {DEFAULT_ROOT})",
    )
    parser.add_argument("--quiet", action="store_true", help="print only violations")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"check_mainline_concurrency: no such directory: {root}", file=sys.stderr)
        return 2

    todos = sorted(p for p in root.glob("*/TODO.md") if p.parent.name != "_template")
    if not todos:
        print(f"check_mainline_concurrency: no module TODOs under {root}", file=sys.stderr)
        return 2

    problems: list[str] = []
    for todo in todos:
        problems.extend(check_file(todo, root))

    for problem in problems:
        print(f"VIOLATION  {problem}")

    if not args.quiet:
        verb = "violation" if len(problems) == 1 else "violations"
        print(f"\nscanned {len(todos)} module TODO(s) under {root} -- {len(problems)} {verb}")
        if not problems:
            print("probe / follow-up / documentation concurrency is unbounded and not checked")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
