from fastapi import FastAPI
from . import database, models
from .routes import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API de Risco de Empréstimo com IA")
app.include_router(router)