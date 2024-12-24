from sqlalchemy import create_engine, text, StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
import pytest
from ..main import app
from fastapi.testclient import TestClient
from ..models import Todo, User
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = 'sqlite:///./testdb.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)


@pytest.fixture
def test_todo():
    todo = Todo(
        title='Learn to code!',
        description='Need to learn everyday!',
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'giangngo', 'id': 1, 'user_role': 'admin'}


@pytest.fixture
def test_user():
    user = User(
        username='giangngo',
        email='giangngo@gmail.com',
        first_name='Giang',
        last_name='Ngo',
        hashed_password=bcrypt_context.hash('testpassword'),
        role='admin',
        phone_number='0123456789'
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
