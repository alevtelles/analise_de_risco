from pydantic import BaseModel
from typing import Literal, Optional

# Entrada recebida pelo frontend

class Solicitacao(BaseModel):
    descricao: str


# Saída da análise
class AnaliseRiscoEmprestimo(BaseModel):
    nome: str
    idade: int
    renda_mensal: float
    valor_emprestimo: float
    prazo_meses: int
    finalidade: str
    score_credito: Optional[int]
    risco_estimado: Literal["baixo", "médio", "alto"]

class AnaliseDB(AnaliseRiscoEmprestimo):
    id: int
    class Config:
        orm_mode = True