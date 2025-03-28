from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# TODO: els vostres test venen aqui
from crud import get_tasks, create_task
from models import Task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_get_tasks():
    db = TestingSessionLocal()
    task = Task(title="Test Task", description="This is a test")
    db.add(task)
    db.commit()
    tasks = get_tasks(db)
    assert len(tasks) == 1
    db.close()
