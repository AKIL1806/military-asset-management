from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.sql import func
from app.core.db import Base

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    from_base_id = Column(Integer, ForeignKey("bases.id"), nullable=False)
    to_base_id = Column(Integer, ForeignKey("bases.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    transfer_date = Column(DateTime(timezone=True), server_default=func.now())
    transferred_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    notes = Column(String, nullable=True)
