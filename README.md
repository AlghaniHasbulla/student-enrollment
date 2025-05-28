# 🎓 Student Course Enrollment System (CLI + ORM)

A simple command-line interface (CLI) application built with **Python**, **SQLAlchemy ORM**, and **Click**, designed to simulate a student course enrollment system.

## 🧠 Purpose

This project allows users to:
- Add students
- Add courses
- Enroll students in courses
- View enrolled courses for any student

It demonstrates proficiency in:
- CLI application development
- SQLAlchemy ORM usage
- Proper Python package structure
- Database design and management
- Use of lists, dictionaries, and tuples
- Virtual environment setup using Pipenv

---

## 🛠️ Tech Stack

- **Python 3.x**
- **SQLAlchemy ORM** – For database modeling and interaction
- **Click** – For building the CLI interface
- **Pipenv** – For managing virtual environments
- **SQLite** – As the backend database

---

## 📦 Folder Structure
student_enrollment/
├── enrollment/
│ ├── init .py
│ ├── cli.py # CLI commands and interface
│ ├── models.py # SQLAlchemy ORM models
│ ├── database.py # Database connection setup
│ └── helpers.py # Optional helper functions
├── migrations/ # Placeholder for future Alembic migrations
├── Pipfile # Pipenv dependency file
├── README.md # This file
├── setup.py # Package configuration
└── create_db.py # Script to initialize the database
---

## 🧪 Features

1. **Add Student**
   ```bash
   enrollment add-student --name "Alice" --email "alice@example.com"

2. *** Add course ***  
  ---bash
 enrollment add-course --title "Intro to Python" --description "Learn basics of Python programming."
 3. *** Enroll student in course ***
 ---bash
enrollment enroll --student-name "Alice" --course-title "Intro to Python"
4. *** View enrolled courses for any student ***
---bash
enrollment view-enrolled --student-name "Alice"

5. **Setup Instructions**
---bash
git clone https://github.com/yourusername/student-enrollment.git 
cd student-enrollment

6. **install dependacies with pipenv**
---bash
pip install pipenv
pipenv install click sqlalchemy
pipenv shell

7. **install the app in development mode**
pip install -e .

8. **run the app**
enrollment --help

9.  **create the database and tables**
python create_db.py

10. **run migrations**
alembic upgrade head


### Next Steps

commit it to github:

```bash
git add README.md
git commit -m "completed functionality and setup"