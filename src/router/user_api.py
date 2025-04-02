from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import db_user, get_db
from src.schemas import UserBase, UserDisplay

router = APIRouter(prefix='/user', tags=['user'])


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):  # noqa: B008
    return db_user.create_user(request, db)
