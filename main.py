#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes the entry -- one sentence, at most 280 characters, recalling a
childhood memory -- to /output/entry.txt, and prints it.

Why this line: the brief's own examples (a grandmother's kitchen, a summer
evening, the smell of fresh rice) are the lines hundreds of other entries
will echo, so the winning angle has to be one nobody else reaches for. A
CRT television that only worked when Dad slapped its side in exactly the
right spot is a ritual from a vanished era: concrete (the slap, the static,
the Saturday cartoon theme), honest (a small, specific, slightly absurd
detail that could only come from a real living room), and warm -- the ache
lands in the last clause, when the whole world fit inside that buzzing
little screen for one hour, and then the hour ended.
"""

import os

ENTRY = (
    "Dad slapped the television's side in exactly the right spot, and the "
    "static cleared just as the Saturday cartoon theme began, and for one "
    "hour the whole world fit inside that buzzing little screen."
)

MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in ENTRY, "the entry must be a single line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, outside the 1-{MAX_CHARS} range"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and confirm the gate sees exactly this one line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match the source line"
    assert "\n" not in written, "written entry must stay a single line"
    print(ENTRY)


if __name__ == "__main__":
    main()
