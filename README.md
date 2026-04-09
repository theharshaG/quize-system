# quize-system

Quiz System (Python Project)
## Overview

This project is a simple command-line Quiz System implemented in Python. It loads questions from a JSON file, presents them to the user, evaluates answers, and calculates the final score. The result is saved in a separate JSON file for future reference.

## Features

Load questions from JSON file
Randomize question order
Display multiple-choice questions
Evaluate user answers
Calculate final score
Save result to file

## Technologies Used

Python
JSON (data storage)
Random module

Project Structure

quiz-system/
│
├── main.py
├── questions.json
├── result.json
└── README.md

## How to Run

install python (VS Code)
Ensure questions.json file exists with quiz data
Run the program: quiz system.py

## How It Works

Questions are stored in a JSON file (questions.json) in the format:
Each question contains:
question, options, and correct answer

When the program starts:
It loads all questions from the file
Questions are shuffled randomly

During quiz:
User selects an option number
The program checks if the answer is correct
Score is updated accordingly

At the end:
Final score is displayed
Result is saved in result.json file

## Future Improvements

Add timer for each question
Add difficulty levels
Store multiple quiz results
Add user login system
Convert to GUI application
Develop web version using Flask

## Author
Harsha G
Learning Python | Embedded Systems | IoT
