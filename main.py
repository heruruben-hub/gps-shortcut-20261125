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


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
