from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.asset_schema import AssetCreate, AssetOut
from app.models.asset import Asset
from app.core.db import get_db

router = APIRouter()

@router.post("/", response_model=AssetOut, status_code=status.HTTP_201_CREATED)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    db_asset = Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.get("/", response_model=List[AssetOut])
def list_assets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    assets = db.query(Asset).offset(skip).limit(limit).all()
    return assets

@router.get("/{asset_id}", response_model=AssetOut)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

# Add update and delete routes as needed...
