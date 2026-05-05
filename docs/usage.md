# Usage Guide

This guide explains how to run and test the FastAPI Starter API.

## 1. Install Dependencies

From the project root:

```bash
pip install -r requirements.txt
```

## 2. Run the API

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 3. Open API Documentation

FastAPI automatically creates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 4. Test Endpoints with curl

### Health Check

```bash
curl http://127.0.0.1:8000/
```

Expected response:

```json
{
  "status": "ok",
  "message": "FastAPI Starter API is running."
}
```

### Get All Tasks

```bash
curl http://127.0.0.1:8000/tasks
```

### Create a Task

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Practice FastAPI", "description": "Create a clean backend API"}'
```

Example response:

```json
{
  "id": 3,
  "title": "Practice FastAPI",
  "description": "Create a clean backend API",
  "completed": false
}
```

### Get Task by ID

```bash
curl http://127.0.0.1:8000/tasks/1
```

### Delete Task

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

Example response:

```json
{
  "message": "Task deleted successfully.",
  "deleted_task": {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Build a simple backend API with Python.",
    "completed": false
  }
}
```

## 5. Test Validation

The `title` field is required. Sending an empty title should return a validation error:

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "", "description": "Invalid task"}'
```

This demonstrates Pydantic validation.

## 6. Current Limitations

This project is intentionally simple.

Current limitations:

- Data is stored in memory
- Data resets after server restart
- No authentication
- No update endpoint
- No database layer
- No automated tests yet

## 7. Suggested Improvements

Good next improvements:

- Add update task endpoint
- Add SQLite or PostgreSQL
- Add SQLAlchemy or SQLModel
- Add unit tests
- Add Dockerfile
- Add authentication
- Add deployment instructions
- Add environment variables
- Add CI with GitHub Actions

## 8. Recommended Client Workflow

For real backend API projects, the process usually looks like this:

1. Define the required entities and endpoints
2. Design request and response schemas
3. Build FastAPI routes
4. Add validation and error handling
5. Connect a real database
6. Add tests
7. Add deployment configuration
8. Document the API clearly
