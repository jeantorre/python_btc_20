from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, get_db
from backend.schema.schema_produtos import CriarProduto, AtualizarProduto, LerProduto
from typing import List
from backend.crud.crud_produtos import (
    criar_produto,
    ler_produtos,
    ler_produto,
    atualizar_produto,
    deletar_produto
)

"""
SEPARAR EM ROTAS TODAS AS FUNÇÕES DO CRUD
"""

rotas = APIRouter()

@rotas.get("/produtos/", resposta_modelo = List[LerProduto])
def ler_todos_produtos(db: Session = Depends(get_db)):
    produtos = ler_produtos(db)
    return produtos

@rotas.get("/produtos/{produto_id}", resposta_modelo = LerProduto)
def ler_um_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produtos = ler_produto(id_produto=produto_id, db=db)
    if db_produtos is None:
        raise HTTPException(status_code=404, detail = "Este produto não existe.")
    return db_produtos

@rotas.post("/produtos/", resposta_modelo = LerProduto)
def criar_produto(produto: CriarProduto, db: Session = Depends(get_db)):
    return criar_produto(produto=produto, db=db)


@rotas.put("/produtos/{produto_id}", resposta_modelo = LerProduto)
def atualizar_produto(produto_id: int, produto: AtualizarProduto, db: Session = Depends(get_db)):
    db_produto = atualizar_produto(produto_id=produto_id, db=db, produto=AtualizarProduto)
    if db_produto is None:
        raise HTTPException(status_code=404, detail = "Este produto não existe.")
    return db_produto


@rotas.delete("/produtos/{produto_id}", resposta_modelo = LerProduto)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto =  deletar_produto(produto_id=produto_id, db=db)
    if db_produto is None:
        raise HTTPException(status_code=404, detail = "Este produto não existe.")
    return db_produto
