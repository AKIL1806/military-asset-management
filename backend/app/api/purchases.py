from fastapi import APIRouter
from typing import List
from app.schemas.purchase_schema import PurchaseOut, PurchaseCreate

router = APIRouter()

# Temporary in-memory "database"
purchases_db = []

@router.get("/", response_model=List[PurchaseOut])
def get_purchases():
    return purchases_db

@router.post("/", response_model=PurchaseOut)
def create_purchase(purchase: PurchaseCreate):
    new_id = len(purchases_db) + 1
    purchase_data = purchase.dict()
    purchase_data["id"] = new_id
    purchases_db.append(purchase_data)
    return purchase_data
