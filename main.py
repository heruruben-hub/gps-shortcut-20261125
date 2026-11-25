#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt, exactly as the competition requires:
one line of plain text, 1 to 200 characters, no setup, no dialogue
tags, just the excuse itself, in the GPS's own voice.
"""

import os

LINE = (
    "That cul-de-sac was a shortcut, I swear, the map just forgot to "
    "mention the wedding, the lake, and the part where the road stops "
    "existing."
)


def validate_line(line: str) -> None:
    """Fail loudly if the entry line breaks the competition rules."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(
            f"entry line must be 1-200 characters, got {len(line)}"
        )
    if line.strip() != line or "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line with no padding")


def main() -> None:
    validate_line(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
