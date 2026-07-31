"""
Task Manager REST API
A Python Flask backend that exposes CRUD REST endpoints for managing tasks,
backed by a SQL database via SQLAlchemy. Serves a Bootstrap + vanilla JS
frontend that consumes the API using fetch().

Author: Manthan Sahu
"""

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# --------------------------------------------------------------------------
# Database Configuration
# By default this uses SQLite so the project runs with zero setup.
# To use MySQL instead, install PyMySQL/mysqlclient and change the URI to:
#   mysql+pymysql://<username>:<password>@localhost/task_manager_db
# --------------------------------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --------------------------------------------------------------------------
# Model
# --------------------------------------------------------------------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


# --------------------------------------------------------------------------
# Frontend route
# --------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------------------------------
# REST API Routes
# --------------------------------------------------------------------------
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([t.to_dict() for t in tasks]), 200


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict()), 200


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    task = Task(
        title=data.get("title"),
        description=data.get("description", ""),
        is_completed=data.get("is_completed", False),
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.is_completed = data.get("is_completed", task.is_completed)

    db.session.commit()
    return jsonify(task.to_dict()), 200


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
