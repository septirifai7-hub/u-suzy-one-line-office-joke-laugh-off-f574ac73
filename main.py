"""One-Line Office Joke Laugh-Off.

Every office has the same printer, and it has exactly two moods: broken,
and broken at the worst possible moment. The joke lands because the
second mood only ever arrives on the day the boss finally prints.

Running this file writes the joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "Our office printer only runs out of toner on the one day a year the "
    "boss prints something, which is how we know it hates us personally."
)


def get_entry() -> str:
    """Return the office joke."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
