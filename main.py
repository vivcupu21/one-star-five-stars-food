"""One Star, Five Stars for the Food.

Writes the single-sentence alien tourist review stored in entry.txt
to $MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, no network, no randomness.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(source, target)
    with open(source, "rb") as handle:
        expected = handle.read()
    with open(target, "rb") as handle:
        actual = handle.read()
    if actual != expected:
        print("copied entry differs from stored entry", file=sys.stderr)
        return 1
    with open(target, "r", encoding="utf-8") as handle:
        text = handle.read()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
