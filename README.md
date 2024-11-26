# Quiz App - Python Intern Take-Home Assignment

## Overview
This project is a simple quiz app built using Django, allowing users to answer multiple-choice questions and track their performance. The app has two main pages:
1. **Dashboard Page** - Displays the user's performance.
2. **Quiz Page** - Displays random multiple-choice questions for the user to answer.

## Features
- **Dashboard Page:**
  - Displays total questions attempted.
  - Displays the number of correct answers.
  - Shows overall score or percentage.
  - A button to navigate to the **Quiz Page**.
  
- **Quiz Page:**
  - Displays one random multiple-choice question at a time.
  - Allows the user to select an answer and submit it.
  - Provides feedback (correct/incorrect) after submission.
  - Options to either:
    - **Answer More**: Load another random question.
    - **End Quiz**: Return to the Dashboard Page.

- **Database:**
  - All questions are pre-populated in a database (no user interface for question creation).
  - Random selection of questions for each quiz session.

## Requirements
- Python 3.x
- Django
- SQLite (or another database of your choice)

## Installation

To set up and run the project, follow these commands:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/quiz_project.git
cd quiz_project

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 5. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create a superuser (Optional, for admin access)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
