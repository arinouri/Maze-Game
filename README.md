# Maze Racing Game

A local Python/Pygame maze game experiment featuring procedurally generated maze layouts and two-player visual elements.

## Technology

- Python 3
- Pygame

## Getting started

```bash
python3 -m pip install pygame
python3 '#python.py'
```

The filename `#python.py` is the actual script name in this repository; quote it when invoking it from a shell.

## Implementation notes

The script configures an 800×600 Pygame window, two player colors, and a recursive-backtracking maze generator. It also contains display and movement logic. This README describes the current source rather than making claims about packaging or automated testing.

## Improvements to explore

- Rename the entry point to `maze_game.py`
- Add a `requirements.txt` and key-control instructions
- Add screenshots and automated tests for maze connectivity
- Handle display scaling and menu/restart states
