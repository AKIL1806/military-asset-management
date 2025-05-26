from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AssignmentCreate(BaseModel):
    asset_id: int
    assigned_to: str
    quantity: int
    date: str  # Format: "YYYY-MM-DD"
    expended: bool


class AssignmentOut(AssignmentCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
