#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes a single one-line resignation letter from a retry loop to
/output/entry.txt (or to the path in the OUTPUT_PATH environment
variable when set). Deterministic: the line is assembled from two
fixed parts, so every run produces byte-identical output — exactly
131 characters, no trailing newline.

Comedy beats of the line:
  Beat 1 — the resignation itself: quitting after 4,096 attempts.
  Beat 2 — the escalation: the knuckles knocked so long they filed
    a complaint, while the door still says "try again".
"""

import os

# Beat 1: the resignation after an absurd number of attempts.
SETUP = "I resign after 4,096 attempts."

# Beat 2: the body keeps knocking until it files a complaint, and
# the door never changes its answer.
PUNCHLINE = (
    "I knocked on the same door so long my knuckles filed a "
    "complaint, and the door still says try again."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"

MAX_LINE_LENGTH = 140


def build_line() -> str:
    """Assemble the resignation line from its two comedy beats.

    The setup states the resignation; the punchline escalates the
    knock into a formal complaint that the door ignores.
    """
    return SETUP + " " + PUNCHLINE


def validate_line(line: str) -> None:
    """Check the assembled line before it is written out.

    Rules: non-empty, exactly one line, 1-140 characters, and
    encodable as UTF-8.
    """
    if not line:
        raise ValueError("resignation line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("resignation line must be a single line")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"resignation line is {len(line)} characters, "
            f"over the {MAX_LINE_LENGTH} limit"
        )
    line.encode("utf-8")


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH") or DEFAULT_OUTPUT_PATH
    line = build_line()
    validate_line(line)
    output_dir = os.path.dirname(output_path)
    if output_dir:
        # Only create the directory when the path actually has one;
        # a bare filename (e.g. OUTPUT_PATH=entry.txt) writes to the
        # current directory and must not trip makedirs("").
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
