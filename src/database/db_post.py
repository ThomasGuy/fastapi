from datetime import datetime, timezone
from pathlib import Path

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.database.models.post import Post
from src.schemas import PostBase

imgFolder = Path.cwd() / 'src' / 'images'


def create_post(request: PostBase, db: Session):
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.user_id,
        timestamp=datetime.now(timezone.utc),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    data = db.query(Post).all()
    return sorted(data, key=lambda p: p.timestamp, reverse=True)  # type: ignore


def delete_post(id: int, db: Session, user_id: str):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} not found'
        )
    if post.user_id != user_id:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='you can only delete your own posts',
        )
    db.delete(post)
    db.commit()

    if post.image_url_type == 'relative':  # type: ignore
        file = post.image_url.split('/')[-1]
        filename = imgFolder / file
        filename.unlink()
    return 'ok'
