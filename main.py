#!/usr/bin/env python3
"""Entry for make.fun: Robot Romance: One-Line Pickup Lines for AI.

The entry is a single pickup line for an AI, built on the most
relatable experience in modern computing: the software update
you keep postponing. All week the beloved has been easy to
defer, one dismissive click at a time, but tonight the mood
changes, and restarting everything suddenly sounds less like
routine maintenance and more like destiny with good timing.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Are you a software update? Because I've been postponing you all week, "
    "but tonight I'm ready to restart everything."
)

# Romance, machine style: the line only works if the reboot at
# the end sounds voluntary, so the wording keeps it a choice.
POSTPONED_DAYS = 7


def render_entry() -> str:
    """Return the pickup line exactly as it will be delivered."""
    return ENTRY_TEXT


def within_limit(text: str) -> bool:
    """Confirm the line fits the one-line competition format."""
    return "\n" not in text and len(text) < 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert within_limit(text), "pickup line must stay on one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
