from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.models.purchase import Purchase
from app.schemas.purchase_schema import PurchaseCreate, PurchaseOut
from app.core.db import get_db

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=PurchaseOut, status_code=status.HTTP_201_CREATED)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = Purchase(**purchase.model_dump())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@router.get("/", response_model=List[PurchaseOut])
def list_purchases(db: Session = Depends(get_db)):
    return db.query(Purchase).all()
