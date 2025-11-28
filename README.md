# Seeds - FastAPI Application

API REST desenvolvida com FastAPI, PostgreSQL e Docker para gerenciamento de produtos e vendas.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **PostgreSQL 16** - Banco de dados relacional
- **Docker & Docker Compose** - Containerização
- **Poetry** - Gerenciamento de dependências
- **SQLAlchemy** - ORM
- **Uvicorn** - Servidor ASGI

## 📦 Imagem Docker

A aplicação está disponível no Docker Hub:

```
victorsantos12/seeds-fastapi:latest
```

## 🏃 Como Executar

### Pré-requisitos

- Docker instalado
- Docker Compose instalado

### Opção 1: Usando Docker Compose (Recomendado)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seeds.git
cd seeds
```

2. Suba os containers:
```bash
docker compose up -d
```

3. Acesse a aplicação:
- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc

### Opção 2: Usando apenas a imagem do Docker Hub

```bash
# Baixar e executar a imagem
docker pull victorsantos12/seeds-fastapi:latest

# Executar com variáveis de ambiente
docker run -p 8000:8000 \
  -e DB_HOST=seu-postgres-host \
  -e DB_USER=postgres \
  -e DB_PASSWORD=sua-senha \
  -e DB_NAME=fastapi_seed \
  victorsantos12/seeds-fastapi:latest
```

## 📖 Documentação da API

Após subir a aplicação, acesse:

### Swagger UI
```
http://localhost:8000/docs
```

Interface interativa para testar todos os endpoints da API.

### ReDoc
```
http://localhost:8000/redoc
```

Documentação alternativa em formato de leitura.

### Endpoints Principais

#### Produtos
- `GET /api/v1/products` - Listar todos os produtos
- `POST /api/v1/products` - Criar novo produto
- `GET /api/v1/products/{id}` - Buscar produto por ID
- `PUT /api/v1/products/{id}` - Atualizar produto
- `DELETE /api/v1/products/{id}` - Deletar produto

#### Vendas
- `GET /api/v1/sales` - Listar todas as vendas
- `POST /api/v1/sales` - Criar nova venda
- `GET /api/v1/sales/{id}` - Buscar venda por ID
- `PUT /api/v1/sales/{id}` - Atualizar venda
- `DELETE /api/v1/sales/{id}` - Deletar venda

## ⚙️ Variáveis de Ambiente

Configure no arquivo `.env` ou no `docker-compose.yml`:

```env
APP_NAME=SeedsDocker
DEBUG=True
DB_HOST=db
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=fastapi_seed
```

## 🛠️ Desenvolvimento Local

### Instalação

1. Clone o repositório
2. Instale as dependências com Poetry:

```bash
poetry install
```

3. Ative o ambiente virtual:

```bash
poetry shell
```

4. Execute a aplicação:

```bash
uvicorn src.app.main:app --reload
```

### Estrutura do Projeto

```
seeds/
├── src/
│   └── app/
│       ├── api/         # Endpoints da API
│       ├── core/        # Configurações e logging
│       ├── db/          # Configuração do banco
│       ├── models/      # Modelos SQLAlchemy
│       ├── services/    # Lógica de negócio
│       └── main.py      # Arquivo principal
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## 🐳 Comandos Docker Úteis

```bash
# Subir containers em background
docker compose up -d

# Ver logs
docker compose logs -f

# Ver logs apenas do web
docker compose logs -f web

# Parar containers
docker compose down

# Parar e remover volumes
docker compose down -v

# Rebuild e subir
docker compose up --build

# Ver containers rodando
docker ps

# Entrar no container
docker exec -it seeds-web-1 bash
```

## 🗄️ Banco de Dados

O PostgreSQL está configurado para:
- **Host**: localhost (fora do Docker) ou `db` (dentro do Docker)
- **Porta**: 5432
- **Usuário**: postgres
- **Senha**: postgres
- **Database**: fastapi_seed

### Acessar o PostgreSQL

```bash
docker exec -it seeds-db-1 psql -U postgres -d fastapi_seed
```

## 🧪 Testes

```bash
# Executar testes
poetry run pytest

# Com cobertura
poetry run pytest --cov
```

## 📝 Notas

- Os dados do PostgreSQL são persistidos em um volume Docker (`postgres_data`)
- A aplicação cria as tabelas automaticamente no startup
- Para desenvolvimento, mantenha `DEBUG=True`
- Para produção, use `DEBUG=False` e senhas seguras

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

**Victor Santos**

- Docker Hub: [@victorsantos12](https://hub.docker.com/u/victorsantos12)
- GitHub: [@seu-usuario](https://github.com/seu-usuario)

## 🔗 Links Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Docker](https://docs.docker.com/)
- [Documentação PostgreSQL](https://www.postgresql.org/docs/)
- [Imagem no Docker Hub](https://hub.docker.com/r/victorsantos12/seeds-fastapi)