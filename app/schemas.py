from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
import enum

# Enums para schemas
class TipoEntrada(str, enum.Enum):
    ofertas_missionarias = "Ofertas Missionárias"
    campanhas = "Campanhas e Propósitos Específicos"
    eventos = "Eventos e Conferências"
    venda_materiais = "Venda de Materiais"
    doacoes_empresas = "Doações de Empresas ou Parceiros"
    parcerias_ongs = "Parcerias com ONGs ou Projetos Sociais"
    apoio_outras_igrejas = "Apoio de Outras Igrejas ou Denominações"
    investimentos = "Investimentos"

class TipoSaida(str, enum.Enum):
    folha_pagamento = "Folha de Pagamento"
    encargos_sociais = "Encargos Sociais e Benefícios"
    aluguel_imovel = "Aluguel de Imóvel"
    manutencao_templo = "Manutenção do Templo"
    contas_mensais = "Água, Luz, Telefone e Internet"
    compra_materiais = "Compra de Materiais"
    ajuda_social = "Ajuda Social e Filantropia"
    eventos_congressos = "Eventos e Congressos"
    missoes_evangelismo = "Missões e Evangelismo"
    taxas_impostos = "Taxas e Impostos"
    marketing_divulgacao = "Marketing e Divulgação"
    instrumentos_musicais = "Instrumentos Musicais e Equipamentos de Som"
    despesas_viagens = "Despesas com Viagens"
    seguranca = "Segurança"
    ofertas_pastores = "Ofertas para Pastores Convidados"


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
    valor: float 
    observacao: Optional[str] = None

class DizimoCreate(DizimoBase):
    pass

class DizimoUpdate(BaseModel):
    idMembro: Optional[int] = None
    referencia: Optional[str] = None
    dataRegistro: Optional[date] = None
    valor: Optional[float] = None 
    observacao: Optional[str] = None

class DizimoResponse(DizimoBase):
    idDizimo: int

    class Config:
        orm_mode = True

class OfertaBase(BaseModel):
    descricao: Optional[str] = None
    dataRegistro: date
    valor: float 
    observacao: Optional[str] = None

class OfertaCreate(OfertaBase):
    pass

class OfertaUpdate(BaseModel):
    descricao: Optional[str] = None
    dataRegistro: Optional[date] = None
    valor: Optional[float] = None 
    observacao: Optional[str] = None

class OfertaResponse(OfertaBase):
    idOferta: int

    class Config:
        orm_mode = True

# Entrada schemas
class EntradaBase(BaseModel):
    tipo: TipoEntrada
    dataRegistro: date
    valor: float
    observacao: Optional[str] = None

class EntradaCreate(EntradaBase):
    pass

class EntradaUpdate(BaseModel):
    tipo: Optional[TipoEntrada] = None
    dataRegistro: Optional[date] = None
    valor: Optional[float] = None
    observacao: Optional[str] = None

class EntradaResponse(EntradaBase):
    idEntrada: int

    class Config:
        orm_mode = True

# Saida schemas
class SaidaBase(BaseModel):
    tipo: TipoSaida
    dataRegistro: date
    valor: float
    observacao: Optional[str] = None

class SaidaCreate(SaidaBase):
    pass

class SaidaUpdate(BaseModel):
    tipo: Optional[TipoSaida] = None
    dataRegistro: Optional[date] = None
    valor: Optional[float] = None
    observacao: Optional[str] = None

class SaidaResponse(SaidaBase):
    idSaida: int

    class Config:
        orm_mode = True