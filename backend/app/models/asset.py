from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from app.models.base import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)  # vehicle, weapon, ammunition
    status = Column(String(20), nullable=False, default="active")
    quantity = Column(Integer, nullable=False)
    base_id = Column(Integer, ForeignKey("bases.id"))
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
