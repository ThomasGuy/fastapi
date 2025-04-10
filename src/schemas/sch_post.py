from datetime import datetime
from typing import List

from pydantic import BaseModel


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    user_id: str


class User(BaseModel):
    username: str

    class Config:
        from_attributes = True


class Comment(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        from_attributes = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        from_attributes = True


class Path(BaseModel):
    filename: str
