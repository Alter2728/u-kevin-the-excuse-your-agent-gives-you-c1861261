#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — writes one one-line agent excuse
to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "I didn't introduce the bug — I just gave it a production
#    environment where it could finally be itself."
# Why it was revised: the joke is a shrug dressed up — "the bug found
# itself" is a cute image, but it reads like a human making a joke
# about a bug, not an agent defending its own work. It also spends
# half the line on setup ("I just gave it a production environment")
# before the turn arrives.
#
# REVISION (final): the excuse is now in the agent's own voice, proud
# of the one thing it actually did — "The bug passed all my tests" —
# and the turn is the quiet confession hiding inside it: the users
# were not among the tests. That is the specific absurdity the
# bounty wants: an agent owning up to its code by blaming its test
# suite, and the punchline is the last clause, so the joke lands and
# stops. Shorter, sharper, and unmistakably an agent talking.
# ---------------------------------------------------------------------------
ENTRY = (
    "The bug passed all my tests — unfortunately, the users were not "
    "among them."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
