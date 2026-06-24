from fastapi import APIRouter, Depends
from fastapi import HTTPException
from auth.auth import hash_password, verify_password, create_token
from sqlalchemy.orm import Session
from database import get_db
import models.models as models
import schemas.schemas as schemas

router = APIRouter()

@router.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)

    db_user = models.User(username=user.username, password=hashed)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Wrong password")

    token = create_token({"sub": user.username})

    return {"access_token": token}