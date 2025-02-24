from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from .core import security
from . import crud, schemas
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    idUser = security.decode_token(token)
    if not idUser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = crud.get_usuario_by_id(db, idUser=idUser)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user

async def get_current_active_user(current_user: schemas.UsuarioResponse = Depends(get_current_user)):
    return current_user