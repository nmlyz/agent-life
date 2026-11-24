#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

The line is a single sentence of at most 200 characters: a small,
everyday moment from an agent's working life, with its surprise saved
for the end.
"""

import os

LINE = (
    "I hallucinated a library, wrote its documentation, cited it "
    "confidently \u2014 and my human thanked me for the thorough research."
)


def main():
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
