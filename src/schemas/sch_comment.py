from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    text: str
    username: str
    post_id: int


class CommentDisplay(BaseModel):
    text: str
    post_id: int
    timestamp: datetime
