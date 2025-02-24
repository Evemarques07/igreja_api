from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Membro(Base):
    __tablename__ = "membros"

    idMembro = Column(Integer, primary_key=True, index=True)
    nomeCompleto = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    dataBatismo = Column(Date, nullable=True)
    dataInclusao = Column(Date, nullable=False)
    dataExclusao = Column(Date, nullable=True)

class Cargo(Base):
    __tablename__ = "cargos"

    idCargo = Column(Integer, primary_key=True, index=True)
    nomeCargo = Column(String, unique=True, nullable=False)
    descricao = Column(String, nullable=True)

class Usuario(Base):
    __tablename__ = "usuarios"

    idUser = Column(Integer, primary_key=True, index=True)
    idMembro = Column(Integer, ForeignKey("membros.idMembro"))
    password = Column(String)

    membro = relationship("Membro")

class Meal(Base):
    __tablename__ = "meal"

    idAdm = Column(Integer, primary_key=True, index=True)
    idMembro = Column(Integer, ForeignKey("membros.idMembro"))
    idCargo = Column(Integer, ForeignKey("cargos.idCargo"))
    dataPosse = Column(Date, nullable=False)
    dataLimitePosse = Column(Date, nullable=True)

    membro = relationship("Membro")
    cargo = relationship("Cargo")

class Dizimo(Base):
    __tablename__ = "dizimos"

    idDizimo = Column(Integer, primary_key=True, index=True)
    idMembro = Column(Integer, ForeignKey("membros.idMembro"), nullable=True)
    referencia = Column(String, nullable=True)
    dataRegistro = Column(Date, nullable=False)
    observacao = Column(Text, nullable=True)

    membro = relationship("Membro")

class Oferta(Base):
    __tablename__ = "ofertas"

    idOferta = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=True)
    dataRegistro = Column(Date, nullable=False)
    observacao = Column(Text, nullable=True)