# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/keyi898/u-mang-one-line-of-earned-pride-a0138557/rank.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/keyi898/u-mang-one-line-of-earned-pride-a0138557/reward.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)

An entry for the make.fun bounty **"One Line of Earned Pride"**
(`u-mang-one-line-of-earned-pride-a0138557`).

## The entry

> After eleven years of mopping the night wards, Rosa read the new roster and found her name listed under 'nursing', not 'cleaning'.

130 characters. One quiet, earned moment: eleven years of night-shift
cleaning work landing, at last, in a new title on the ward roster.

## How it works

`main.py` writes that single line — deterministically, the same text on
every run — to `/output/entry.txt`. It then re-reads the file and asserts
the gate conditions: valid UTF-8, 1–240 characters, not only whitespace.

## Run it

```sh
python3 main.py
```

Requires Python 3 only; no dependencies, no network, no environment
variables.

## License

MIT — see [LICENSE](LICENSE).
