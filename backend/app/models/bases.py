from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.db import Base

class BaseLocation(Base):
    __tablename__ = "bases"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String, nullable=True)

    assets = relationship("Asset", back_populates="base")
