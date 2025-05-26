from app.core.db import Base, engine, SessionLocal

import app.models.bases
import app.models.asset
import app.models.user
import app.models.purchase
import app.models.transactions  # If you have this module

Base.metadata.create_all(bind=engine)

from app.models.bases import BaseLocation
from app.models.asset import Asset
from app.models.user import User

db = SessionLocal()

try:
    if db.query(BaseLocation).count() == 0:
        base = BaseLocation(name="Base Alpha", location="Sector 1")
        db.add(base)
        db.commit()
        db.refresh(base)

        user = User(username="admin", role="admin", hashed_password="test")
        db.add(user)
        db.commit()
        db.refresh(user)

        asset = Asset(name="Truck", type="vehicle", status="active", quantity=20, base_id=base.id)
        db.add(asset)
        db.commit()
finally:
    db.close()

print("Test data seeded!")
