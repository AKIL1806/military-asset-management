from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False, default="active")
    quantity = Column(Integer, nullable=False)
    base_id = Column(Integer, ForeignKey("bases.id"))
    description = Column(String(500), nullable=True)

    base = relationship("BaseLocation", back_populates="assets")
