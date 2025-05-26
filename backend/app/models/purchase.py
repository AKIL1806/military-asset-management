from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    base_id = Column(Integer, ForeignKey("bases.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    purchase_date = Column(DateTime(timezone=True), server_default=func.now())
    purchased_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    notes = Column(String, nullable=True)
