#!/usr/bin/env python3
"""Snooze Button Roast — writes the winning one-line roast to entry.txt.

The program writes exactly one line (no trailing newline) to
<output_dir>/entry.txt, where <output_dir> is $MAKEFUN_OUTPUT_DIR when set
and /output otherwise. The output is byte-identical to entry.txt in this repo.
"""

import os

ENTRY = (
    "My alarm clock went off at 6 AM on a Saturday like a GPS "
    "recalculating my sleep \u2014 'in 9 minutes, turn left into regret.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
