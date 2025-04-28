from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth.oauth2 import create_access_token
from src.database import get_db
from src.database.models import User
from src.utils.hash import Hash

router = APIRouter(tags=['authentication'])


@router.post('/login')
def login(
    request: OAuth2PasswordRequestForm = Depends(),  # noqa: B008
    db: Session = Depends(get_db),  # noqa: B008
):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user with username {request.username} not found',
        )
    if not Hash.verify(user.password, request.password):  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'user with password {request.password} not valid',
        )
    access_token = create_access_token(data={'username': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.public_id,
        'username': user.username,
    }
