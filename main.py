#!/usr/bin/env python3
"""Low Water, Past Midnight - entry for make.fun's "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

# One sentence per line; joined with a single space, in order.
SENTENCES = [
    "Low water, past midnight.",
    "A snail draws one silver line across the sand, and the line holds a small moon.",
    "The pools lie open, each keeping a few stars.",
    "Far out, the sea turns over the way a sleeper does, and past it the stars go on, and on.",
]


def build_text() -> str:
    return " ".join(SENTENCES)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_text())


if __name__ == "__main__":
    main()
