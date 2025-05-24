from pydantic import BaseModel
from typing import Optional

class AssetCreate(BaseModel):
    name: str
    description: Optional[str] = None
    type: Optional[str] = "Unknown"
    status: Optional[str] = "Inactive"

class AssetResponse(BaseModel):
    id: int
    name: str
    type: str
    status: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
