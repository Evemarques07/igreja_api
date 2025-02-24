from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, dependencies

router = APIRouter(
    prefix="/membros",
    tags=["Membros"],
    dependencies=[Depends(dependencies.get_current_active_user)],
)

# Criar membro
@router.post("/", response_model=schemas.MembroResponse)
def criar_membro(membro: schemas.MembroCreate, db: Session = Depends(database.get_db)):
    return crud.criar_membro(db, membro)

# Listar membros
@router.get("/", response_model=list[schemas.MembroResponse])
def listar_membros(db: Session = Depends(database.get_db)):
    return crud.listar_membros(db)

# Buscar membro por ID
@router.get("/{idMembro}", response_model=schemas.MembroResponse)
def buscar_membro(idMembro: int, db: Session = Depends(database.get_db)):
    membro = crud.buscar_membro(db, idMembro)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro

# Atualizar membro
@router.put("/{idMembro}", response_model=schemas.MembroResponse)
def atualizar_membro(idMembro: int, membro_update: schemas.MembroUpdate, db: Session = Depends(database.get_db)):
    membro = crud.atualizar_membro(db, idMembro, membro_update)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro

# Atualizar parcialmente membro (PATCH - atualiza apenas os campos fornecidos)
@router.patch("/{idMembro}", response_model=schemas.MembroResponse)
def atualizar_parcial_membro(idMembro: int, membro_update: schemas.MembroUpdate, db: Session = Depends(database.get_db)):
    membro = crud.atualizar_membro(db, idMembro, membro_update)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro

# Deletar membro
@router.delete("/{idMembro}", response_model=schemas.MembroResponse)
def deletar_membro(idMembro: int, db: Session = Depends(database.get_db)):
    membro = crud.deletar_membro(db, idMembro)
    if not membro:
        raise HTTPException(status_code=404, detail="Membro não encontrado")
    return membro
