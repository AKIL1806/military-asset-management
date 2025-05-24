from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # weapon, vehicle, etc.
    quantity = Column(Integer, default=0)
    base_id = Column(Integer, nullable=False)
