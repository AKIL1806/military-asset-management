from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.schemas.asset_schema import AssetCreate, AssetOut

router = APIRouter()

# Temporary in-memory store (until DB is integrated)
fake_db = [
    {"id": 1, "name": "Tank A", "type": "Vehicle", "status": "Active", "description": "Heavy battle tank"},
    {"id": 2, "name": "Drone X", "type": "UAV", "status": "Inactive", "description": "Recon drone"},
]

@router.get("/", response_model=List[AssetOut])
def get_assets():
    return fake_db

@router.post("/", response_model=AssetOut, status_code=201)
def create_asset(asset: AssetCreate):
    new_asset = {
        "id": len(fake_db) + 1,
        "name": asset.name,
        "type": "Unknown",
        "status": "Inactive",
        "description": asset.description
    }
    fake_db.append(new_asset)
    return new_asset
