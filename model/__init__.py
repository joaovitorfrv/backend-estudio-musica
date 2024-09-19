'''

Esta classe cria e configura o banco de dados a ser utilizado no nosso API.
Define diretórios do BD, cria a engine, sessão e o próprio banco

'''
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os

from model.base import Base
from model.cliente import Cliente

# Diretório do banco de dados
db_path = "database/"

# Verificar se diretório já existe. Caso não, criar.
if not os.path.exists(db_path):
    os.makedirs(db_path)
    
# URL de acesso ao banco de dados SQLite.
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Cria a engine
# O comando echo=Façse faz com que os comandos SQL não sejam exibidos.
engine = create_engine(db_url, echo=False)

# Cria sessão a partir do engine, permitindo manipular o BD
Session = sessionmaker(bind=engine)

# Cria o banco de dados caso não exista.
if not database_exists(engine.url):
    create_database(engine.url)
    
# Cria as tabelas do banco
Base.metadata.create_all(engine)