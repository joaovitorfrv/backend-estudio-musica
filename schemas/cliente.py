from pydantic import BaseModel, Field
from typing import List
from model.cliente import Cliente
from datetime import datetime, date

# Função para formatar o número de celular no padrão (XX) XXXXX-XXXX
def format_phone_number(phone_number: str) -> str:
    """
    Formata o número de telefone para o padrão (XX) XXXXX-XXXX.
    Remove caracteres não numéricos e aplica a formatação.
    """
    digits = ''.join(filter(str.isdigit, phone_number))  # Remove caracteres não numéricos
    return f'({digits[:2]}) {digits[2:7]}-{digits[7:]}'  # Formata o número

# Função para formatar a data
def format_date(data: str) -> date:
    """
    Converte uma string de data no formato 'YYYY-MM-DD' para um objeto date.
    """
    return datetime.strptime(data, '%Y-%m-%d').date()

# Schema para definir a estrutura de um cliente no sistema
class ClienteSchema(BaseModel):
    """
    Schema para representar um cliente sendo inserido.
    """
    nome: str = Field(..., example="João Vitor")
    data_nasc: date = Field(..., example="1989-05-16")
    celular: str = Field(..., example="(11) 9999-8888")
    email: str = Field(..., example="joao@exemplo.com")
    instrumentos: str = Field(..., example="Baixo")

# Schema para buscar um cliente pelo ID
class ClienteBuscaSchema(BaseModel):
    """
    Schema para busca de um cliente utilizando o ID.
    """
    id: int = Field(..., example=1)

# Schema para retornar a lista de clientes
class ListagemClientesSchema(BaseModel):
    """
    Schema para definir a estrutura de retorno de uma lista de clientes.
    """
    clientes: List[ClienteSchema]

# Função para apresentar uma lista de clientes formatada
def apresenta_clientes(clientes: List[Cliente]) -> dict:
    """
    Formata e retorna uma lista de clientes.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "data_nasc": cliente.data_nasc.strftime('%Y-%m-%d'),  # Formata a data de nascimento
            "celular": format_phone_number(cliente.celular),  # Formata o número de celular
            "email": cliente.email,
            "instrumentos": cliente.instrumentos,
            "data_cadastro": cliente.data_cadastro.strftime('%Y-%m-%d')  # Formata a data de cadastro
        })
    return {"clientes": result}

# Schema para visualizar um único cliente
class ClienteViewSchema(BaseModel):
    """
    Define como um cliente será retornado.
    """
    id: int = Field(..., example=1)
    nome: str = Field(..., example="João Vitor")
    data_nasc: date = Field(..., example="1989-05-16")
    celular: str = Field(..., example="(11) 9999-8888")
    email: str = Field(..., example="joao@exemplo.com")
    instrumentos: str = Field(..., example="Baixo")
    data_cadastro: str = Field(..., example="2024-09-01")

# Schema para excluir um cliente
class ClienteDelSchema(BaseModel):
    """
    Define a estrutura de resposta para exclusão de um cliente.
    """
    mensagem: str
    nome: str

# Função para apresentar um cliente formatado
def apresenta_cliente(cliente: Cliente) -> dict:
    """
    Retorna os dados formatados de um único cliente.
    """
    return {
        'nome': cliente.nome,
        'data_nasc': cliente.data_nasc.strftime('%Y-%m-%d'),  # Formata a data de nascimento para 'YYYY-MM-DD'
        'celular': format_phone_number(cliente.celular),  # Formata o número de celular de números para (XX) XXXXX-XXXX
        'email': cliente.email,
        'instrumentos': cliente.instrumentos,
        'data_cadastro': cliente.data_cadastro.strftime('%Y-%m-%d')  # Formata a data de cadastro para 'YYYY-MM-DD'
    }
