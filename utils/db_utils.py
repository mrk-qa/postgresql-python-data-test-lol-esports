import pandas as pd
from sqlalchemy.engine import Engine

def execute_query(engine: Engine, query: str, params: dict = None) -> pd.DataFrame:
    """
    Executa uma consulta SQL e retorna os resultados como DataFrame.
    :param engine: Objeto de conexão do SQLAlchemy
    :param query: Consulta SQL
    :param params: Parâmetros opcionais para a consulta
    :return: DataFrame com os resultados
    """
    with engine.connect() as conn:
        return pd.read_sql_query(query, conn, params=params)
