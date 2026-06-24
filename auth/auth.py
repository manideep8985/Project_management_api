from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from jose import JWTError, jwt
from database import SessionLocal
import models.models as models


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ Hash password
def hash_password(password: str):
    return pwd_context.hash(password)


# ✅ Verify password
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


# ✅ Create JWT token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        return None

    db = SessionLocal()
    user = db.query(models.User).filter(models.User.username == username).first()
    db.close()

    return user
