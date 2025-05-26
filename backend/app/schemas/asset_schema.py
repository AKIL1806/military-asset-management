from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssetBase(BaseModel):
    name: str
    type: str
    status: str
    quantity: int
    base_id: int
    description: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class AssetOut(AssetBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # For Pydantic v2
