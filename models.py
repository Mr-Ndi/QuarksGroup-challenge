from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):
    id: str
    is_active: bool = True