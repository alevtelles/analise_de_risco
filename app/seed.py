from faker import Faker
from sqlalchemy.orm import Session
from app.models import AnaliseEmprestimo
from app.database import SessionLocal
import random

fake = Faker("pt_BR")

def gerar_risco(renda, parcela, score):
    if renda >= 3 * parcela and score >= 700:
        return "baixo"
    
    elif renda >=2 * parcela and score >= 600:
        return "médio"
    
    else: 
        return "alto"

def criar_seeds(db: Session, quantidade: int = 100):
    for _ in range(quantidade):
        idade = random.randint(20, 70)
        renda = random.uniform(2000, 15000)
        valor = random.uniform(5000, 60000)
        prazo = random.choice([12, 24, 36, 48])
        parcela = valor / prazo
        score = random.randint(300, 900)
        risco = gerar_risco(renda, parcela, score)

        emprestimo = AnaliseEmprestimo(
            nome=fake.name(),
            idade=idade,
            renda_mensal=round(renda, 2),
            valor_emprestimo=round(valor, 2),
            prazo_meses=prazo,
            finalidade=fake.sentence(nb_words=6),
            score_credito=score,
            risco_estimado=risco
        )

        db.add(emprestimo)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    criar_seeds(db)
    print("✅ Banco de dados populado com dados fake.")
    