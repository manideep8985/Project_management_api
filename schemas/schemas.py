from pydantic import BaseModel

# ✅ USER SCHEMAS
class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# ✅ PROJECT SCHEMAS
class ProjectCreate(BaseModel):
    name: str
    description: str
    owner_id: int


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


# ✅ TASK SCHEMAS
class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    user_id: int


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    priority: str

    class Config:
        orm_mode = True