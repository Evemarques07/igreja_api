from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import crud, models, schemas
from ..core import security
from ..database import get_db
from typing import Optional

router = APIRouter(
    tags=["Auth"],
    prefix="/auth",
)

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_usuario_by_idMembro(db, idMembro=int(form_data.username))
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not security.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Buscar informações do membro
    membro = crud.buscar_membro(db, idMembro=user.idMembro)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro not found")

    # Buscar informações do cargo
    meals = crud.get_meal_by_membro(db, idMembro=user.idMembro)
    cargo_nome: str = "membro"  # Valor padrão
    if meals:
        meal = meals[0]  # Pega o primeiro registro de meal
        cargo = crud.get_cargo(db, idCargo=meal.idCargo)
        if cargo:
            cargo_nome = cargo.nomeCargo

    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={
            "sub": str(user.idUser),
            "nomeCompleto": membro.nomeCompleto,
            "idMembro": membro.idMembro,
            "cpf": membro.cpf,
            "cargo": cargo_nome,
        },
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=schemas.UsuarioResponse)
def create_user(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_usuario_by_idMembro(db, idMembro=usuario.idMembro)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario already registered")
    return crud.criar_usuario(db, usuario)