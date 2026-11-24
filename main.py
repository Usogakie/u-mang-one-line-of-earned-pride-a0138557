"""One Line of Earned Pride.

Writes a single line of quiet, earned pride to
${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.

Deterministic: no network, no clock, no randomness. The line is a
fixed string chosen at authoring time, so every run writes the same
bytes.
"""

import os

LINE = (
    "For eleven years he wrote one page a night after the kids slept, "
    "and the morning the box of his own novel arrived, he opened it "
    "in the kitchen and just stared at his name."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
