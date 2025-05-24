from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from app.core.db import Base
import enum

class TransactionType(str, enum.Enum):
    purchase = "purchase"
    transfer_in = "transfer_in"
    transfer_out = "transfer_out"
    assignment = "assignment"
    expended = "expended"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    transaction_type = Column(Enum(TransactionType), nullable=False)
    quantity = Column(Integer, nullable=False)
    source_base = Column(String, nullable=True)
    destination_base = Column(String, nullable=True)
    personnel = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
