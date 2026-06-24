from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.models as models
import schemas.schemas as schemas

router = APIRouter()


@router.post("/tasks/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        user_id=task.user_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task