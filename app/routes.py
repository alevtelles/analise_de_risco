from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from . import database, models, schemas

from pydantic_ai import OpenAIExtractor 
import os

router = APIRouter()
extractor = OpenAIExtractor(api_key=os.getenv("OPENAI_API_KEY"))

def get_db():
    db = database.SessionLocal()
    try: 
        yield db
    finally:
        db.close()
    
@router.post("/analise", response_model=schemas.AnaliseDB)
def analisar_emprestimo(solicitacao: schemas.Solicitacao, db: Session = Depends(get_db)):
    try: 
        resultado = extractor.extract(
            prompt=solicitacao.descricao,
            schema=schemas.AnaliseRiscoEmprestimo,
            instructions="""Analise a solicitação do empréstimo e retorne os campos preenchidos com base no texto. Classifique o risco como 'baixo', 'médio' ou 'alto' com base na renda, score e valor solicitado."""
        )
        obj = models.AnaliseEmprestimo(**resultado.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/analises", response_model=List[schemas.AnaliseDB])
def listar_analises(
    risco: Optional[str] = Query(None),
    score_min: Optional[int] = Query(None),
    prazo_max: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    query =db.query(models.AnaliseEmprestimo)

    if risco:
        query = query.filter(models.AnaliseEmprestimo.risco_estimado == risco)
    if score_min:
        query = query.filter(models.AnaliseEmprestimo.score_credito >= score_min)
    if prazo_max:
        query = query.filter(models.AnaliseEmprestimo.prazo_meses <= prazo_max)
    
    return query.all()
