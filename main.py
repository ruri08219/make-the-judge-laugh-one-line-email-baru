#!/usr/bin/env python3
"""Make the Judge Laugh in One Line -- writes one funny line to /output/entry.txt.

Stdlib only, no dependencies. The entry is a single line of 1-200
characters, not whitespace-only, so it passes the sealed gate.
"""

import os
import sys

ENTRY = "I asked my AI to water the plants. It scheduled a meeting with the fern and billed me for the consultation."
MAX_CHARS = 200


def validate(text):
    """Reject anything the gate would refuse: empty, too long, multi-line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry exceeds %d characters: %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print("wrote %d chars to %s" % (len(entry), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
