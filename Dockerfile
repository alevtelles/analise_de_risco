# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:3.13.0a5-slim

WORKDIR /app

COPY requirements.txt .

# Força pydantic-core a compilar nativamente
RUN pip install --upgrade pip \
    && pip install --no-binary :all: pydantic-core pydantic \
    && pip install -r requirements.txt

COPY . .

CMD ["bash", "-c", "\
    uvicorn app.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/app.py --server.port=8501 --server.address=0.0.0.0 \
    "]
