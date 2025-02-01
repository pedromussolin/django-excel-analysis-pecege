# Projeto PECEGE - Processamento de Planilha Excel com Django

Este projeto implementa um endpoint em Django para processar uma planilha Excel (.xlsx) contendo informações de pessoas, aplicar regras de negócio e retornar os dados em formato JSON.  
Além disso, há um endpoint bônus para gerar uma planilha Excel com os dados processados e a persistência dos dados em um banco MySQL, com gerenciamento via Django Admin.

## Funcionalidades

- **Upload da planilha (.xlsx):**  
  - Endpoint: `POST /upload-planilha/`
  - Processa os dados da planilha e aplica as regras:
    - Se a pessoa for menor de 18 anos, ela é marcada como inativa.
    - Se a coluna "ativo" estiver vazia, assume `True` (exceto para menores de 18).
    - Calcula um valor para cada pessoa ativa:
      - Menores de 21 anos: R$ 100,00
      - Entre 21 e 59 anos: R$ 150,00
      - 60 anos ou mais: R$ 200,00
  - Retorna um JSON com os dados das pessoas ativas.

- **Download da planilha (.xlsx):** (Bônus 1)
  - Endpoint: `GET /download-planilha/`
  - Gera e retorna uma planilha Excel com as informações das pessoas ativas.

- **Django Admin:** (Bônus 2)
  - Gerencie as informações das pessoas no Django Admin.
  - Modelo **Pessoa** com os campos: nome, e-mail, data de nascimento, ativo e valor.

## Tecnologias Utilizadas

- **Python 3**
- **Django**
- **MySQL**
- **openpyxl** para manipulação de planilhas Excel

## Pré-requisitos

- Python 3 instalado.
- MySQL instalado e em execução.
- [pip](https://pip.pypa.io/en/stable/) para instalar dependências.

## Configuração do Banco de Dados

1. Crie um banco de dados MySQL, por exemplo:


CREATE DATABASE pecege_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


2. Atualize o arquivo pecege/settings.py com as credenciais do seu banco de dados:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pecege_db',     # Nome do banco de dados
        'USER': 'seu_usuario',   # Seu usuário MySQL
        'PASSWORD': 'sua_senha', # Sua senha MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


## Instalação e Configuração

1. Clone este repositório:


git clone https://github.com/seu_usuario/projeto-pecege.git
cd projeto-pecege


2. Crie um ambiente virtual:


python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate


3. Instale as dependências:


pip install -r requirements.txt


4. Execute as migrações do Django:


python manage.py makemigrations
python manage.py migrate


5. Crie um superusuário para acessar o Django Admin:


python manage.py createsuperuser


## Executando o Projeto

1. Inicie o servidor Django:


python manage.py runserver


2. Acesse o endpoint de upload (utilizei o Postman):

- URL: http://127.0.0.1:8000/upload-planilha/
- Método: POST
- Na aba Body, selecione form-data:
  - Chave: file
  - Type: File
  - Valor: (arquivo Excel .xlsx com as colunas nome, e-mail, data de nascimento e ativo)

3. Acesse o endpoint de download para baixar a planilha:

- URL: http://127.0.0.1:8000/download-planilha/
- Método: GET

4. Acesse o Django Admin (após criar o superusuário):
- URL: http://127.0.0.1:8000/admin/
