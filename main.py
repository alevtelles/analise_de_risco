from fastapi import FastAPI, HTTPException
from schemas import Solicitacao, AnaliseRiscoEmprestimo
from pydantic_ai import OpenAIExtractor
import os

app = FastAPI(title="API de Análise de Risco de Empréstimos")

# Configure a chave da OpenAI com variável de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Defina a variável de ambiente OPENAI_API_KEY")

extractor = OpenAIExtractor(api_key=OPENAI_API_KEY)

@app.post("/analise", response_model=AnaliseRiscoEmprestimo)
async def analisar_emprestimo(solicitacao: Solicitacao):
    try:
        resultado = extractor.extract(
            prompt=solicitacao.descricao,
            schema=AnaliseRiscoEmprestimo,
            instructions="""Analise o texto da solicitação de emprestimo e extraia os dados estruturados. Com base na renda mensal, valor do emprestimo, prazo e score de crédito (se informado), estime o risco do empréstimo como 'baixo', 'médio' ou 'alto'. """
        )
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))