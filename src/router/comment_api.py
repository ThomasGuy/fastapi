from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.oauth2 import get_current_user
from src.database import db_comment, get_db
from src.schemas.sch_auth import UserAuth
from src.schemas.sch_comment import CommentBase

router = APIRouter(prefix='/comment', tags=['comment'])


@router.get('/all/{post_id}')
def comment(post_id: int, db: Session = Depends(get_db)):  # noqa: B008
    return db_comment.get_all(post_id, db)


@router.post('')
def create(
    request: CommentBase,
    db: Session = Depends(get_db),  # noqa: B008
    current_user: UserAuth = Depends(get_current_user),  # noqa: B008
):
    return db_comment.create_comment(request, db)
