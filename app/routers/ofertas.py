from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, database, dependencies

router = APIRouter(
    prefix="/ofertas",
    tags=["Ofertas"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

@router.post("/", response_model=schemas.OfertaResponse)
def create_oferta(oferta: schemas.OfertaCreate, db: Session = Depends(database.get_db)):
    return crud.criar_oferta(db, oferta)

@router.get("/{idOferta}", response_model=schemas.OfertaResponse)
def read_oferta(idOferta: int, db: Session = Depends(database.get_db)):
    db_oferta = crud.get_oferta(db, idOferta=idOferta)
    if db_oferta is None:
        raise HTTPException(status_code=404, detail="Oferta not found")
    return db_oferta

@router.get("/", response_model=List[schemas.OfertaResponse])
def read_ofertas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    ofertas = crud.listar_ofertas(db, skip=skip, limit=limit)
    return ofertas

@router.put("/{idOferta}", response_model=schemas.OfertaResponse)
def update_oferta(idOferta: int, oferta: schemas.OfertaUpdate, db: Session = Depends(database.get_db)):
    db_oferta = crud.atualizar_oferta(db, idOferta=idOferta, oferta=oferta)
    if db_oferta is None:
        raise HTTPException(status_code=404, detail="Oferta not found")
    return db_oferta

@router.delete("/{idOferta}", response_model=bool)
def delete_oferta(idOferta: int, db: Session = Depends(database.get_db)):
    deleted = crud.remover_oferta(db, idOferta=idOferta)
    if not deleted:
        raise HTTPException(status_code=404, detail="Oferta not found")
    return True