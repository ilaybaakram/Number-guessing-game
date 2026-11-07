# 💜 Number Guessing Game

*A little game from 12th standard, lovingly refreshed.*

## 🎀 [Play A Little Guess of Luck Online](https://a-little-guess-of-luck.streamlit.app/)

Come play the cozy pastel version right in your browser—no installation needed! 🐰

This was one of my early programming projects: a simple C game where you try to guess a secret number. I'm keeping it as a small reminder of where my coding journey began, while giving it a cute, cozy makeover.

## 🐰 The original C game

The original program is kept at the repository root in `NUMBER_GUESS_GAME.c`. It now chooses a **random secret number from 1 to 100** each round, instead of always using `42`.

### Play the C version

Compile with a C compiler:

```bash
gcc NUMBER_GUESS_GAME.c -o number-guessing-game
./number-guessing-game
```

The game gives directional and proximity hints, and lets you play another round.

## ✨ Cozy Python version

A pastel-themed interactive version lives in [`cute-version/`](cute-version/), built with Streamlit.

### Run it locally

```bash
cd cute-version
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 🌷 About

Not every project has to be huge or complicated. This one is a little milestone in my journey from 12th standard to studying Computer Science—and a reminder to appreciate how far I've come.

Made with 💗, curiosity, and a little luck.
