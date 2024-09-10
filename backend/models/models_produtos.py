from datetime import datetime

from database import Base
from pytz import timezone
from sqlalchemy import Column, DateTime, Float, Integer, String

"""
CRIAR MODELOS DO BANCO DE DADOS (REGRA DE NEGÓCIOS)
"""


class ModeloProdutos(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    ultima_alteracao = Column(
        DateTime, default=lambda: datetime.now(timezone("America/Sao_Paulo"))
    )
