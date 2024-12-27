import os
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path, Request, Form
from starlette import status
from ..database import SessionLocal
from ..models import Todo
from .auth import get_current_user
from .. import models
from ..database import engine
from starlette.responses import RedirectResponse

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
)
models.Base.metadata.create_all(bind=engine)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../templates"))
templates = Jinja2Templates(directory="todo_app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', response_class=HTMLResponse)
async def read_all_by_user(request: Request, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todos = db.query(models.Todo).filter(models.Todo.owner_id == user.get('id')).all()
    return templates.TemplateResponse("home.html", {"request":
                                                        request, 'todos': todos, 'user': user})


@router.get('/add-todo', response_class=HTMLResponse)
async def add_new_todo(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("add-todo.html",
                                      {"request": request, 'user': user})


@router.post('/add-todo', response_class=HTMLResponse)
async def create_todo(request: Request, title: str = Form(...), description: str = Form(...)
                      , priority: int = Form(...), db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todo_model = models.Todo(title=title, description=description,
                             priority=priority, complete=False, owner_id=user.get('id'))

    # todo_model = models.Todo()
    # todo_model.title = title
    # todo_model.description = description
    # todo_model.priority = priority
    # todo_model.complete = False
    # todo_model.owner_id = user.get('id')

    db.add(todo_model)
    db.commit()
    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


@router.get('/edit-todo/{todo_id}', response_class=HTMLResponse)
async def edit_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return templates.TemplateResponse("edit-todo.html", {"request": request, 'todo': todo, 'user': user})


@router.post('/edit-todo/{todo_id}', response_class=HTMLResponse)
async def edit_todo_commit(request: Request, todo_id: int,
                           title: str = Form(...)
                           , description: str = Form(...)
                           , priority: int = Form(...), db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todo_model = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority

    db.add(todo_model)
    db.commit()

    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


@router.get('/delete/{todo_id}')
async def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    # todo_model = db.query(models.Todo).filter(models.Todo.id == todo_id) \
    #     .filter(models.Todo.owner_id == 1).first()

    todo_model = db.query(models.Todo).filter(
        models.Todo.id == todo_id,
        models.Todo.owner_id == user.get('id')
    ).first()

    if todo_model is None:
        return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)

    db.query(models.Todo).filter(models.Todo.id == todo_id).delete()
    db.commit()
    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


@router.get('/complete/{todo_id}', response_class=HTMLResponse)
async def complete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    todo.complete = not todo.complete

    db.add(todo)
    db.commit()

    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)
