import models.models_produtos
from database import engine
from fastapi import FastAPI
from routers.router_produto import rotas

models.models_produtos.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(rotas)
