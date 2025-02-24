from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, database, dependencies
from ..models import TipoEntrada

router = APIRouter(
    prefix="/entradas",
    tags=["Entradas"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

@router.post("/", response_model=schemas.EntradaResponse)
def create_entrada(entrada: schemas.EntradaCreate, db: Session = Depends(database.get_db)):
    try:
        entrada.tipo = TipoEntrada(entrada.tipo)  # Converte o valor para o enum
    except ValueError:
        raise HTTPException(status_code=400, detail="Tipo de entrada inválido")
    return crud.criar_entrada(db, entrada)

@router.get("/{idEntrada}", response_model=schemas.EntradaResponse)
def read_entrada(idEntrada: int, db: Session = Depends(database.get_db)):
    db_entrada = crud.get_entrada(db, idEntrada=idEntrada)
    if db_entrada is None:
        raise HTTPException(status_code=404, detail="Entrada not found")
    return db_entrada

@router.get("/", response_model=List[schemas.EntradaResponse])
def read_entradas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    entradas = crud.listar_entradas(db, skip=skip, limit=limit)
    return entradas

@router.put("/{idEntrada}", response_model=schemas.EntradaResponse)
def update_entrada(idEntrada: int, entrada: schemas.EntradaUpdate, db: Session = Depends(database.get_db)):
    try:
        if entrada.tipo:  # Verifica se o tipo foi fornecido na requisição
            entrada.tipo = TipoEntrada(entrada.tipo)  # Converte o valor para o enum
    except ValueError:
        raise HTTPException(status_code=400, detail="Tipo de entrada inválido")
    db_entrada = crud.atualizar_entrada(db, idEntrada=idEntrada, entrada=entrada)
    if db_entrada is None:
        raise HTTPException(status_code=404, detail="Entrada não encontrada")
    return db_entrada

@router.delete("/{idEntrada}", response_model=bool)
def delete_entrada(idEntrada: int, db: Session = Depends(database.get_db)):
    deleted = crud.remover_entrada(db, idEntrada=idEntrada)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entrada not found")
    return True