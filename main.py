from fastapi import FastAPI, HTTPException
from models import UserCreate, User
import crud

app = FastAPI()

@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    return crud.create_user(user)

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
