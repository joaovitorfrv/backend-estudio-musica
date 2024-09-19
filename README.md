# Cadastro de Clientes para Estúdio de Música

Este projeto permite o gerenciamento de clientes para um estúdio de música. Com ele, você pode cadastrar, editar, excluir e buscar clientes, além de visualizar uma lista completa dos cadastrados. O backend foi desenvolvido com **Flask** e o frontend utiliza **HTML**, **CSS** e **JavaScript**.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x**
- **Virtualenv**
- **Flask**
- Pacotes adicionais listados no `requirements.txt`

## Instalação e Configuração

### 1. Clonando o repositório

```bash
git clone https://github.com/joaovitorfrv/Engenharia-de-Software-MVP-Sprint-1
cd Engenharia-de-Software-MVP-Sprint-1
```

### 2. Criando e ativando o ambiente virtual

Na raiz do diretório do projeto, crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No **Windows**:

```bash
.\venv\Scripts\activate
```

- No **Linux/MacOS**:

```bash
source venv/bin/activate
```

### 3. Instalando as dependências

Com o ambiente virtual ativo, instale todas as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Executando o Projeto

### 1. Iniciando a API

Navegue até o diretório `app_api` e execute o servidor Flask:

```bash
cd app_api
flask run --host 0.0.0.0 --port 5000
```

### 2. Acessando a API

Abra o navegador e acesse a documentação da API (OpenAPI) no seguinte endereço:

```bash
http://127.0.0.1:5000
```

Recomenda-se o uso do **Swagger** para realizar testes da API.

## Funcionalidades

Este projeto oferece as seguintes funcionalidades:

- **Listar Clientes**: Visualize todos os clientes cadastrados.
- **Cadastrar Cliente**: Adicione um novo cliente com nome, data de nascimento, e-mail, celular e instrumentos.
- **Editar Cliente**: Atualize as informações de um cliente existente.
- **Excluir Cliente**: Remova um cliente do banco de dados.
- **Buscar Cliente**: Encontre clientes pelo nome através da barra de busca.

## Estrutura do Projeto

```bash
├── app_api
│   ├── app.py            # Arquivo principal da API
│   ├── model             # Modelos do banco de dados
│   ├── schemas           # Schemas para validação
│   └── database          # Diretório contendo o banco de dados SQLite
├── app_front_end
│   ├── index.html        # Página principal (frontend)
│   ├── style.css         # Estilos da página
│   └── script.js         # Lógica do frontend (JavaScript)
├── venv                  # Ambiente virtual Python
├── requirements.txt       # Dependências do projeto
└── README.md             # Arquivo atual com instruções
```

## Observações

- Certifique-se de que o **ambiente virtual** está ativado ao rodar os comandos do Flask.
- A aplicação está configurada para rodar no `localhost:5000`, mas você pode alterar o `host` e `port` conforme necessário.
- Para adicionar novos clientes ou realizar buscas, utilize o formulário presente na interface web ou faça requisições diretamente via **Swagger** na documentação **OpenAPI**.

## Autor

- **João Vitor M. Frugiuele**

## Licença

Este projeto está licenciado sob a licença **MIT**.
