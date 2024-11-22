"""
Este módulo contém uma função para criar uma conexão com o banco de dados PostgreSQL.
"""

from sqlalchemy import create_engine


def connect_to_db():
    """
    Cria e retorna um objeto de conexão com o banco de dados PostgreSQL.

    :return: Objeto de conexão do SQLAlchemy.
    """
    database_url = "postgresql://postgres:123456@localhost:5432/lol"
    return create_engine(database_url)
