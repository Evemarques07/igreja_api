from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas, database, dependencies

router = APIRouter(
    prefix="/meal",
    tags=["Meal"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

@router.post("/", response_model=schemas.MealResponse)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(database.get_db)):
    return crud.criar_meal(db, meal)

@router.get("/{idAdm}", response_model=schemas.MealResponse)
def read_meal(idAdm: int, db: Session = Depends(database.get_db)):
    db_meal = crud.get_meal(db, idAdm=idAdm)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal

@router.get("/membro/{idMembro}", response_model=List[schemas.MealResponse])
def read_meal_by_membro(idMembro: int, db: Session = Depends(database.get_db)):
    db_meals = crud.get_meal_by_membro(db, idMembro=idMembro)
    return db_meals

@router.get("/", response_model=List[schemas.MealResponse])
def read_meals(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    meals = crud.listar_meals(db, skip=skip, limit=limit)
    return meals

@router.put("/{idAdm}", response_model=schemas.MealResponse)
def update_meal(idAdm: int, meal: schemas.MealUpdate, db: Session = Depends(database.get_db)):
    db_meal = crud.atualizar_meal(db, idAdm=idAdm, meal=meal)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal

@router.delete("/{idAdm}", response_model=bool)
def delete_meal(idAdm: int, db: Session = Depends(database.get_db)):
    deleted = crud.remover_meal(db, idAdm=idAdm)
    if not deleted:
        raise HTTPException(status_code=404, detail="Meal not found")
    return True