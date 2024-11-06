# Q3-Project

Quiz Bowl Project
This project is a graphical user interface (GUI) quiz application built in Python. It includes a back-end database for storing questions, which users can answer through a user-friendly GUI. The quiz covers various topics represented by different tables in an SQLite database.

Project Structure
setup_database.py: Sets up the database with tables for each course.
manage_database.py: Provides functions to add, remove, and read questions from the database.
seed_database.py (optional): Script to populate the database with initial questions.
quiz_gui.py: The main GUI application where users select a quiz category, answer questions, and receive feedback.
Requirements
Python 3.x
SQLite3
Tkinter (comes with Python’s standard library)
Optional: DB Browser for SQLite or a similar tool for managing the database visually.
Setup Instructions
1. Database Setup
Run setup_database.py:

This script creates an SQLite database (quiz_bowl.db) with tables for each course.
Each table has fields for question text, answer choices (A, B, C, D), the correct answer, and feedback.

Verify Database Creation:

You should see quiz_bowl.db in your project directory.
Each table is created for a course, and the structure prevents duplicate questions.

2. Adding Questions
Use addtoDB.py to add, remove, or fetch questions from the database.

Adding Questions:

The add_question function allows you to insert questions into the database.
This function uses INSERT OR IGNORE to prevent duplicate questions from being added.
Removing Questions:

The remove_question function deletes a question based on its text from the specified course table.
Fetching Questions:

The fetch_questions function retrieves all questions from a specified course, useful for verifying the database content.

3. GUI Quiz Application
Run quiz_gui.py to launch the interactive quiz application. Users can select a quiz category, answer questions, and view their score at the end.
How It Works:

Category Selection: Users select a quiz category (course) to start.
Question Display: Questions are displayed one at a time, with answer choices (A, B, C, D).
Answer Submission: Users select an answer and submit it.
Feedback and Scoring: The application provides immediate feedback and tracks the score. At the end, users see their total score.

File Details
setup_database.py
This script creates an SQLite database with tables for each quiz category. Each table has the following structure:

id: Auto-incrementing primary key.
question_text: The question text.
choice_a, choice_b, choice_c, choice_d: Answer choices.
correct_answer: The correct choice (e.g., "A", "B").
feedback: Feedback for the correct answer.
manage_database.py
Contains functions for managing questions in the database:

add_question(course, question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback): Adds a question.
remove_question(course, question_text): Removes a question.
fetch_questions(course): Fetches all questions for a given course.
quiz_gui.py
This file is the main GUI for the quiz application. It includes:

Question Class: Represents each question with attributes for text, choices, correct answer, and feedback.
QuizApp Class: Manages the GUI layout, handles question display, and manages scoring.
Sample Code Usage
Setting Up the Database
Run setup_database.py once to set up the database:
Adding Questions (Example)
In manage_database.py, add sample questions to a course table:
Running the GUI Application
Start the GUI application for user interaction:
Notes
Database Management: If you want to reset or modify the database, rerun setup_database.py or use manage_database.py to add or remove specific questions.
Error Handling: Ensure questions are added accurately to avoid database duplicates or missing information.
Future Enhancements: You could add more categories, modify questions, or enhance the GUI with additional feedback features.
