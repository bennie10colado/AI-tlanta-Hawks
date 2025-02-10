import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# RF1 - PROJ 1
def fetch_nba_players():
    """ Obtém e salva a lista de times da NBA agrupados por Conferência. """
    try:
# IDs dos jogadores na NBA API (IDs conhecidos para evitar varredura)
        player_ids = {
            "Clint Capela": 203991,
            "Trae Young": 1629027,
            "Jalen Johnson": 1630552
        }

# Lista para armazenar informações
        hawks_players = []

# Buscar detalhes dos jogadores
        for name, player_id in player_ids.items():
            player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_dict()
            player_info_data = player_info['resultSets'][0]['rowSet'][0]

# Extrair dados
            height = player_info_data[10]  # Altura
            weight = player_info_data[11]  # Peso
            age = player_info_data[6]      # Idade
            experience = player_info_data[12]  # Experiência
            position = player_info_data[14]    # Posição
            college = player_info_data[8]      # Universidade
            salary = player_info_data[17]      # Salário (pode estar indisponível)

            # Converter Rookie para 0
            experience = 0 if experience == "R" else experience

            hawks_players.append([player_id, name, height, weight, age, experience, position, college, salary])

# Criar um DataFrame para melhor visualização
        df = pd.DataFrame(hawks_players, columns=['ID', 'Nome', 'Altura', 'Peso', 'Idade', 'Experiência', 'Posição', 'Universidade', 'Salário'])

        df.to_csv("data/player_stats.csv")
        print("✅ Lista de jogadores salva em data")

    except Exception as e:
        print(f"❌ Erro ao obter os times da NBA: {e}")

if __name__ == "__main__":
    fetch_nba_players()
