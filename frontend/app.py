import streamlit as st
import requests
import pandas as pd

API_URL = "http://api:8000"

st.set_page_config(page_title="Análise de Empréstimos", layout="wide")
st.title("📊 Análise de Risco de Empréstimos")

with st.sidebar:
    st.subheader("🔎 Filtros")
    risco = st.selectbox("Risco", ["", "baixo", "médio", "alto"])
    score_min = st.slider("Score mínimo", 300, 600, 900)
    prazo_max = st.slider("Prazo máximo (meses)", 12, 24, 36, 48)

params = {"score_min": score_min, "prazo_max": prazo_max}
if risco:
    params["risco"] = risco

res = requests.get(f"{API_URL}/analises", params=params)
if res.status_code == 200:
    df = pd.DataFrame(res.json())
    st.dataframe(df, use_container_width=True)
else:
    st.error("Error ao carregar dados da API")

st.subheader("📩 Nova Solicitação de Empréstimo")
texto = st.text_area("Descreva a solicitação")
if st.button("Enviar para análise"):
    r = requests.post(f"{API_URL}/analise", json={"descricao": texto})
    if r.status_code == 200:
        st.success("Análise realizada com sucesso!")
        st.json(r.json())

    else:
        st.error(f"Erro: {r.status_code} - {r.text}")