from datetime import datetime, timezone

from sqlalchemy.orm import Session

from src.database.models import Comment
from src.schemas.sch_comment import CommentBase


def create_comment(request: CommentBase, db: Session):
    new_comment = Comment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now(timezone.utc),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(post_id: int, db: Session):
    data = db.query(Comment).filter(Comment.post_id == post_id).all()
    return sorted(data, key=lambda c: c.timestamp)  # type: ignore
