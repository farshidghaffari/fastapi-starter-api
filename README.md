# FastAPI Starter API

A beginner-friendly FastAPI starter project by **Farshid Ghaffari**.

This repository demonstrates how to build a clean Python backend API using FastAPI, Pydantic models, and simple in-memory data storage.

## Purpose

The goal of this project is to show basic backend API structure with Python and FastAPI.

It includes:

- API health check
- Task list endpoint
- Create task endpoint
- Get task by ID endpoint
- Delete task endpoint
- Pydantic validation
- Clean project structure

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

Open in browser:

```text
http://127.0.0.1:8000
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
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

## Related Links

- Portfolio: https://farshidghaffari.net
- Services: https://farshidghaffari.net/services/
- Projects: https://farshidghaffari.net/projects/
- Blog: https://farshidghaffari.net/blog/

## Author

**Farshid Ghaffari**  
Python Developer focused on automation, backend APIs, data tools, and practical problem solving.
