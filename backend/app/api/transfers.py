from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.transactions import Transfer
from app.schemas.transaction_schema import TransferCreate, TransferOut
from app.core.db import get_db

router = APIRouter()

@router.post("/", response_model=TransferOut)
async def create_transfer(transfer: TransferCreate, db: Session = Depends(get_db)):
    try:
        db_transfer = Transfer(**transfer.dict())
        db.add(db_transfer)
        db.commit()
        db.refresh(db_transfer)
        return db_transfer
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[TransferOut])
async def get_transfers(db: Session = Depends(get_db)):
    return db.query(Transfer).all()