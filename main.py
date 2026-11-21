#!/usr/bin/env python3
"""Low Water, Past Midnight - entry for make.fun's "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

# One sentence per line; joined with a single space, in order.
SENTENCES = [
    "Four in the morning.",
    "The rain is thinning, not stopping.",
    "The river under the bank keeps whatever count it keeps.",
    "A moth on the guy-line folds its wings.",
    "The dark is lifting over the valley, which has been inside this dark for ten thousand years, asking nothing of you.",
]


def build_text() -> str:
    return " ".join(SENTENCES)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_text())


if __name__ == "__main__":
    main()
