from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

# Membros schemas
class MembroBase(BaseModel):
    nomeCompleto: str
    cpf: str
    dataBatismo: Optional[date] = None
    dataInclusao: date
    dataExclusao: Optional[date] = None

class MembroCreate(MembroBase):
    pass

class MembroUpdate(BaseModel):
    nomeCompleto: Optional[str] = None
    cpf: Optional[str] = None
    dataBatismo: Optional[date] = None
    dataInclusao: Optional[date] = None
    dataExclusao: Optional[date] = None

class MembroResponse(MembroBase):
    idMembro: int

    class Config:
        orm_mode = True

# Cargos schemas 
class CargoBase(BaseModel):
    nomeCargo: str
    descricao: Optional[str] = None

class CargoCreate(CargoBase):
    pass

class CargoResponse(CargoBase):
    idCargo: int

    class Config:
        orm_mode = True

class CargoUpdate(BaseModel):
    nomeCargo: Optional[str] = None
    descricao: Optional[str] = None

class UsuarioBase(BaseModel):
    idMembro: int
    password: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    idUser: int

    class Config:
        orm_mode = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    idUser: Optional[int] = None

# Meal schemas
class MealBase(BaseModel):
    idMembro: int
    idCargo: int
    dataPosse: date
    dataLimitePosse: Optional[date] = None

class MealCreate(MealBase):
    pass

class MealUpdate(BaseModel):
    idMembro: Optional[int] = None
    idCargo: Optional[int] = None
    dataPosse: Optional[date] = None
    dataLimitePosse: Optional[date] = None

class MealResponse(MealBase):
    idAdm: int

    class Config:
        orm_mode = True

# Dizimo schemas
class DizimoBase(BaseModel):
    idMembro: Optional[int] = None
    referencia: Optional[str] = None
    dataRegistro: date
    observacao: Optional[str] = None

class DizimoCreate(DizimoBase):
    pass

class DizimoUpdate(BaseModel):
    idMembro: Optional[int] = None
    referencia: Optional[str] = None
    dataRegistro: Optional[date] = None
    observacao: Optional[str] = None

class DizimoResponse(DizimoBase):
    idDizimo: int

    class Config:
        orm_mode = True

# Oferta schemas
class OfertaBase(BaseModel):
    descricao: Optional[str] = None
    dataRegistro: date
    observacao: Optional[str] = None

class OfertaCreate(OfertaBase):
    pass

class OfertaUpdate(BaseModel):
    descricao: Optional[str] = None
    dataRegistro: Optional[date] = None
    observacao: Optional[str] = None

class OfertaResponse(OfertaBase):
    idOferta: int

    class Config:
        orm_mode = True

