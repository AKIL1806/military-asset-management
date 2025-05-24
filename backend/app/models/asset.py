from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.db import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  
    base_name = Column(String, nullable=False)
    opening_balance = Column(Integer, default=0)
    closing_balance = Column(Integer, default=0)
