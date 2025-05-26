from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    asset_id: int
    from_base_id: int
    to_base_id: int
    quantity: int
    status: Optional[str] = "pending"
    initiated_by: Optional[int] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    transfer_date: Optional[datetime] = None

    class Config:
        from_attributes = True  # For Pydantic v2; use orm_mode=True if on v1

# Aliases for Transfer endpoints (for clarity in API code)
TransferCreate = TransactionCreate
TransferOut = TransactionOut
