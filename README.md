# Full Stack Book To Do FastAPI

Terminal

```
mkdir fullstackbook-todo-fastapi
cd fullstackbook-todo-fastapi
python3 -m venv venv
. venv/bin/activate
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
createdb fullstackbook-todo-fastapi
pip install alembic psycopg2
alembic init alembic
alembic revision -m "create todos table"
alembic upgrade head
alembic downgrade -1
psql fullstackbook-todo-fastapi
pytest
```