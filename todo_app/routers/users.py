from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request, Form
from starlette import status
from ..database import SessionLocal, engine

from .. import models
from .auth import get_current_user, get_password_hash, verify_password

from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="todo_app/templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/edit-password", response_class=HTMLResponse)
async def edit_user_view(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("edit-user-password.html", {"request": request, "user": user})


@router.post("/edit-password", response_class=HTMLResponse)
async def edit_password_change(request: Request, username: str = Form(...)
                               , password: str = Form(...),
                               password2: str = Form(...),
                               db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)

    user_data = db.query(models.User).filter(models.User.username == username).first()
    msg = 'Invalid username or password'

    if user_data is not None:
        if username == user_data.username and verify_password(password, user_data.hashed_password):
            user_data.hashed_password = get_password_hash(password2)
            db.add(user_data)
            db.commit()
            msg = 'Password updated'
    return templates.TemplateResponse('edit-user-password.html',
                                      {"request": request, "user": user, "msg": msg})
