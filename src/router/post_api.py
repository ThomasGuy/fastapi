import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from src.auth.oauth2 import get_current_user
from src.database import db_post, get_db
from src.schemas import Path, PostBase, PostDisplay, UserAuth

router = APIRouter(prefix='/post', tags=['post'])

image_url_types = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(
    request: PostBase,
    db: Session = Depends(get_db),  # noqa: B008
    current_user: UserAuth = Depends(get_current_user),  # noqa: B008
):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='parameter image_url_type can only take values "absolute" or "relative"',
        )
    return db_post.create_post(request, db)


@router.get('/all', response_model=List[PostDisplay])
def get_all(db: Session = Depends(get_db)):  # noqa: B008
    return db_post.get_all(db)


@router.post('/image', response_model=Path)
def upload_file(
    image: UploadFile = File(...),  # noqa: B008
    current_user: UserAuth = Depends(get_current_user),  # noqa: B008
):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = ''
    if image.filename:
        filename = new.join(image.filename.rsplit('.', 1))
    path = f'src/images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}


@router.delete('/delete/{id}')
def delete(
    id: int,
    db: Session = Depends(get_db),  # noqa: B008
    current_user: UserAuth = Depends(get_current_user),  # noqa: B008
):
    return db_post.delete_post(id, db, current_user.public_id)
