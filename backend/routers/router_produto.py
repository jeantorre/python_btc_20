from typing import List

from crud.crud_produtos import (
    atualizar_produto,
    criar_produto,
    deletar_produto,
    ler_produto,
    ler_produtos,
)
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schema.schema_produtos import AtualizarProduto, CriarProduto, LerProduto
from sqlalchemy.orm import Session

"""
SEPARAR EM ROTAS TODAS AS FUNÇÕES DO CRUD
"""

rotas = APIRouter()


@rotas.get("/produtos/", response_model=List[LerProduto])
def ler_todos_produtos(db: Session = Depends(get_db)):
    produtos = ler_produtos(db)
    return produtos


@rotas.get("/produtos/{produto_id}", response_model=LerProduto)
def ler_um_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produtos = ler_produto(id_produto=produto_id, db=db)
    if db_produtos is None:
        raise HTTPException(status_code=404, detail="Este produto não existe.")
    return db_produtos


@rotas.post("/produtos/", response_model=LerProduto)
def criar_um_produto(produto: CriarProduto, db: Session = Depends(get_db)):
    return criar_produto(produto=produto, db=db)


@rotas.put("/produtos/{produto_id}", response_model=LerProduto)
def atualizar_um_produto(
    produto_id: int, produto: AtualizarProduto, db: Session = Depends(get_db)
):
    db_produto = atualizar_produto(
        produto_id=produto_id, db=db, produto=AtualizarProduto
    )
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Este produto não existe.")
    return db_produto


@rotas.delete("/produtos/{produto_id}", response_model=LerProduto)
def deletar_um_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = deletar_produto(produto_id=produto_id, db=db)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Este produto não existe.")
    return db_produto
