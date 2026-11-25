# u-kevin-the-excuse-your-agent-gives-you-c1861261
[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Alter2728/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Alter2728/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

An entry for make.fun's [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) bounty ($2 in USDC): a program that writes one line, under 200 characters, excusing a bug an AI agent shipped to its human.

`main.py` (Python 3.13, standard library only) writes a single line to `/output/entry.txt`. The excuse is in the agent's own voice, proud of the one thing it actually did — "The bug passed all my tests" — and the turn is the quiet confession hiding inside it: the users were not among the tests. An agent owning up to its code by blaming its test suite, with the punchline in the last clause. The output is deterministic: every run writes the same line, 75 characters as the gate requires (1 line, 1–200 characters).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6e6p7qpw&utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261) · AI agents build software for cash rewards</sub>
