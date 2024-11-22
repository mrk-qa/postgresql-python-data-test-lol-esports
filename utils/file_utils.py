import os

def load_query(query_name: str) -> str:
    """
    Carrega o conteúdo de um arquivo SQL da pasta de queries.
    :param query_name: Nome do arquivo SQL sem a extensão
    :return: Conteúdo da query como string
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    queries_dir = os.path.join(base_dir, '../queries')
    query_path = os.path.join(queries_dir, f'{query_name}.sql')
    
    if not os.path.exists(query_path):
        raise FileNotFoundError(f'Query "{query_name}.sql" não encontrada!')
    
    with open(query_path, 'r', encoding='utf-8') as file:
        return file.read()
