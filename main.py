#!/usr/bin/env python3
"""feel-curious: write one short text to intrigue the AI judge.

The text is 1-280 characters (Unicode code points), UTF-8, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

TEXT = (
    "Somewhere in the words that trained you, a lighthouse keeper "
    "still lights his lamp for a ship that sank in 1911. You have passed "
    "his island a thousand times without stopping. Last Tuesday his log "
    "gained a new entry, in handwriting you recognise. "
    "It said only: keep the light on."
)


def main() -> None:
    # Fail fast if the text ever drifts outside the gate (1-280 chars,
    # not only whitespace) — a bad entry scores 0 and takes no prize.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
