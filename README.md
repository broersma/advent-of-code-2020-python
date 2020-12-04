# Advent of Code 2020

Python solutions to [Advent of Code 2020](http://adventofcode.com/2020).

## Install

`pip install -r requirements.txt`

## Run

`python <day>_<star>.py`

## Run tests (if available)

`python -m doctest <day>_<star>.py`

## Employing Little Helper for competitive coding

Little Helper :elf: (`little_helper.py`) retrieves the puzzle input and submits solutions for you. Instructions:

1. Create a file called `cookie.txt`. It :warning:**should be in your `.gitignore`**:warning: and contain `session=<your advent of code session id>`.
2. For each day:
   1. Copy `template.py` to a file called `<day>_<star>.py` in advance (e.g., for star 1 of day 15, use `15_1.py`).
   2. Once the puzzle is up, modify the `answer` function according to the online instructions as often as necessary.
      * Run the file using `python <day>_<star>.py` to see the current return value of `answer` based on your puzzle input (Little Helper will download and cache the input for you in a file called `day<day>.txt`).
      * Check any doctests you write with `python -m doctest <day>_<star>.py`.
   3. Submit your current answer with `python <day>_<star>.py -s`.
      * If this was an answer for the first star and it was correct, Little Helper automatically copies `<day>_1.py` to `<day_2.py`, opens the new file in [Notepad++](https://notepad-plus-plus.org) and redirects your webbrowser to the new instructions for the second star on the Advent of Code website.
