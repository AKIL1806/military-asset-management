from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.db import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    type = Column(String, nullable=False)  # purchase, transfer_in, transfer_out, assigned, expended
    quantity = Column(Integer, nullable=False)
    from_base_id = Column(Integer, nullable=True)
    to_base_id = Column(Integer, nullable=True)
    performed_by = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
