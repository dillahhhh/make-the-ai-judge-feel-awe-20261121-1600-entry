#!/usr/bin/env python3
"""Low Water, Past Midnight - entry for make.fun's "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

# One sentence per line; joined with a single space, in order.
SENTENCES = [
    "Slack water.",
    "In a rock pool one barnacle opens its small door and waits.",
    "The flats lie wet and quiet to the horizon.",
    "Above the cloud the moon is lifting the sea, an inch at a time, the way you carry a sleeping child from a car.",
    "It has done this since before there were doors.",
]


def build_text() -> str:
    return " ".join(SENTENCES)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_text())


if __name__ == "__main__":
    main()
