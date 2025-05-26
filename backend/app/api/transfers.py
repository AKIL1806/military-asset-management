from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.transactions import Transfer
from app.schemas.transaction_schema import TransferCreate, TransferOut
from app.core.db import get_db

router = APIRouter()

@router.post("/", response_model=TransferOut, status_code=status.HTTP_201_CREATED)
def create_transfer(transfer: TransferCreate, db: Session = Depends(get_db)):
    db_transfer = Transfer(**transfer.model_dump())
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

@router.get("/", response_model=list[TransferOut])
def list_transfers(db: Session = Depends(get_db)):
    return db.query(Transfer).all()
