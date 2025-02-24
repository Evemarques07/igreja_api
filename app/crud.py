from sqlalchemy.orm import Session
from . import models, schemas
from .core.security import get_password_hash

# Criar membro
def criar_membro(db: Session, membro: schemas.MembroCreate):
    db_membro = models.Membro(**membro.dict())
    db.add(db_membro)
    db.commit()
    db.refresh(db_membro)
    return db_membro

# Listar todos os membros
def listar_membros(db: Session):
    return db.query(models.Membro).all()

# Buscar membro por ID
def buscar_membro(db: Session, idMembro: int):
    return db.query(models.Membro).filter(models.Membro.idMembro == idMembro).first()

# Atualizar membro
def atualizar_membro(db: Session, idMembro: int, membro_update: schemas.MembroUpdate):
    db_membro = buscar_membro(db, idMembro)
    if db_membro:
        for key, value in membro_update.dict(exclude_unset=True).items():
            setattr(db_membro, key, value)
        db.commit()
        db.refresh(db_membro)
    return db_membro

# Deletar membro
def deletar_membro(db: Session, idMembro: int):
    db_membro = buscar_membro(db, idMembro)
    if db_membro:
        db.delete(db_membro)
        db.commit()
    return db_membro

# Criar cargo
def criar_cargo(db: Session, cargo: schemas.CargoCreate):
    db_cargo = models.Cargo(**cargo.dict())
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo

# Listar todos os cargos
def get_cargo(db: Session, idCargo: int):
    return db.query(models.Cargo).filter(models.Cargo.idCargo == idCargo).first()

# Atualizar cargo
def atualizar_cargo(db: Session, idCargo: int, cargo_update: schemas.CargoUpdate):
    db_cargo = db.query(models.Cargo).filter(models.Cargo.idCargo == idCargo).first()
    if db_cargo:
        for key, value in cargo_update.dict(exclude_unset=True).items():
            setattr(db_cargo, key, value)
        db.commit()
        db.refresh(db_cargo)
    return db_cargo

# Criar usuario
def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(idMembro=usuario.idMembro, password=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Get usuario by id
def get_usuario_by_id(db: Session, idUser: int):
    return db.query(models.Usuario).filter(models.Usuario.idUser == idUser).first()

# Get usuario by idMembro
def get_usuario_by_idMembro(db: Session, idMembro: int):
    return db.query(models.Usuario).filter(models.Usuario.idMembro == idMembro).first()

# Meal CRUD functions
def criar_meal(db: Session, meal: schemas.MealCreate):
    db_meal = models.Meal(**meal.dict())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

# Get meal by idAdm
def get_meal(db: Session, idAdm: int):
    return db.query(models.Meal).filter(models.Meal.idAdm == idAdm).first()

# Get meal by idMembro
def get_meal_by_membro(db: Session, idMembro: int):
    return db.query(models.Meal).filter(models.Meal.idMembro == idMembro).first()

# Listar todas as meals
def listar_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()

# Atualizar meal
def atualizar_meal(db: Session, idAdm: int, meal: schemas.MealUpdate):
    db_meal = db.query(models.Meal).filter(models.Meal.idAdm == idAdm).first()
    if db_meal:
        for key, value in meal.dict(exclude_unset=True).items():
            setattr(db_meal, key, value)
        db.commit()
        db.refresh(db_meal)
        return db_meal
    return None

# Remover meal
def remover_meal(db: Session, idAdm: int):
    db_meal = db.query(models.Meal).filter(models.Meal.idAdm == idAdm).first()
    if db_meal:
        db.delete(db_meal)
        db.commit()
        return True
    return False