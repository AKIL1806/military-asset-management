from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    asset_id: int
    from_base_id: int
    to_base_id: int
    quantity: int
    transfer_date: Optional[datetime] = None
    status: Optional[str] = "pending"
    initiated_by: Optional[int] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int

    class Config:
        from_attributes = True

# ✅ Aliases for API-specific naming
TransferCreate = TransactionCreate
TransferOut = TransactionOut
