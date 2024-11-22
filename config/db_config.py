from sqlalchemy import create_engine

def connect_to_db():
    database_url = "postgresql://postgres:123456@localhost:5432/lol"
    return create_engine(database_url)