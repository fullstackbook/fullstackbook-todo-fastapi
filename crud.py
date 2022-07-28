from sqlalchemy.orm import Session
import models, schemas

def search_todos(db: Session, q: str):
    return db.query(models.ToDo).filter(models.ToDo.name.ilike(f"%{q}%")).all()

def create_todo(db: Session, todo: schemas.ToDoRequest):
    db_todo = models.ToDo(name=todo.name, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def read_todos(db: Session):
    return db.query(models.ToDo).all()

def read_todo(db: Session, id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == id).first()

def update_todo(db: Session, id: int, todo: schemas.ToDoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).update({'name': todo.name, 'completed': todo.completed})
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).delete()
    db.commit()
    return True