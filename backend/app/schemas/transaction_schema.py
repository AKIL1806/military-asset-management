from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    asset_id: int
    type: str
    quantity: int
    from_base_id: Optional[int] = None
    to_base_id: Optional[int] = None
    performed_by: int

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
