from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.models.transfer import Transfer
from app.schemas.transfer_schema import TransferCreate, TransferOut
from app.core.db import get_db

router = APIRouter(prefix="/transfers", tags=["Transfers"])

@router.post("/", response_model=TransferOut, status_code=status.HTTP_201_CREATED)
def create_transfer(transfer: TransferCreate, db: Session = Depends(get_db)):
    db_transfer = Transfer(**transfer.model_dump())
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

@router.get("/", response_model=List[TransferOut])
def list_transfers(db: Session = Depends(get_db)):
    return db.query(Transfer).all()
