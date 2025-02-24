from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Float, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

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
    valor = Column(Float, nullable=False)
    dataRegistro = Column(Date, nullable=False)
    observacao = Column(Text, nullable=True)

    membro = relationship("Membro")

class Oferta(Base):
    __tablename__ = "ofertas"

    idOferta = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=True)
    dataRegistro = Column(Date, nullable=False)
    valor = Column(Float, nullable=False)
    observacao = Column(Text, nullable=True)

# Enum para tipos de entradas
class TipoEntrada(enum.Enum):
    ofertas_missionarias = "Ofertas Missionárias"
    campanhas = "Campanhas e Propósitos Específicos"
    eventos = "Eventos e Conferências"
    venda_materiais = "Venda de Materiais"
    doacoes_empresas = "Doações de Empresas ou Parceiros"
    parcerias_ongs = "Parcerias com ONGs ou Projetos Sociais"
    apoio_outras_igrejas = "Apoio de Outras Igrejas ou Denominações"
    investimentos = "Investimentos"

# Enum para tipos de saídas
class TipoSaida(enum.Enum):
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

class Entrada(Base):
    __tablename__ = "entradas"

    idEntrada = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoEntrada), nullable=False)
    dataRegistro = Column(Date, nullable=False)
    valor = Column(Float, nullable=False)
    observacao = Column(Text, nullable=True)

class Saida(Base):
    __tablename__ = "saidas"

    idSaida = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoSaida), nullable=False)
    dataRegistro = Column(Date, nullable=False)
    valor = Column(Float, nullable=False)
    observacao = Column(Text, nullable=True)