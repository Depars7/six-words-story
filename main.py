#!/usr/bin/env python3
"""Entry for make.fun's "Six Words, One Story" bounty.

The whole deliverable is a single six-word story, assembled
here word by word so the count can never drift: a widow,
a garden in bloom, and the husband who planted it before
he died. The program writes the story to /output/entry.txt.
"""

import os
import sys

WORDS = [
    "Widow's",
    "garden",
    "bloomed;",
    "he",
    "planted",
    "everything.",
]

EXPECTED_WORDS = 6


def render_story() -> str:
    """Join the words into the story and check the count."""
    if len(WORDS) != EXPECTED_WORDS:
        raise ValueError("the story must hold exactly six words")
    return " ".join(WORDS)


def target_path() -> str:
    folder = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(folder, exist_ok=True)
    except OSError:
        folder = os.path.join(os.getcwd(), "output")
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> int:
    text = render_story()
    with open(target_path(), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
