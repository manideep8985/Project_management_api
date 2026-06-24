from fastapi import FastAPI, Depends
from database import engine
import models.models as models
from fastapi.security import OAuth2PasswordBearer
from auth.auth import get_current_user

from routers import user, project, task

app = FastAPI()

# ✅ ADD THIS LINE (this was missing)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# create tables
models.Base.metadata.create_all(bind=engine)

# include routers
app.include_router(user.router)
app.include_router(project.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {"message": "Project Management API running 🚀"}

@app.get("/secure")
def secure(token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)

    return {
        "message": "You are logged in ✅",
        "user": user.username
    }