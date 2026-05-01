# Usage Guide

## Run the API

From the project root:

```bash
uvicorn app.main:app --reload
```

## Open API Docs

FastAPI automatically creates interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Example Endpoints

### Health Check

```bash
curl http://127.0.0.1:8000/
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

### Get Task by ID

```bash
curl http://127.0.0.1:8000/tasks/1
```

### Delete Task

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

## Suggested Improvements

- Add update task endpoint
- Add SQLite database
- Add user authentication
- Add unit tests
- Add Dockerfile
- Add deployment instructions
