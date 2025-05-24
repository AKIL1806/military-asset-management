from pydantic import BaseModel

class AssetBase(BaseModel):
    name: str
    type: str
    quantity: int
    base_id: int

class AssetCreate(AssetBase):
    pass

class AssetOut(AssetBase):
    id: int

    class Config:
        orm_mode = True
