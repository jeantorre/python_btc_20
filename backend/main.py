from fastapi import FastAPI

import backend.models.models_produtos
from backend.database import engine
from backend.routers import router_produto

backend.models.models_produtos.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_produto)
