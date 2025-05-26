from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    base_id: Optional[int] = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
