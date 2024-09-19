from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from flask_cors import CORS
from datetime import datetime


# Importações do modelo e schemas
from model import Session, Cliente
from schemas import *

# Informações gerais sobre a API
info = Info(title="Estúdio de Música", version='0.0.2')
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição de tags usadas na documentação da API
home_tag = Tag(name="Documentação", description="Acessa a documentação")
cliente_tag = Tag(name="Cliente", description="Gerencia cadastro de clientes")

# Redireciona para a documentação da API OpenAPI3
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')


# ==========================
# Endpoints relacionados ao Cliente
# ==========================

@app.post('/cliente', tags=[cliente_tag],
          responses={'200': ClienteViewSchema})
def add_cliente(form: ClienteSchema):
    """
    Cadastra um novo cliente na base de dados.
    """
    try:
        # Captura os dados enviados via formulário
        data_nasc_str = request.form['data_nasc']
        nome = request.form['nome']
        celular = request.form['celular']
        email = request.form['email']
        instrumentos = request.form['instrumentos']

        # Converte a data de nascimento de string para objeto date
        data_nasc = datetime.strptime(data_nasc_str, '%Y-%m-%d').date()
        cliente = Cliente(
            nome=nome,
            data_nasc=data_nasc,
            celular=celular,
            email=email,
            instrumentos=instrumentos
        )

        with Session() as session:
            session.add(cliente)
            session.commit()

            # Retorna o ID do cliente recém-criado
            return jsonify({
                "id": cliente.id,
                "message": "Cliente cadastrado com sucesso."
            }), 200

    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")
        return jsonify({"error": str(e)}), 500


@app.get('/clientes', tags=[cliente_tag],
         responses={'200': ListagemClientesSchema, '404': ErrorSchema})
def get_clientes():
    """
    Retorna todos os clientes cadastrados.
    """
    with Session() as session:
        clientes = session.query(Cliente).all()

    if not clientes:
        return {"clientes": []}, 200
    return apresenta_clientes(clientes), 200


@app.get('/cliente', tags=[cliente_tag],
         responses={'200': ClienteViewSchema})
def get_cliente(query: ClienteBuscaSchema):
    """
    Busca um cliente pelo ID.
    """
    cliente_id = query.id
    with Session() as session:
        cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        return {"message": "Cliente não encontrado"}, 404
    return apresenta_cliente(cliente), 200


@app.delete('/cliente', tags=[cliente_tag],
            responses={'200': ClienteDelSchema, '404': ErrorSchema}, methods=['DELETE'])
def del_cliente(query: ClienteBuscaSchema):
    """
    Exclui um cliente pelo ID.
    """
    with Session() as session:
        cliente_id = query.id
        cliente = session.query(Cliente).get(cliente_id)

    if cliente:        
        session.delete(cliente)
        session.commit()
        return jsonify({"message": "Cliente removido", "id": cliente_id})
    return jsonify({"message": "Cliente não encontrado"}, 404)


# Edita o cliente
@app.put('/cliente', tags=[cliente_tag],
         responses={'200': ClienteViewSchema}, methods=['PUT'])
def update_cliente():
    '''
    Atualiza as informações de um cliente existente
    '''
    data = request.form
    id = data.get('id')
    if not id:
        return jsonify({"message": "ID não fornecido"}), 400
    # Busca o cliente pelo ID
    with Session() as session:
        cliente = session.query(Cliente).filter(Cliente.id == id).first()

    # Caso não encontre cliente
    if not cliente:
        return jsonify({"message": "Cliente não encontrado"}), 404


    cliente.nome = data.get('nome')
    # Converte a data de nascimento recebida em string para um objeto date
    data_nasc_str = data.get('data_nasc')
    cliente.data_nasc = datetime.strptime(data_nasc_str, '%Y-%m-%d').date()  # Converte a string para date
    cliente.email = data.get('email')
    cliente.celular = data.get('celular')
    cliente.instrumentos = data.get('instrumentos')

    session.commit()

    return jsonify({"id": cliente.id, "message": "Cliente atualizado com sucesso"}), 200

