from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserBase
from src.utils import Hash


def create_user(request: UserBase, db: Session):  # noqa: B008
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.get_password_hash(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with username {username} not found',
        )
    return user
