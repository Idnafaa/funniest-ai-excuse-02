#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

A tiny program with one job: put a single original excuse line
(130 characters, well under the 200-character cap) into
/output/entry.txt, where the sealed scorer and the judge can read it.
"""

from pathlib import Path

EXCUSE = (
    "Sorry \u2014 I was halfway through your task when my context window "
    "filled up, so I evicted the deadline to make room for this apology."
)


def main() -> None:
    line = EXCUSE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(line)}")
    if "\n" in line:
        raise ValueError("excuse must be exactly one line")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
