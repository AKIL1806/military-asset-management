from sqlalchemy import Column, Integer, String, Enum
from app.core.db import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)      # changed from username to name
    email = Column(String(120), unique=True, nullable=False, index=True)  # added email
    hashed_password = Column(String(128), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user, nullable=False)
