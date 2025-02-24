from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models import TipoSaida

from .. import crud, models, schemas, database, dependencies

router = APIRouter(
    prefix="/saidas",
    tags=["Saidas"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

@router.post("/", response_model=schemas.SaidaResponse)
def create_saida(saida: schemas.SaidaCreate, db: Session = Depends(database.get_db)):
    try:
        saida.tipo = TipoSaida(saida.tipo)
    except ValueError:
        raise HTTPException(status_code=400, detail="Tipo de saida inválido")
    return crud.criar_saida(db, saida)

@router.get("/{idSaida}", response_model=schemas.SaidaResponse)
def read_saida(idSaida: int, db: Session = Depends(database.get_db)):
    db_saida = crud.get_saida(db, idSaida=idSaida)
    if db_saida is None:
        raise HTTPException(status_code=404, detail="Saida not found")
    return db_saida

@router.get("/", response_model=List[schemas.SaidaResponse])
def read_saidas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    saidas = crud.listar_saidas(db, skip=skip, limit=limit)
    return saidas

@router.put("/{idSaida}", response_model=schemas.SaidaResponse)
def update_saida(idSaida: int, saida: schemas.SaidaUpdate, db: Session = Depends(database.get_db)):
    try:
        if saida.tipo:  # Verifica se o tipo foi fornecido na requisição
            saida.tipo = TipoSaida(saida.tipo)
    except ValueError:
        raise HTTPException(status_code=400, detail="Tipo de saida inválido")
    db_saida = crud.atualizar_saida(db, idSaida=idSaida, saida=saida)
    if db_saida is None:
        raise HTTPException(status_code=404, detail="Saida não encontrada")
    return db_saida

@router.delete("/{idSaida}", response_model=bool)
def delete_saida(idSaida: int, db: Session = Depends(database.get_db)):
    deleted = crud.remover_saida(db, idSaida=idSaida)
    if not deleted:
        raise HTTPException(status_code=404, detail="Saida not found")
    return True