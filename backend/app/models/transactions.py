from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base  # This must be SQLAlchemy's Base

class Transfer(Base):  # Correct: Use Base, not BaseModel
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    from_base_id = Column(Integer, ForeignKey("bases.id"), nullable=False)
    to_base_id = Column(Integer, ForeignKey("bases.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    transfer_date = Column(DateTime(timezone=True), server_default=func.now())
    initiated_by = Column(Integer, ForeignKey("users.id"))
    status = Column(String(20), default="pending")  # pending, completed, cancelled

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    assigned_to = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    expended = Column(Boolean, default=False)
    created_at = Column(DateTime)

    asset = relationship("Asset")
