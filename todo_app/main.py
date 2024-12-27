from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

# # Đường dẫn tuyệt đối tới thư mục "static"
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_DIR = os.path.join(BASE_DIR, "static")
#
# app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Mount thư mục tĩnh sử dụng đường dẫn tương đối
app.mount("/static", StaticFiles(directory="todo_app/static"), name="static")


@app.get('/')
async def root():
    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
