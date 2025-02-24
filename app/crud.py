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
    return db.query(models.Meal).filter(models.Meal.idMembro == idMembro).all()

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

# Dizimo CRUD functions
def criar_dizimo(db: Session, dizimo: schemas.DizimoCreate):
    db_dizimo = models.Dizimo(**dizimo.dict())
    db.add(db_dizimo)
    db.commit()
    db.refresh(db_dizimo)
    return db_dizimo

def get_dizimo(db: Session, idDizimo: int):
    return db.query(models.Dizimo).filter(models.Dizimo.idDizimo == idDizimo).first()

def listar_dizimos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dizimo).offset(skip).limit(limit).all()

def atualizar_dizimo(db: Session, idDizimo: int, dizimo: schemas.DizimoUpdate):
    db_dizimo = db.query(models.Dizimo).filter(models.Dizimo.idDizimo == idDizimo).first()
    if db_dizimo:
        for key, value in dizimo.dict(exclude_unset=True).items():
            setattr(db_dizimo, key, value)
        db.commit()
        db.refresh(db_dizimo)
        return db_dizimo
    return None

def remover_dizimo(db: Session, idDizimo: int):
    db_dizimo = db.query(models.Dizimo).filter(models.Dizimo.idDizimo == idDizimo).first()
    if db_dizimo:
        db.delete(db_dizimo)
        db.commit()
        return True
    return False

# Oferta CRUD functions
def criar_oferta(db: Session, oferta: schemas.OfertaCreate):
    db_oferta = models.Oferta(**oferta.dict())
    db.add(db_oferta)
    db.commit()
    db.refresh(db_oferta)
    return db_oferta

def get_oferta(db: Session, idOferta: int):
    return db.query(models.Oferta).filter(models.Oferta.idOferta == idOferta).first()

def listar_ofertas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Oferta).offset(skip).limit(limit).all()

def atualizar_oferta(db: Session, idOferta: int, oferta: schemas.OfertaUpdate):
    db_oferta = db.query(models.Oferta).filter(models.Oferta.idOferta == idOferta).first()
    if db_oferta:
        for key, value in oferta.dict(exclude_unset=True).items():
            setattr(db_oferta, key, value)
        db.commit()
        db.refresh(db_oferta)
        return db_oferta
    return None

def remover_oferta(db: Session, idOferta: int):
    db_oferta = db.query(models.Oferta).filter(models.Oferta.idOferta == idOferta).first()
    if db_oferta:
        db.delete(db_oferta)
        db.commit()
        return True
    return False