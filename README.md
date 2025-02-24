# API Igreja

API RESTful construída com FastAPI para gerenciamento de dados da igreja, como membros, cargos e atividades.

## Visão Geral

Esta API fornece endpoints para:

- Gerenciar membros (CRUD completo)
- Gerenciar cargos (CRUD básico)
- Gerenciar membros em atividades eclesiásticas relevantes (CRUD completo)
- Autenticação e autorização com tokens JWT

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework web Python moderno e de alto desempenho para construir APIs.
- [Uvicorn](https://www.uvicorn.org/): Servidor ASGI para executar a API.
- [SQLAlchemy](https://www.sqlalchemy.org/): Toolkit SQL e ORM para interagir com o banco de dados.
- [PostgreSQL](https://www.postgresql.org/): Banco de dados relacional utilizado para armazenar os dados.
- [Pydantic](https://pydantic-docs.samuelcolvin.io/): Biblioteca para validação de dados.
- [Passlib](https://passlib.readthedocs.io/): Biblioteca para hashing de senhas.
- [python-jose](https://python-jose.readthedocs.io/): Biblioteca para trabalhar com JSON Web Tokens (JWT).
- [python-dotenv](https://github.com/theskumar/python-dotenv): Biblioteca para carregar variáveis de ambiente do arquivo `.env`.

## Pré-requisitos

- Python 3.7+
- PostgreSQL instalado e configurado

## Instalação

1.  Clone o repositório:

    ```bash
    git clone https://github.com/Evemarques07/igreja_api.git
    cd <nome_do_projeto>
    ```

2.  Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    venv\Scripts\activate
    source venv/bin/activate
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4.  Configure as variáveis de ambiente:

    - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

      ```
      DATABASE_URL=postgresql://seu_usuario:sua_senha@localhost/seu_banco
      SECRET_KEY="SUA_CHAVE_SECRETA_FORTE"
      ALGORITHM="HS256"
      ACCESS_TOKEN_EXPIRE_MINUTES=30
      ```

      Substitua `seu_usuario`, `sua_senha`, `seu_banco` e `"SUA_CHAVE_SECRETA_FORTE"` com os valores corretos.

# Configuração do Alembic

## O projeto utiliza o Alembic para gerenciar as migrações do banco de dados. Para configurar o Alembic corretamente, crie o arquivo alembic.ini na raiz do projeto com o seguinte conteúdo:

# A generic, single database configuration.

[alembic]
script_location = alembic
prepend_sys_path = .
version_path_separator = os

sqlalchemy.url = postgresql://usuario:seu_usuario:sua_senha@localhost/seu_banco

[post_write_hooks]

# Logging configuration

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
Explicação dos campos:
script_location: Define o diretório onde as migrações do Alembic serão armazenadas. Neste caso, estamos configurando para que as migrações fiquem na pasta alembic/.
sqlalchemy.url: Configuração da URL de conexão com o banco de dados PostgreSQL. Substitua `seu_usuario`, `sua_senha`, `seu_banco` pelos dados corretos do seu banco de dados.
[loggers], [handlers], [formatters]: Configurações de logging para monitorar as atividades do Alembic e SQLAlchemy.

# Explicação dos campos:

script_location: Define o diretório onde as migrações do Alembic serão armazenadas. Neste caso, estamos configurando para que as migrações fiquem na pasta alembic/.
sqlalchemy.url: Configuração da URL de conexão com o banco de dados PostgreSQL. Substitua everton, 123456, e igreja pelos dados corretos do seu banco de dados.
[loggers], [handlers], [formatters]: Configurações de logging para monitorar as atividades do Alembic e SQLAlchemy.

## Estrutura do Projeto

├───app
│ │ config.py
│ │ crud.py
│ │ database.py
│ │ dependencies.py
│ │ models.py
│ │ schemas.py
│ │ **init**.py
│ │  
│ ├───core
│ │ │ security.py
│ │ │ settings.py
│ │ │  
│ │ └───**pycache**
│ │ security.cpython-312.pyc
│ │  
│ ├───routers
│ │ │ auth.py
│ │ │ cargos.py
│ │ │ meal.py
│ │ │ membros.py
│ │ │ **init**.py
│ │ │  
│ │ └───**pycache**
│ │ auth.cpython-312.pyc
│ │ cargos.cpython-312.pyc
│ │ meal.cpython-312.pyc
│ │ membros.cpython-312.pyc
│ │ **init**.cpython-312.pyc
│ │  
│ └───**pycache**
│ crud.cpython-312.pyc
│ database.cpython-312.pyc
│ dependencies.cpython-312.pyc
│ models.cpython-312.pyc
│ schemas.cpython-312.pyc
│ **init**.cpython-312.pyc
│  
└───**pycache**
main.cpython-312.pyc

## Como Executar a API

1.  Execute o servidor Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2.  Acesse a documentação interativa da API em:

    ```
    http://127.0.0.1:8000/docs
    ```

## Autenticação

A API utiliza autenticação por token JWT. Para obter um token de acesso, faça uma requisição POST para `/auth/token` com as credenciais (idMembro e senha) de um usuário registrado.

Em seguida, adicione o token no cabeçalho `Authorization` das requisições para as rotas protegidas, no formato `Bearer <token>`.

## Endpoints da API

- `/membros`: Gerenciamento de membros (requer autenticação)
- `/cargos`: Gerenciamento de cargos (requer autenticação)
- `/meal`: Gerenciamento de membros em atividades (requer autenticação)
- `/auth/token`: Obter token de acesso
- `/auth/register`: Registrar um novo usuário

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

[MIT](LICENSE)

# igreja_api
