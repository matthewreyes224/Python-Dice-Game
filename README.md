# Python Dice Game

A command-line Python guessing game built to practice core programming concepts including functions, loops, conditionals, input validation, exception handling, and random number generation.

## Features

- Random number generation from 1 to 100
- Three difficulty levels:
  - Easy: 15 attempts
  - Medium: 10 attempts
  - Hard: 5 attempts
- Input validation for guesses and menu selections
- Higher/lower feedback after incorrect guesses
- Remaining-attempt tracking
- Replay option after each game
- ESC key support to exit during a guess

## Technologies

- Python 3
- Python standard library
  - `random`
  - `msvcrt`
  - `sys`

## How to Run

1. Clone or download this repository.
2. Open the project in Visual Studio, Visual Studio Code, or another Python IDE.
3. Run:

```bash
python main.py
```

4. Press **ENTER** to start the game.
5. Select a difficulty and begin guessing.

> Note: The ESC-key exit feature uses Python's `msvcrt` module and is designed for Windows.

## What I Practiced

This project helped reinforce:

- Creating and calling functions
- Using `while` loops
- Building menu systems
- Validating user input
- Using `try` / `except`
- Working with conditional logic
- Managing game state with variables
- Generating random values
- Structuring a small Python program into reusable functions

## Future Improvements

Possible future additions include:

- Score tracking
- Best-score history
- Additional game modes
- Cross-platform keyboard handling
- Graphical user interface
