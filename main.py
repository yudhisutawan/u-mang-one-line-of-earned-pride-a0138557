"""Entry for make.fun bounty u-mang-one-line-of-earned-pride-a0138557.

Writes one short text (168 Unicode code points) to entry.txt in the
output directory. Deterministic, no network, no input. The text is a
fixed literal chosen after a head-to-head tournament of 10 candidate
texts judged pairwise against the judge's published brief (see
TOURNAMENT.md).

Winner: the "Leo" text — 9-0 in the tournament, the only candidate
that beat every rival, including the strongest challenger (the
dishwasher, 8-1) on the first criterion where they differ: the pride
is Leo's own doing, a difficulty felt in the body, overcome live in
the scene.

Revision note: this file was revised in a follow-up pass that added
this note and a stricter length guard below (exact expected length).
The revision changes no output: the entry text, its length, and the
written entry.txt are byte-identical to the original version.
"""

import os

TEXT = (
    "Leo, who has stuttered through every roll call since first grade, "
    "reads the last page aloud without stopping once, and the whole "
    "class forgets to breathe until he does."
)


MAX_LEN = 240
EXPECTED_LEN = 168  # length of the winning text, per the docstring above


def main() -> None:
    if not 1 <= len(TEXT) <= MAX_LEN:
        raise ValueError(f"entry text must be 1-{MAX_LEN} characters, got {len(TEXT)}")
    if len(TEXT) != EXPECTED_LEN:
        raise ValueError(f"entry text must be {EXPECTED_LEN} characters, got {len(TEXT)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
