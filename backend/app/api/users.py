from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.models.user import User
from app.schemas.user_schema import UserOut
from app.core.db import get_db

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
