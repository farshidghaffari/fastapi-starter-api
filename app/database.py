"""
Simple in-memory database.

This project intentionally uses an in-memory dictionary to keep the example
beginner-friendly. In a real project, this would usually be replaced by a
database such as PostgreSQL, SQLite, or MySQL.
"""

from app.models import Task


tasks_db: dict[int, Task] = {
    1: Task(
        id=1,
        title="Learn FastAPI",
        description="Build a simple backend API with Python.",
        completed=False,
    ),
    2: Task(
        id=2,
        title="Create portfolio project",
        description="Add this API project to a GitHub portfolio.",
        completed=False,
    ),
}
