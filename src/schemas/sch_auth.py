from pydantic import BaseModel


class UserAuth(BaseModel):
    public_id: str
    username: str
    email: str
