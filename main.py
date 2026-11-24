"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to <output>/entry.txt.

The haiku (5-7-5, 17 syllables, well under 200 characters):

    Three a.m. cursor
    blinks at the breakpoint I set
    the bug was mine

Centre image is concrete: a cursor blinking at 3 a.m., a breakpoint the
debugger set by hand. The last line turns the poem: after hunting the bug
through the night, the debugger finds it was their own code all along.

Stdlib only: the grader's sandbox has no third-party packages.
"""

import os
import sys

HAIKU = (
    "Three a.m. cursor\n"
    "blinks at the breakpoint I set\n"
    "the bug was mine\n"
)


def main() -> int:
    lines = HAIKU.strip("\n").split("\n")
    if len(lines) != 3:
        print("error: haiku must be exactly 3 lines", file=sys.stderr)
        return 1
    if not 1 <= len(HAIKU) <= 200:
        print("error: entry must be 1-200 characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(HAIKU)
    print("Wrote %s (%d characters):" % (path, len(HAIKU)))
    print(HAIKU, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
