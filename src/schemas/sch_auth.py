import uuid
from pydantic import BaseModel


class UserAuth(BaseModel):
    public_id: uuid.UUID
    username: str
    email: str
