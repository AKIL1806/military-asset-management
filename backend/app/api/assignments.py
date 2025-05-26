from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.asset import Asset
from app.models.transactions import Assignment
from app.schemas.assignment_schema import AssignmentCreate, AssignmentOut
from datetime import datetime

router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.post("/", response_model=AssignmentOut)
def assign_asset(
    data: AssignmentCreate,
    db: Session = Depends(get_db),
    require_roles_dep=Depends(lambda: __import__('app.middleware.rbac_middleware').rbac_middleware.require_roles(["admin", "base_commander"]))
):
    from app.middleware.rbac_middleware import require_roles
    require_roles(["admin", "base_commander"])()

    asset = db.query(Asset).filter(Asset.id == data.asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    if asset.quantity < data.quantity:
        raise HTTPException(status_code=400, detail="Not enough asset quantity available")

    asset.quantity -= data.quantity

    assignment = Assignment(
        asset_id=data.asset_id,
        assigned_to=data.assigned_to,
        quantity=data.quantity,
        date=data.date,
        expended=data.expended,
        created_at=datetime.utcnow()
    )
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment

@router.get("/", response_model=List[AssignmentOut])
def get_assignments(
    db: Session = Depends(get_db),
    require_roles_dep=Depends(lambda: __import__('app.middleware.rbac_middleware').rbac_middleware.require_roles(["admin", "base_commander", "logistics_officer"]))
):
    from app.middleware.rbac_middleware import require_roles
    require_roles(["admin", "base_commander", "logistics_officer"])()
    return db.query(Assignment).all()
