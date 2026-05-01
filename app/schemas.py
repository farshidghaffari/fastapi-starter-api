"""
Request and response schemas.
"""

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Schema for creating a new task."""

    title: str = Field(..., min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class TaskResponse(BaseModel):
    """Schema returned by the API."""

    id: int
    title: str
    description: str | None = None
    completed: bool
