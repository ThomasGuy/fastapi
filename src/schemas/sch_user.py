import uuid
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class Post(BaseModel):
    id: int
    caption: str

    class Config:
        from_attributes = True


class UserDisplay(BaseModel):
    id: uuid.UUID
    public_id: uuid.UUID
    username: str
    email: str
    admin: bool
    items: List[Post] = []

    class Config:
        from_attributes = True
