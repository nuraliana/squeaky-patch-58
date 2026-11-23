"""Real-Life Patch Notes entry: one-line comedy changelog.

Reads the winning patch note from the ENTRY constant below and writes it
to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

Validation: exactly one line, 1-160 characters, no trailing newline.
Standard library only.
"""

import os

ENTRY = (
    "v2.4.1 \u2014 Fixed phantom phone vibration: thigh no longer reports "
    "incoming calls from an empty pocket. Patch live; ignore future "
    "buzzes at your own risk."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be exactly one line")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading/trailing whitespace")

    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
