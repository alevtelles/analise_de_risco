## 📊 Análise de Risco Financeiro com PydanticAI

### Sistema de avaliação de risco de crédito com validação inteligente de dados e deploy via Docker.

---

### ⚙️ Visão Geral

Este projeto é um protótipo funcional de um sistema de **análise de risco financeiro**, com foco na avaliação de **concessão de crédito** e prevenção à **inadimplência**. Ele demonstra como a biblioteca [PydanticAI](https://github.com/alevtelles/pydantic_ai) pode ser utilizada para **validação estruturada de dados e modelagem inteligente** com suporte a IA.

---

### 🧰 Tecnologias Principais

| Tecnologia         | Descrição                                               |
| ------------------ | ------------------------------------------------------- |
| **Python**         | Linguagem principal do backend                          |
| **PydanticAI**     | Validação inteligente de dados com suporte a IA         |
| **Docker**         | Containerização e deploy consistente do sistema         |
| **Docker Compose** | Orquestração de serviços do backend e frontend          |
| **Streamlit**      | Interface visual para interação com o modelo (frontend) |

---

### 🗂 Estrutura do Projeto

```
analise_de_risco/
├── app/                    # Backend com lógica de negócio e API
│   ├── main.py             # Ponto de entrada da aplicação
│   └── ...
├── frontend/               # Interface Streamlit
│   └── ...
├── .env                    # Configurações sensíveis (não versionado)
├── .env.example            # Template do .env
├── Dockerfile              # Dockerfile do backend
├── docker-compose.yml      # Orquestração do backend/frontend
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

---

### 🚀 Como Executar

#### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- (Opcional) [Python 3.10+](https://www.python.org/), caso queira rodar sem containers

#### Passo a passo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/alevtelles/analise_de_risco.git
   cd analise_de_risco
   ```

2. Crie seu arquivo `.env`:

   ```bash
   cp .env.example .env
   ```

3. Suba os containers:

   ```bash
   docker-compose up --build
   ```

4. Acesse:

   - **API Backend**: `http://localhost:8000`
   - **Frontend Streamlit**: `http://localhost:8501`

---

### 🧪 Testes

> ⚠️ Testes automatizados ainda não foram implementados.

Sugestão: utilizar `pytest` e `httpx` para testes de integração via FastAPI.

---

### ✅ Funcionalidades Atuais

- Validação de dados de entrada com PydanticAI
- Classificação de risco de crédito com base em atributos pessoais e financeiros
- Interface interativa com Streamlit
- Deploy completo com Docker

---

### 📌 Melhorias Futuras

- [ ] Implementação de testes automatizados
- [ ] Persistência com banco de dados relacional
- [ ] Treinamento de modelos próprios para classificação
- [ ] Autenticação de usuários
- [ ] Documentação automática da API (FastAPI Swagger)

---

### 🔒 Segurança

- Certifique-se de **não subir o arquivo `.env`** para repositórios públicos.
- Avalie variáveis sensíveis como tokens, senhas ou chaves de API com cuidado.

---

### 📄 Licença

Distribuído sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

### 👨‍💻 Autor

**Alev Telles**
[GitHub](https://github.com/alevtelles)

---

Se quiser, posso adicionar badges, GIF de demonstração, ou gerar a documentação automática da API para incluir neste README.

Deseja isso?
