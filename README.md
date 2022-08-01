# Full Stack Book To Do FastAPI

## Setup

```
createdb fullstackbook-todo-fastapi
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Configuration

Copy `.env.example` to `.env`.

## Database Migrations

```
alembic init alembic
alembic revision -m "create todos table"
alembic upgrade head
alembic downgrade -1
```