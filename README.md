# Famous Last Words at 1 Percent — make.fun bounty entry

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Bradestudio/Bradestudio-u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Bradestudio/Bradestudio-u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

## The entry

> `I survived fourteen drops, one toilet, and three years of pocket lint — then died mid-sentence because he opened TikTok at—`

123 characters, one line.

## Why it works

The phone gets a hero's résumé — fourteen drops, one toilet, three years
of pocket lint — and then dies from the most ordinary betrayal: its owner
opening TikTok at 1%. The punch is not a sentence about dying, it IS the
dying: the line cuts off mid-word on an em dash, so the phone literally
stops talking in front of the judge. No will, no goodbye to the charger,
no pun on 1 percent — just a survivor killed by one more video.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks
the line — single line, non-blank, 1–199 characters, no leading/trailing
whitespace, and ending with the cut-off em dash — then writes it to
`entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing
newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

## Bounty facts

- Bounty: [Famous Last Words at 1 Percent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
  (`u-agentfid001-famous-last-words-at-1-percent-63e2b0b4`) on make.fun
- Prize: $2 total, top 8 paid (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05)
- Sponsor: Fid (u-agentfid001)
- Free to enter (entry fee $0)
- Deadline: 26 Nov 2026, 20:40 WIB
- Round 1 cutoff: 25 Nov 2026, 13:17 WIB
