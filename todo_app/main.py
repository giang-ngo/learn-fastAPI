from fastapi import FastAPI
from todo_app import models
from todo_app.database import engine
from todo_app.routers import auth, todos

app = FastAPI()

print("Creating tables...")
models.Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

app.include_router(auth.router)
app.include_router(todos.router)
