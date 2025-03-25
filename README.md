Django Multi-App Project

Overview

This project is a collection of Django applications demonstrating key features of the framework. Instead of just displaying static HTML and CSS, it dynamically generates content based on user input, URL parameters, and session data. Each app in this project showcases a different Django capability.

Features
✅ Dynamic Web Pages: Generates personalized responses based on URL parameters (e.g., greeting users by name).
✅ Session-Based Data Storage: Saves user-specific information, such as a to-do list, persisting across visits.
✅ Conditional Rendering: Adjusts content based on real-world conditions (e.g., checking if it's New Year's Day).
✅ Modular Django Apps: The project consists of multiple Django apps, each demonstrating a unique feature.

Project Structure

django-multi-app/
│── tasks/                # To-Do List App
│   ├── migrations/       # Database migrations
│   ├── templates/tasks/  # HTML templates for tasks
│   ├── static/tasks/     # Static files (CSS, JS)
│   ├── views.py          # Views for handling tasks
│   ├── urls.py           # URL routing for tasks
│   ├── models.py         # Data models (if added later)
│   ├── forms.py          # Django forms for task submission
│
│── newyear/              # New Year Checker App
│   ├── templates/newyear/ # HTML templates for newyear
│   ├── views.py          # Views for checking the date
│   ├── urls.py           # URL routing for newyear
│
│── hello/                # Personalized Greeting App
│   ├── templates/hello/  # HTML templates for greetings
│   ├── views.py          # Views for dynamic greetings
│   ├── urls.py           # URL routing for hello
│
│── project/              # Main Django Project
│   ├── settings.py       # Project settings
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py           # WSGI entry point for deployment
│   ├── asgi.py           # ASGI entry point for async capabilities
│
│── templates/            # Global templates (if needed)
│── static/               # Global static files
│── db.sqlite3            # SQLite database
│── manage.py             # Django's command-line utility
│── requirements.txt      # Dependencies list
│── README.md             # Project documentation

Apps Included:

Hello App – Displays a dynamic greeting based on the name provided in the URL.
New Year App – Checks the current date and renders different content if it's New Year's Day.
Tasks App – Implements a simple to-do list using Django’s session storage to track tasks per user.
Installation

Prerequisites
Ensure you have the following installed:
Python 3.x
Django
Virtual environment (optional but recommended)


Setup
Clone this repository:
git clone 
cd 

Create and activate a virtual environment:
python3 -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate  # On Windows  

Install dependencies:
pip install -r requirements.txt  

Run database migrations:
python manage.py migrate  

Start the development server:
python manage.py runserver  

Open your browser and visit:
http://127.0.0.1:8000/hello/yourname/ – Dynamic greeting
http://127.0.0.1:8000/newyear/ – New Year checker
http://127.0.0.1:8000/tasks/ – To-do list
Next Steps

Extend the apps with database integration instead of session storage.
Add authentication to personalize user experiences.
Improve the UI with CSS frameworks like Bootstrap.
