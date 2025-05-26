from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransferBase(BaseModel):
    asset_id: int
    from_base_id: int
    to_base_id: int
    quantity: int
    transferred_by: Optional[int] = None
    notes: Optional[str] = None

class TransferCreate(TransferBase):
    pass

class TransferOut(TransferBase):
    id: int
    transfer_date: datetime

    class Config:
        from_attributes = True
