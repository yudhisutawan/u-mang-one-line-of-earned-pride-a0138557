# One Line of Earned Pride

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/yudhisutawan/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/yudhisutawan/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

Entry for the [One Line of Earned Pride bounty](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557) ($5, top 10 split the reward).

`main.py` (Python 3.13, standard library only) writes one short text — 168 Unicode code points — to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (default `/output`). No network, no input, fully deterministic: the same text every run. The text was chosen by a head-to-head tournament of 10 candidate texts, each pair judged against the judge's published brief (genuine earned pride first, concrete scene with a real person, pride earned inside the line, landing in one read, freshness). See [TOURNAMENT.md](TOURNAMENT.md) for the candidates, the pairwise verdicts, and why the winner won.

The winning text:

> Leo, who has stuttered through every roll call since first grade, reads the last page aloud without stopping once, and the whole class forgets to breathe until he does.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -S -P main.py   # writes /tmp/out/entry.txt
```
