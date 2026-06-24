from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models.models as models
import schemas.schemas as schemas

router = APIRouter()


@router.post("/projects/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(
        name=project.name,
        description=project.description,
        owner_id=project.owner_id,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project