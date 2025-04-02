from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, unique=True)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    user_id = Column(String, ForeignKey('user.public_id'))
    user = relationship('User', back_populates='items')

    comments = relationship('Comment', back_populates='post')
