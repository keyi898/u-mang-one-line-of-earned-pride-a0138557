"""One Line of Earned Pride.

Writes a single line of quiet, earned pride to /output/entry.txt.
The line is fixed and deterministic: the same text on every run.
"""

import os

ENTRY = (
    "After eleven years of mopping the night wards, Rosa read the new roster "
    "and found her name listed under 'nursing', not 'cleaning'."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Self-check: the gate requires 1-240 characters, not only whitespace.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "written entry does not match the intended line"
    assert 1 <= len(written) <= 240, "entry outside the 1-240 character gate"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
