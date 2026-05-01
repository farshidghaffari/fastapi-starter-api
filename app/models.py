"""
Application data models.
"""

from pydantic import BaseModel


class Task(BaseModel):
    """Internal task model."""

    id: int
    title: str
    description: str | None = None
    completed: bool = False
