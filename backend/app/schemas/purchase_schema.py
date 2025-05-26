from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PurchaseBase(BaseModel):
    asset_id: int
    base_id: int
    quantity: int
    notes: Optional[str] = None
    purchased_by: Optional[int] = None

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseOut(PurchaseBase):
    id: int
    purchase_date: datetime

    class Config:
        from_attributes = True  # For Pydantic v2 compatibility
