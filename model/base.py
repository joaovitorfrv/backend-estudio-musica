'''
Cria uma classe para base, permitindo o instanciamento de novos objetos e tabelas
'''
import sqlalchemy
Base = sqlalchemy.orm.declarative_base()