# API REST Framework

# Especificações e Requisitos do Projeto
Desenvolvimento de um projeto Django e DRF, relacionamento one-to-many e autenticação para consumo de dados.

#### APP User:
- Nome
- CNPJ

#### APP Transfer:
- pagador_nome
- pagador_banco
- pagador_agencia
- pagador_conta
- beneficiario_nome
- beneficiario_banco
- beneficiario_agencia
- beneficiario_conta
- valor
- status


## Tecnologias
Django framework versão 2.0.10,

Django REST Framework versão 3.9.1,

Linguagem de programação Python 3.6.5,

Banco de dados Sqlite3.


## Instalação

**1. Download do projeto via git clone**:

`$ git clone https://github.com/GilsonLeite/bank_transfer_system.git`

**2. Acesse o projeto e crie o ambiente virtual**:

`$ cd bank_transfer_system`

`virtualenv -p python3 venv`

`mkdir venv`

`. venv/bin/activate`

**3. Instalando as dependencias:**

`(venv)$ pip install -r requirements.txt`

**4. Criando o banco de dados e usuario:**

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

**5. Executando o projeto:**
`python manage.py runserver`


**6. Acessando API Root**
http://127.0.0.1:8000/api/v1/



### Endpoints
**Método**|**URL**|**Ação**
:--:|:--:|:--:
GET|`http://127.0.0.1:8000/api/v1/user/`|Lista os usuarios
GET|`http://127.0.0.1:8000/api/v1/user/<id>`|Detalhe do usuario
GET|`http://127.0.0.1:8000/api/v1/transfer/`|Lista da transferencia
GET|`http://127.0.0.1:8000/api/v1/transfer/<id>/`|Detalhe da transferencia


**Estrutura User**
```json
[
    {
        "name": "Gilson Leite",
        "cnpj": "1234567",
        "id": 1
    }
]
```

**Estrutura Transfer**
```json
{
    "user": {
        "nome": "Gilson Leite",
        "cnpj": "1234567"
    },
    "pagador_nome": "Moises",
    "pagador_banco": "237",
    "pagador_agencia": "2212",
    "pagador_conta": "2212",
    "beneficiario_nome": "Pedro",
    "beneficiario_banco": "212",
    "beneficiario_agencia": "2121",
    "beneficiario_conta": "328766",
    "valor": "200.00"
}

```