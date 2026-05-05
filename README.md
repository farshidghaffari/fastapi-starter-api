# FastAPI Starter API

A clean and beginner-friendly FastAPI starter project by **Farshid Ghaffari**.

This repository demonstrates how to build a simple Python backend API using FastAPI, Pydantic validation, structured endpoints, and an in-memory data layer.

It is designed as a portfolio-ready backend example for clients or teams who need small APIs, internal tools, dashboards, or backend foundations for web and mobile applications.

## What This Project Demonstrates

- Python backend development
- FastAPI project structure
- REST API endpoint design
- Pydantic request and response validation
- HTTP error handling
- Interactive API documentation with Swagger UI
- Simple in-memory data storage
- Clean and readable starter code

## Use Case

This starter API can be adapted for:

- Task management APIs
- Admin dashboards
- Internal business tools
- Simple CRUD backends
- MVP backend services
- Mobile app backend prototypes
- Portfolio backend demonstrations

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
fastapi-starter-api/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
└── docs/
    └── usage.md
```

## API Features

This API includes:

- Health check endpoint
- Get all tasks
- Create a task
- Get a task by ID
- Delete a task by ID
- Request body validation
- Response models
- 404 error handling for missing tasks

## Quick Start

Clone the repository:

```bash
git clone https://github.com/farshidghaffari/fastapi-starter-api.git
cd fastapi-starter-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open the API in your browser:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{task_id}` | Get a task by ID |
| DELETE | `/tasks/{task_id}` | Delete a task by ID |

## Example Request

Create a task:

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Build a simple backend API"}'
```

Example response:

```json
{
  "id": 3,
  "title": "Learn FastAPI",
  "description": "Build a simple backend API",
  "completed": false
}
```

## Example Error Response

If a task does not exist:

```bash
curl http://127.0.0.1:8000/tasks/999
```

Response:

```json
{
  "detail": "Task not found."
}
```

## Important Note About Storage

This project uses an in-memory dictionary for simplicity. Data will reset when the server restarts.

For a real project, the data layer can be upgraded to:

- SQLite
- PostgreSQL
- MySQL
- SQLAlchemy
- SQLModel
- Alembic migrations

## Freelance Service Angle

This repository demonstrates the type of backend API work I can build:

> I can create clean Python APIs with FastAPI, request validation, structured endpoints, API documentation, and a clear foundation for dashboards, internal tools, or web applications.

## Related Portfolio Pages

- Portfolio: https://farshidghaffari.net
- Services: https://farshidghaffari.net/services/
- Projects: https://farshidghaffari.net/projects/
- Blog: https://farshidghaffari.net/blog/
- GitHub Profile: https://github.com/farshidghaffari

## Suggested Next Improvements

- Add update task endpoint
- Add SQLite or PostgreSQL database
- Add SQLAlchemy or SQLModel
- Add unit tests with pytest
- Add Dockerfile and Docker Compose
- Add authentication
- Add environment variables
- Add deployment instructions
- Add CI workflow with GitHub Actions

## Author

**Farshid Ghaffari**  
Python Developer focused on automation, backend APIs, data tools, and practical problem solving.

Website: https://farshidghaffari.net  
GitHub: https://github.com/farshidghaffari
