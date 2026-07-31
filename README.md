# Task Manager – Flask REST API + Bootstrap Frontend

A full-stack task management app. Backend REST API built with Flask and
SQLAlchemy; frontend built with HTML, Bootstrap, and vanilla JavaScript
using `fetch()` to consume the API.

## Features
- Create, read, update, and delete tasks (full CRUD)
- Mark tasks as complete/incomplete
- REST API endpoints returning JSON
- SQLite database (easily switchable to MySQL)
- Responsive Bootstrap UI

## Tech Stack
- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (fetch API)
- **Database:** SQLite (default) / MySQL (optional)

## API Endpoints
| Method | Endpoint             | Description         |
|--------|-----------------------|----------------------|
| GET    | /api/tasks             | Get all tasks        |
| GET    | /api/tasks/<id>         | Get a single task     |
| POST   | /api/tasks             | Create a new task     |
| PUT    | /api/tasks/<id>         | Update a task         |
| DELETE | /api/tasks/<id>         | Delete a task         |

## Setup Instructions
```bash
pip install -r requirements.txt
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

## Switching to MySQL
Install the driver:
```bash
pip install pymysql
```
Update the URI in `app.py`:
```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/task_manager_db"
```

## Author
Manthan Sahu
