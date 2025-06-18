from uuid import uuid4
from models import UserCreate, User
from typing import Dict

# In-memory user store
users: Dict[str, User] = {}

def create_user(user_data: UserCreate) -> User:
    user_id = str(uuid4())
    new_user = User(id=user_id, **user_data.dict())
    users[user_id] = new_user
    return new_user

def get_user(user_id: str) -> User | None:
    return users.get(user_id)
