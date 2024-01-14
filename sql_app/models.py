from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Tea(Base):
    __tablename__ = "tea"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)


