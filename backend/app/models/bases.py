from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class BaseModel(Base):
    __tablename__ = 'bases'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    assets = relationship("Asset", back_populates="base")
