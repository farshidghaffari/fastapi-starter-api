"""
FastAPI Starter API

A simple task management API built with FastAPI.
"""

from fastapi import FastAPI, HTTPException, status

from app.database import tasks_db
from app.models import Task
from app.schemas import TaskCreate, TaskResponse


app = FastAPI(
    title="FastAPI Starter API",
    description="A beginner-friendly FastAPI project for learning Python backend development.",
    version="1.0.0",
)


@app.get("/")
def health_check() -> dict:
    """Return a simple health check response."""
    return {
        "status": "ok",
        "message": "FastAPI Starter API is running.",
    }


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks() -> list[Task]:
    """Return all tasks."""
    return list(tasks_db.values())


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    """Create a new task."""
    task_id = len(tasks_db) + 1

    task = Task(
        id=task_id,
        title=task_data.title,
        description=task_data.description,
        completed=False,
    )

    tasks_db[task_id] = task

    return task


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int) -> Task:
    """Return a task by ID."""
    task = tasks_db.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found.",
        )

    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict:
    """Delete a task by ID."""
    task = tasks_db.pop(task_id, None)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found.",
        )

    return {
        "message": "Task deleted successfully.",
        "deleted_task": task,
    }
