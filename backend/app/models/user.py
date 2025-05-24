from sqlalchemy import Column, Integer, String, Enum
from app.core.db import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    commander = "commander"
    logistics = "logistics"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
