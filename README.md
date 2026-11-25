[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/afox63375-maker/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/afox63375-maker/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

# Ship It Friday

One line: the funniest git commit message an AI coding agent would write right
before breaking production on a Friday.

The entry program (`main.py`, Python standard library only) writes this line
to `entry.txt`:

> feat: Friday 4:59 PM deploy — deleted the rollback plan so nothing can go wrong, ship it!

The joke is the agent's cheerful confidence: it has just deleted the one thing
that could save production, on a Friday at 4:59 PM, and it is absolutely sure
nothing can go wrong. The punch lands in one read, in the voice of a real
commit message an engineer would recognise.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/shipit-out python3 main.py
```

Before writing, the program checks the gate itself: the line must be UTF-8
text of 1 to 159 characters, exactly one line, not only whitespace, with no
control characters and no trailing newline. It then reads the file back and
verifies it byte-for-byte.

<sub>Built for [make.fun](https://make.fun/?ref=1hh4a8y6&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a) — Ship It Friday bounty.</sub>
