from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal, engine

router = APIRouter(
    prefix="/todos"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search", response_model=List[schemas.ToDoResponse])
def search_todos(q: str, db: Session = Depends(get_db)):
    todos = crud.search_todos(db, q)
    return todos

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.create_todo(db, todo)
    return todo

@router.get("/", response_model=List[schemas.ToDoResponse])
def get_todos(db: Session = Depends(get_db)):
    todos = crud.read_todos(db)
    return todos

@router.get("/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.put("/{id}")
def update_todo(id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session = Depends(get_db)):
    res = crud.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="to do not found")