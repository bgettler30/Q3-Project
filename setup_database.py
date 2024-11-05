import sqlite3

def setup_database():
    connection = sqlite3.connect("quiz_bowl.db")
    cursor = connection.cursor()

    courses = [
        'Intermediate_Financial_Management', 
        'Fundamentals_of_Investment', 
        'Computer_Forensics', 
        'Business_Analytics', 
        'Business_Application_Development'
    ]

    for course in courses:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {course} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT UNIQUE,        -- Ensures each question is unique
            choice_a TEXT,
            choice_b TEXT,
            choice_c TEXT,
            choice_d TEXT,
            correct_answer TEXT,
            feedback TEXT
        )
        """)

    connection.commit()
    connection.close()
    
setup_database()
print("Database and tables created successfully!")
