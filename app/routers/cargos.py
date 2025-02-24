from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, dependencies

router = APIRouter(
    prefix="/cargos", 
    tags=["Cargos"], 
    dependencies=[Depends(dependencies.get_current_active_user)],)

@router.post("/", response_model=schemas.CargoResponse)
def criar_cargo(cargo: schemas.CargoCreate, db: Session = Depends(database.get_db)):
    return crud.criar_cargo(db, cargo)

@router.put("/{idCargo}", response_model=schemas.CargoResponse)
def atualizar_cargo(idCargo: int, cargo_update: schemas.CargoUpdate, db: Session = Depends(database.get_db)):
    cargo = crud.atualizar_cargo(db, idCargo, cargo_update)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo não encontrado")
    return cargo

