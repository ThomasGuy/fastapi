import uuid
from datetime import datetime, timezone

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String

from src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    public_id = Column(String(100), unique=True, default=str(uuid.uuid4()))
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    registered_on = Column(DateTime, default=datetime.now(timezone.utc))
    password = Column(String)
    admin = Column(Boolean, default=False)

    items = relationship('Post', back_populates='user')
