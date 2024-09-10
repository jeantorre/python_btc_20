from models.models_produtos import ModeloProdutos
from schema.schema_produtos import AtualizarProduto, CriarProduto
from sqlalchemy.orm import Session

"""
RESPONSÁVEL POR CRIAR AS 5 FUNÇÕES DO SQLALCHEMY
- get all (SELECT * FROM)
- get where id = 1
- insert into (CREATE)
- update where id = 1
- delete where id = 1
"""


def ler_produtos(db: Session):
    """
    Função responsável por retornar todos os  produtos
    """
    return db.query(ModeloProdutos).all()


def ler_produto(db: Session, id_produto: int):
    """
    Função responsável por retornar a pesquisa
    de um id de um produto específico
    """
    return db.query(ModeloProdutos).filter(ModeloProdutos.id == id_produto).first()


def criar_produto(db: Session, produto: CriarProduto):
    """
    Função responsável por criar novos produtos
    """
    db_produto = ModeloProdutos(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


def atualizar_produto(db: Session, id_produto: int, produto=AtualizarProduto):
    """
    Função responsável por atualizar as informações de um produto
    """
    db_produto = (
        db.query(ModeloProdutos).filter(ModeloProdutos.id == id_produto).first()
    )

    if db_produto is None:
        return None

    if produto.nome is not None:
        db_produto.nome = produto.nome

    if produto.descricao is not None:
        db_produto.descricao = produto.descricao

    if produto.preco is not None:
        db_produto.preco = produto.preco

    if produto.categoria is not None:
        db_produto.categoria = produto.categoria

    if produto.email_fornecedor is not None:
        db_produto.email_fornecedor = produto.email_fornecedor

    db.commit()
    db.refresh(db_produto)
    return db_produto


def deletar_produto(db: Session, id_produto: int):
    """
    Função responsável por deletar um produto já adicionado
    no banco de dados
    """
    db_produto = (
        db.query(ModeloProdutos).filter(ModeloProdutos.id == id_produto).first()
    )
    db.delete(db_produto)
    db.commit()
    return db_produto
