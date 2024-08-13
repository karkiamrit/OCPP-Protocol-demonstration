from typing import Optional
from app.auth.models import UserInDB
from app.auth.security import get_password_hash, verify_password
from app.auth.schemas import UserCreate

# Dummy in-memory user store (Replace with your actual database logic)
db_users = {}

def create_user(user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        id=len(db_users) + 1,
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db_users[db_user.id] = db_user
    return db_user

def get_user(username: str) -> Optional[UserInDB]:
    for user in db_users.values():
        if user.username == username:
            return user
    return None

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user(username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
