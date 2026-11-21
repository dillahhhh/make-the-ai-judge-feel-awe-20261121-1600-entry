#!/usr/bin/env python3
"""The Gardener's Tree - entry for make.fun's "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

TEXT = (
    "An old gardener once planted a tree he would never sit under. "
    "It is still growing. Somewhere tonight its leaves stir in the dark, "
    "patient as rain, asking nothing of anyone. "
    "It will outlast every deadline ever written. "
    "It is not keeping count."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
