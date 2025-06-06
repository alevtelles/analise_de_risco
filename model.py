from sqlalchemy import Column, Integer, String, Float
from .database import Base

class AnaliseEmprestimo(Base):
    __tablename__ = "analise"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)
    renda_mensal = Column(Float)
    valor_emprestimo = Column(Float)
    prazos_meses = Column(Integer)
    finalidade = Column(String)
    score_cretido = Column(Integer, nullable=True)
    risco_estimado = Column(String)

    