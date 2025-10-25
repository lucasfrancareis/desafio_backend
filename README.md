## 🚀 Desafio Back-End - ASCII Empresa Júnior

API REST desenvolvida em **Python (FastAPI)** com **PostgreSQL**, 
**SQLAlchemy ORM**, **Alembic** e **Swagger**, como parte do processo seletivo
 da **ASCII Empresa Júnior (UFU)**.

---

## 📋 Objetivo
Fornecer uma API REST para gerenciar produtos, com os seguintes campos:

- Nome do produto  
- Preço  
- Categoria  

---

## 🧱 Tecnologias Utilizadas
- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic v2
- Pytest
- Docker + Docker Compose (opcional)

---

## 📂 Estrutura do Projeto

├── .gitignore
├── .env                       # variáveis de ambiente
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── versions/
│       └── <timestamp>_create_products_table.py
└── app/
    ├── __init__.py
    ├── main.py                # entrypoint (FastAPI app)
    ├── core/
    │   ├── __init__.py
    │   ├── config.py          # settings (pydantic-settings)
    │   └── logger.py
    ├── db/
    │   ├── __init__.py
    │   └── database.py        # engine, SessionLocal, Base, get_db()
    ├── models/
    │   ├── __init__.py
    │   └── product.py         # model SQLAlchemy (products)
    ├── schemas/
    │   ├── __init__.py
    │   └── product_schema.py  # DTOs Pydantic
    ├── repositories/
    │   ├── __init__.py
    │   └── product_repo.py    # consultas CRUD
    ├── services/
    │   ├── __init__.py
    │   └── product_service.py # regras de negócio
    ├── controllers/
    │   ├── __init__.py
    │   └── product_controller.py  # rotas /api/produtos
    └── tests/
        └── test_products.py   # testes pytest

---

## 🚀 Como Usar a API
- Existem duas formas de testar e usar esta API:

## 1. (Recomendada) Usando a Documentação Interativa (Swagger)
- Esta é a maneira mais fácil e visual de testar todos os endpoints.

> Com o servidor rodando (uvicorn app.main:app --reload), abra seu navegador.

> Acesse a "home page" que criei: http://127.0.0.1:8000/

> Clique no botão "Ir para /docs" ou acesse diretamente: http://127.0.0.1:8000/docs

> Você verá a interface do Swagger UI, onde pode expandir cada rota (POST, GET,
> PUT, DELETE), clicar em "Try it out" e testar a API em tempo real.

## 2. Usando um Cliente de API (Ex: cURL ou Postman)
- Você também pode interagir com a API diretamente através de qualquer cliente 
HTTP. Os exemplos abaixo usam cURL (que você pode rodar no seu terminal).

Endpoint Base: http://127.0.0.1:8000/api/produtos

# 1. Criar um novo produto (POST)

- Envia um JSON com os dados do produto para criar um novo registro.

curl -X POST "http://127.0.0.1:8000/api/produtos/" \
-H "Content-Type: application/json" \
-d '{
    "name": "Monitor Ultrawide",
    "price": 850.00,
    "category": "Periféricos"
}'

> Resposta Esperada (Code 200): O produto que acabou de ser criado, agora com um id.

# 2. Listar todos os produtos (GET)

- Retorna uma lista de todos os produtos cadastrados no banco de dados.

curl -X GET "http://127.0.0.1:8000/api/produtos/"

> Resposta Esperada (Code 200): Uma lista [ ... ] de objetos JSON, cada um 
> sendo um produto.

# 3. Buscar um produto por ID (GET /:id)

- Retorna os detalhes de um produto específico.

> Substitua '1' pelo ID do produto que você quer buscar

curl -X GET "http://127.0.0.1:8000/api/produtos/1"

>Resposta Esperada (Code 200): O objeto JSON do produto com id: 1.

- Se não encontrar (Code 404): {"detail":"Produto não encontrado"}

# 4. Atualizar um produto (PUT /:id)

- Atualiza os dados de um produto existente. Você só precisa enviar os campos
 que deseja alterar.

> Substitua '1' pelo ID do produto que você quer atualizar

curl -X PUT "http://127.0.0.1:8000/api/produtos/1" \
-H "Content-Type: application/json" \
-d '{
    "name": "Monitor Ultrawide (Novo Modelo)",
    "price": 900.00
}'

> Resposta Esperada (Code 200): O objeto JSON do produto com os dados atualizados.

# 5. Deletar um produto (DELETE /:id)

- Remove um produto do banco de dados pelo seu ID.

> Substitua '1' pelo ID do produto que você quer deletar

curl -X DELETE "http://127.0.0.1:8000/api/produtos/1"

>Resposta Esperada (Code 200): Uma mensagem de sucesso, como {"detail":
> "Produto removido com sucesso"}.

## 🏗️ Arquitetura e Estrutura do Projeto

- Para este desafio, eu escolhi seguir uma arquitetura em camadas (layered 
architecture). A ideia principal é separar as responsabilidades
do aplicativo em blocos lógicos, onde cada camada tem um trabalho específico. 
Isso torna o código mais limpo, mais fácil de manter e de testar.

> O fluxo de uma requisição segue: Controller → Service → Repository → Model 
> (Banco de Dados)

- Aqui está um detalhamento de cada pasta e arquivo principal do projeto:

# 📁 app/
É o coração do projeto. Todo o código-fonte da aplicação vive aqui.

> 📄 app/main.py
Este é o ponto de entrada da aplicação. Aqui eu faço três coisas principais:

Crio a instância principal do FastAPI: app = FastAPI().

Defino a rota raiz "/" (a "home page" que criamos) e o health check "/health".

Incluo o roteador do product_controller, dizendo que todos os endpoints de 
produto devem começar com o prefixo /api/produtos (como pedido no desafio).

Home Page Interativa (/): Em vez de deixar a rota raiz (/) mostrar um erro 404, 
eu decidi criar uma landing page customizada.

Eu usei o @app.get("/") e especifiquei response_class=HTMLResponse.
 O conteúdo é uma string Python que contém todo o HTML e CSS.

O visual que você vê é um "glassmorphism" (efeito de vidro). Eu consegui esse 
efeito no CSS combinando um background com rgba (para dar a transparência ao 
"card") com a propriedade backdrop-filter: blur(10px) (que borra o fundo 
gradiente do body atrás do card). Também adicionei uma animação fadeIn e um 
rodapé com minha assinatura.

# 📁 app/db/

Nesta pasta, eu centralizei toda a configuração de conexão com o banco de dados.

> 📄 database.py 

Arquivo crucial. Ele define o engine do SQLAlchemy (que sabe como se conectar ao
PostgreSQL usando a DATABASE_URL do .env). Ele também cria o SessionLocal (para
criar sessões de banco) e a famosa função get_db, que o FastAPI usa como uma 
dependência para injetar uma sessão de banco em cada rota que precisar dela.


# 📁 app/core/

Aqui ficam as configurações centrais da aplicação.

> 📄 config.py 

Eu uso a biblioteca pydantic-settings para carregar as variáveis de ambiente 
(como a DATABASE_URL) de forma segura a partir do arquivo .env.


# 📁 app/models/

Esta camada representa a estrutura dos meus dados no banco.

> 📄 product.py

Aqui eu defino o modelo Product, que herda do Base (definido no 
database.py). Esta classe mapeia o objeto Python Product para a tabela products 
no banco de dados, definindo as colunas (id, name, price, category).

# 📁 app/schemas/

Esta é a camada de validação de dados (DTOs - Data Transfer Objects). Eu uso 
Pydantic aqui, como pedido nos requisitos.

> 📄 product_schemas.py 

Aqui eu crio as "formas" dos dados que minha API aceita e retorna.

> ProductBase: Campos comuns que todo produto tem.

> ProductCreate: O que a API espera receber em um POST (herda de ProductBase).

> ProductUpdate: O que a API espera receber em um PUT (todos os campos são opcionais).

> ProductOut: O que a API retorna para o cliente (inclui o id).

# 📁 app/repositories/

Esta é a única camada que fala diretamente com o banco de dados. Ela separa a 
lógica de negócio da lógica de acesso aos dados.

> 📄 product_repo.py 
Eu criei uma classe ProductRepository que contém todos os 
métodos CRUD (Criar, Ler, Atualizar, Deletar). Por exemplo, save(product) 
executa db.add(product) e db.commit(). O Service chama esses métodos.

# 📁 app/services/

Esta é a camada da lógica de negócios (o "cérebro" da aplicação).

> 📄 product_service.py 

A classe ProductService coordena as ações. Por exemplo, a função create_product 
recebe o schema ProductCreate (do controller), transforma ele em um modelo 
Product (do SQLAlchemy) e chama o product_repo.save() para salvá-lo. Se eu 
precisasse de regras (ex: "não permitir preço negativo"), elas estariam aqui.

# 📁 app/controllers/
Esta é a camada de rotas da API (endpoints). Ela lida com as requisições HTTP e 
envia as respostas.

> 📄 product_controller.py 

Aqui eu uso o APIRouter do FastAPI para definir os endpoints (@router.post, 
@router.get, etc.). Cada rota apenas recebe a requisição, chama o ProductService
 correspondente para fazer o trabalho sujo, e retorna a resposta. Ela não sabe 
 como o produto é salvo, apenas que o serviço faz isso.

# 📁 alembic/ e 📄 alembic.ini

Aqui eu configurei o Alembic, que é a ferramenta profissional para gerenciar 
"migrations" de banco de dados (como o README.md original pedia). Em vez de 
criar as tabelas automaticamente com create_all, eu usei o Alembic para gerar um
arquivo de versão (alembic/versions/19d...create_products_table.py) que cria a 
tabela products de forma controlada. Esta é a prática recomendada em produção.

# Arquivos na Raiz

📄 .env: Arquivo local (ignorado pelo Git) onde eu armazeno dados importantes,
 como a DATABASE_URL.

📄 .gitignore: Arquivo de configuração que diz ao Git quais arquivos ignorar 
(como .env, __pycache__, etc.).

📄 requirements.txt: A lista de todas as dependências Python que o projeto 
precisa (FastAPI, Uvicorn, SQLAlchemy, Psycopg2).