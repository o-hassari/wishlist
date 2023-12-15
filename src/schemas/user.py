from pydantic import BaseModel, Field
from uuid import UUID



class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    birth_date: str
    email: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    email: str
    password: str

class UserAuth(BaseModel):
    email: str = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=64, description="user password")

class UserOut(BaseModel):
    id: UUID
    email: str


class SystemUser(UserOut):
    password: str