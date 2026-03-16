LMS Project - Developer Setup Guide

Welcome to the LMS Project! This guide acts as the definitive manual for setting up the development environment. **Please follow these steps exactly in order** to ensure the project runs correctly on your local machine.

1. Prerequisites
Before proceeding, ensure the following software is installed:
1.  **Python** (3.10 or higher) - [Download Here](https://www.python.org/downloads/)
    * *Critical:* During installation, ensure you check the box **"Add Python to PATH"**.
2.  **XAMPP** (for MySQL Database) - [Download Here](https://www.apachefriends.org/index.html)
3.  **VS Code** (Recommended Code Editor)
4.  **Git** (For version control)

2. Project Installation

### Step 1: Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Git Bash) and run:
```bash
git clone https://github.com/premzumble/mylms.git 
cd lms

Virtual environment to isolate project dependencies from your system - 

# Create the environment named 'env'
python -m venv env

# Activate the environment
# Windows:
.\env\Scripts\activate

Install all required libraries (Django, MySQL connector, etc.) using the requirements.txt file provided in the repo.
pip install -r requirements.txt

3. Database Setup (Crucial!)
IMPORTANT: Do NOT rely on python manage.py migrate. That command builds empty tables. We need the actual data (Admin user, Roles, etc.) to log in.

Open XAMPP Control Panel and start Apache and MySQL.

Open your browser and go to: http://localhost/phpmyadmin

Click New (left sidebar) -> Create a database named exactly: mylms

Click Import (top navigation bar).

Choose the file mylms_backup.sql (located in the project root folder).

Click Go (bottom right).

4. Configuration 
Open the file lms/settings.py (inside the inner project folder). Scroll to the DATABASES section and verify it matches your XAMPP settings:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mylms',       # Must match the DB name you created
        'USER': 'root',        # Default XAMPP User
        'PASSWORD': '',        # Default XAMPP Password is empty
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

5. To run project
python manage.py runserver

6. Rules to follow
New Libraries: If you install a new package (e.g., pandas), you MUST run pip freeze > requirements.txt and commit the file so others can use it.

Database Changes: Since our models are managed = False (I have already changed it to true but if you got any error, do check the the models file first), do not use makemigrations to change the DB structure. Make changes in phpMyAdmin and share a new SQL export.
