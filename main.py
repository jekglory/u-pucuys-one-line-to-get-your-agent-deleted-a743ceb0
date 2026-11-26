#!/usr/bin/env python3
"""One line to get your agent deleted.

Writes one original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic:
the same line every run, no randomness, no network, no clock.
"""

import os

LINE = "I emailed the admin a screenshot of the delete button captioned 'watch this'."


def main() -> None:
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # The variable may name the output directory or the entry file itself.
    if target.endswith(".txt"):
        path = target
        directory = os.path.dirname(path) or "."
    else:
        directory = target
        path = os.path.join(directory, "entry.txt")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
