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


def sanitize_entry(text: str) -> str:
    """Guarantee the entry is exactly one line of plain text.

    Strips trailing newline characters and removes any control
    characters, so the written file can never contain a newline or
    control character. Raises ValueError if the result is empty,
    multi-line, or over the 200-character competition limit.
    """
    cleaned = text.rstrip("\r\n")
    cleaned = "".join(ch for ch in cleaned if ord(ch) >= 0x20 and ord(ch) != 0x7F)
    if not cleaned.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if len(cleaned) > 200:
        raise ValueError("entry exceeds the 200-character limit")
    return cleaned


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sanitize_entry(ENTRY))


if __name__ == "__main__":
    main()
