# Student Management System

A simple menu-driven Student Management System built with Python and object-oriented programming (OOP).

## Features

- Add a student with a name, unique student ID, and marks
- Prevent duplicate student IDs
- Validate marks so they must be whole numbers between 0 and 100
- Search for a student by ID
- Display all registered students
- Check whether a student has passed or failed
- Exit through the menu

## Requirements

- Python 3

No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   Depending on your system, you may need to use `python3 main.py`.

## Pass/Fail Rule

- Marks of 50 or above: Pass
- Marks below 50: Fail

## Notes

Student records are stored in a Python list while the program is running. They are not saved to a file or database, so the records are cleared when the program exits.

## Concepts Practiced

- Classes and objects
- Constructors and instance attributes
- Methods
- Lists
- Functions
- Loops and conditional statements
- Input validation with `try`/`except`
- Searching with `next()`
