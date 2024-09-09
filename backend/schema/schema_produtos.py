from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

"""
VALIDAÇÃO DE COMO OS DADOS VÃO TRAFEGAR
"""


class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr


class LerProduto(ProdutoBase):
    id: PositiveInt
    ultima_alteracao: datetime

    class Config:
        from_atributes = True


class CriarProduto(ProdutoBase):
    pass


class AtualizarProduto(ProdutoBase):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None
