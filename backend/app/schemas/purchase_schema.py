from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PurchaseBase(BaseModel):
    asset_id: int
    quantity: int
    price_per_unit: float

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseOut(PurchaseBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
