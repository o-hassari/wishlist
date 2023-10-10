from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: int
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