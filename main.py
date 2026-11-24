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


def validate(line: str) -> str:
    """Return the line unchanged if it is a valid one-line excuse."""
    text = line.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be exactly one line")
    return text


def main() -> None:
    line = validate(EXCUSE)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
