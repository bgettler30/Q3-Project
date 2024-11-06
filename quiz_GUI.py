import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

DB_NAME = "quiz_bowl.db"

class Question:
    def __init__(self, question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback):
        self.question_text = question_text
        self.choices = {
            'A': choice_a,
            'B': choice_b,
            'C': choice_c,
            'D': choice_d
        }
        self.correct_answer = correct_answer
        self.feedback = feedback
        
def get_categories():
    return [
        "Intermediate_Financial_Management",
        "Fundamentals_of_Investment",
        "Computer_Forensics",
        "Business_Analytics",
        "Business_Application_Development"
    ]

def fetch_questions(category):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(f"SELECT question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback FROM {category}")
    questions = cursor.fetchall()
    connection.close()
    return questions

    questions = [Question(*data) for data in questions_data]
    return questions

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("400x300")

        self.create_category_selection_window()

    def create_category_selection_window(self):
        self.clear_window()
        tk.Label(self.root, text="Select a Category", font=("Helvetica", 16)).pack(pady=20)

        self.selected_category = tk.StringVar()
        self.selected_category.set("Choose a category")
        categories = get_categories()
        category_menu = tk.OptionMenu(self.root, self.selected_category, *categories)
        category_menu.pack(pady=10)

        start_button = tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz)
        start_button.pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_quiz(self):
        category = self.selected_category.get()
        if category == "Choose a category":
            messagebox.showwarning("Selection Error", "Please select a category.")
            return
        
        self.questions = fetch_questions(category)
        if not self.questions:
            messagebox.showinfo("No Questions", f"No questions found for {category}.")
            return

        self.current_question_index = 0
        self.score = 0
        self.create_quiz_window()


    def create_quiz_window(self):
        self.clear_window()
        self.display_question()

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        question_text, choice_a, choice_b, choice_c, choice_d, self.correct_answer, feedback = question_data

        tk.Label(self.root, text=question_text, font=("Helvetica", 14)).pack(pady=20)

        self.selected_answer = tk.StringVar()
        for choice in (("A", choice_a), ("B", choice_b), ("C", choice_c), ("D", choice_d)):
            tk.Radiobutton(self.root, text=choice[1], variable=self.selected_answer, value=choice[0]).pack(anchor="w")

        submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer)
        submit_button.pack(pady=20)

    def check_answer(self):
        selected = self.selected_answer.get()
        if selected == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the correct answer!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer was {self.correct_answer}.")

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.create_quiz_window()  
        else:
            self.end_quiz()  

    def end_quiz(self):
        self.clear_window()
        tk.Label(self.root, text=f"Quiz Complete!", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Your score: {self.score} out of {len(self.questions)}", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Back to Category Selection", command=self.create_category_selection_window).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
