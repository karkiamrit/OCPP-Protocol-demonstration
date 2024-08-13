from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    username: str
    email: str
    role: str

class UserInDB(User):
    hashed_password: str

class Role(BaseModel):
    name: str
    permissions: List[str]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    role: str
