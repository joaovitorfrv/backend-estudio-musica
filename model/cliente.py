from sqlalchemy import Column, String, Integer, DateTime, Date
from datetime import datetime
from model.base import Base

# Classe que define a estrutura da tabela 'cliente' no banco de dados
class Cliente(Base):
    __tablename__ = 'cliente'

    # Atributos da tabela cliente
    id = Column('pk_cliente', Integer, autoincrement=True, primary_key=True)  # Primary Key
    nome = Column(String(100), unique=True, nullable=False)  # Nome do cliente (único e obrigatório)
    data_nasc = Column(Date, nullable=False)  # Data de nascimento (obrigatória)
    celular = Column(String(13), unique=True, nullable=False)  # Número de celular (único e obrigatório)
    email = Column(String(90), unique=True, nullable=False)  # Email (único e obrigatório)
    instrumentos = Column(String(100), nullable=False)  # Equivalente a um comentário ou observação
    data_cadastro = Column(DateTime, default=datetime.now)  # Data de cadastro com valor padrão atual

    def __init__(self, nome: str, data_nasc: Date, celular: str, email: str, instrumentos: str):
        """
        Inicializa um novo cliente com as informações fornecidas.
        """
        self.nome = nome
        self.data_nasc = data_nasc
        self.celular = celular
        self.email = email
        self.instrumentos = instrumentos
