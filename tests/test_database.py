import pytest
from utils.db_utils import execute_query
from utils.file_utils import load_query
from config.db_config import connect_to_db

engine = connect_to_db()

class TestLolEsports:
    def test_tabela_existe(self):
        query = load_query('check_table_exists')
        df = execute_query(engine, query)
        assert df['table_exists'][0], 'Tabela "2024_lol_esports" não existe!'

    def test_colunas_existem(self):
        expected_columns = [
            'gameid', 'datacompleteness', 'url', 'league', 'year', 'split', 'playoffs', 'date', 'game', 'patch', 'participantid',
            'side', 'position', 'playername', 'playerid', 'teamname', 'teamid', 'champion', 'ban1', 'ban2', 'ban3', 'ban4', 'ban5',
            'pick1', 'pick2', 'pick3', 'pick4', 'pick5', 'gamelength', 'result', 'kills', 'deaths', 'assists', 'teamkills',
            'teamdeaths', 'doublekills', 'triplekills', 'quadrakills', 'pentakills', 'firstblood', 'firstbloodkill',
            'firstbloodassist', 'firstbloodvictim', 'team kpm', 'ckpm', 'firstdragon', 'dragons', 'opp_dragons', 'elementaldrakes',
            'opp_elementaldrakes', 'infernals', 'mountains', 'clouds', 'oceans', 'chemtechs', 'hextechs', 'dragons (type unknown)', 
            'elders', 'opp_elders', 'firstherald', 'heralds', 'opp_heralds', 'void_grubs', 'opp_void_grubs', 'firstbaron', 'barons',
            'opp_barons', 'firsttower', 'towers', 'opp_towers', 'firstmidtower', 'firsttothreetowers', 'turretplates',
            'opp_turretplates', 'inhibitors', 'opp_inhibitors', 'damagetochampions', 'dpm', 'damageshare', 'damagetakenperminute',
            'damagemitigatedperminute', 'wardsplaced', 'wpm', 'wardskilled', 'wcpm', 'controlwardsbought', 'visionscore', 'vspm', 
            'totalgold', 'earnedgold', 'earned gpm', 'earnedgoldshare', 'goldspent', 'gspd', 'gpr', 'total cs', 'minionkills',
            'monsterkills', 'monsterkillsownjungle', 'monsterkillsenemyjungle', 'cspm', 'goldat10', 'xpat10', 'csat10', 'opp_goldat10', 
            'opp_xpat10', 'opp_csat10', 'golddiffat10', 'xpdiffat10', 'csdiffat10', 'killsat10', 'assistsat10', 'deathsat10',
            'opp_killsat10', 'opp_assistsat10', 'opp_deathsat10', 'goldat15', 'xpat15', 'csat15', 'opp_goldat15', 'opp_xpat15',
            'opp_csat15', 'golddiffat15', 'xpdiffat15', 'csdiffat15', 'killsat15', 'assistsat15', 'deathsat15', 'opp_killsat15',
            'opp_assistsat15', 'opp_deathsat15', 'goldat20', 'xpat20', 'csat20', 'opp_goldat20', 'opp_xpat20', 'opp_csat20',
            'golddiffat20', 'xpdiffat20', 'csdiffat20', 'killsat20', 'assistsat20', 'deathsat20', 'opp_killsat20', 'opp_assistsat20', 
            'opp_deathsat20', 'goldat25', 'xpat25', 'csat25', 'opp_goldat25', 'opp_xpat25', 'opp_csat25', 'golddiffat25', 'xpdiffat25',
            'csdiffat25', 'killsat25', 'assistsat25', 'deathsat25', 'opp_killsat25', 'opp_assistsat25', 'opp_deathsat25'
        ]
        query = load_query('check_columns_exist')
        df = execute_query(engine, query)['column_name'].tolist()
        missing = set(expected_columns) - set(df)
        assert not missing, f'Colunas ausentes: {missing}'

    def test_campos_obrigatorios_nao_nulos(self):
        required_columns = ['gameid', 'league', 'year', 'playername', 'teamname', 'champion']
        for col in required_columns:
            query = load_query('check_no_nulls_in_required_columns').replace('{{column_name}}', col)
            df = execute_query(engine, query)
            assert df['null_count'][0] == 0, f'Coluna {col} contém valores nulos!'

    def test_valores_nao_negativos(self):
        query = load_query('check_no_negative_values')
        df = execute_query(engine, query)
        assert df['negative_count'][0] == 0, 'Existem valores negativos em métricas!'

    def test_times_vitoriosos(self):
        query = load_query('count_victorious_teams')
        df = execute_query(engine, query)
        assert df['victorious_teams'][0] > 0, 'Nenhum time registrado como vencedor!'

    def test_numero_jogadores_unicos(self):
        query = load_query('count_unique_players')
        df = execute_query(engine, query)
        assert df['unique_players'][0] > 0, 'Não há jogadores únicos na tabela!'

    def test_campeoes_mais_jogados(self):
        query = load_query('most_played_champions')
        df = execute_query(engine, query)
        assert not df.empty, 'Não há campeões registrados como mais jogados!'

    def test_campeoes_nao_repetidos_em_uma_partida(self):
        query = load_query('unique_champions_per_game')
        df = execute_query(engine, query)
        assert df['repeated_champions'].empty, 'Há campeões repetidos em partidas!'

    def test_time_com_maior_media_de_kills(self):
        query = load_query('team_highest_avg_kills')
        df = execute_query(engine, query)
        assert not df.empty, 'Nenhum time encontrado com maior média de kills!'

    def test_duracao_media_de_jogos(self):
        query = load_query('average_game_length')
        df = execute_query(engine, query)
        assert df['average_length'][0] > 0, 'A duração média dos jogos é inválida!'

    def test_jogadores_com_mais_de_uma_pentakill(self):
        query = load_query('players_multiple_pentakills')
        df = execute_query(engine, query)
        assert not df.empty, 'Nenhum jogador possui múltiplas pentakills registradas!'

    def test_primeiro_sangue_registrado(self):
        query = load_query('games_with_first_blood')
        df = execute_query(engine, query)
        assert df['games_with_first_blood'][0] > 0, 'Nenhuma partida possui First Blood registrado!'

    def test_vitorias_por_lado(self):
        query = load_query('victories_by_side')
        df = execute_query(engine, query)
        assert df['blue_wins'][0] > 0 and df['red_wins'][0] > 0, 'Não há registro de vitórias para ambos os lados!'