from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, database, dependencies

router = APIRouter(
    prefix="/dizimos",
    tags=["Dizimos"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

@router.post("/", response_model=schemas.DizimoResponse)
def create_dizimo(dizimo: schemas.DizimoCreate, db: Session = Depends(database.get_db)):
    return crud.criar_dizimo(db, dizimo)

@router.get("/{idDizimo}", response_model=schemas.DizimoResponse)
def read_dizimo(idDizimo: int, db: Session = Depends(database.get_db)):
    db_dizimo = crud.get_dizimo(db, idDizimo=idDizimo)
    if db_dizimo is None:
        raise HTTPException(status_code=404, detail="Dizimo not found")
    return db_dizimo

@router.get("/", response_model=List[schemas.DizimoResponse])
def read_dizimos(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    dizimos = crud.listar_dizimos(db, skip=skip, limit=limit)
    return dizimos

@router.put("/{idDizimo}", response_model=schemas.DizimoResponse)
def update_dizimo(idDizimo: int, dizimo: schemas.DizimoUpdate, db: Session = Depends(database.get_db)):
    db_dizimo = crud.atualizar_dizimo(db, idDizimo=idDizimo, dizimo=dizimo)
    if db_dizimo is None:
        raise HTTPException(status_code=404, detail="Dizimo not found")
    return db_dizimo

@router.delete("/{idDizimo}", response_model=bool)
def delete_dizimo(idDizimo: int, db: Session = Depends(database.get_db)):
    deleted = crud.remover_dizimo(db, idDizimo=idDizimo)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dizimo not found")
    return True