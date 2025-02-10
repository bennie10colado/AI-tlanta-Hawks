# RF1 - PROJ 2 - Coleta de dados dos jogadores
import pandas as pd
import os
from nba_api.stats.endpoints import commonplayerinfo

def fetch_nba_players():
    """ Obtém e salva a lista de jogadores do Atlanta Hawks com detalhes importantes. """
    try:
        # IDs dos jogadores na NBA API (IDs conhecidos para evitar varredura)
        player_ids = {
            "Clint Capela": 203991,
            "Trae Young": 1629027,
            "Jalen Johnson": 1630552
        }

        # Lista para armazenar informações dos jogadores
        hawks_players = []

        # Buscar detalhes dos jogadores
        for name, player_id in player_ids.items():
            try:
                player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_dict()
                player_headers = player_info['resultSets'][0]['headers']  # ✅ Pegamos os nomes das colunas
                player_data = player_info['resultSets'][0]['rowSet'][0]

                # Criar um dicionário associando os headers aos valores extraídos
                player_dict = dict(zip(player_headers, player_data))

                # Extração usando os nomes das colunas
                birthdate = player_dict.get("BIRTHDATE", "N/A")  # Data de nascimento
                college = player_dict.get("SCHOOL", "N/A")  # Universidade
                country = player_dict.get("COUNTRY", "N/A")  # País de origem
                height = player_dict.get("HEIGHT", "N/A")  # Altura
                weight = player_dict.get("WEIGHT", "N/A")  # Peso
                experience = player_dict.get("SEASON_EXP", "N/A")  # Experiência
                position = player_dict.get("POSITION", "N/A")  # Posição
                salary = player_dict.get("DRAFT_NUMBER", "N/A")  # Draft Number (sem salário disponível na API)

                # Converter Rookie para 0
                experience = 0 if experience == "R" else int(experience) if experience != "N/A" else "N/A"

                # Calcular idade do jogador
                birth_year = int(birthdate[:4]) if birthdate != "N/A" else 0
                current_year = 2024  # Atualizar para o ano correto
                age = current_year - birth_year if birth_year else "N/A"

                # Adicionar ao DataFrame
                hawks_players.append([name, height, weight, age, experience, position, college, country, salary])
            except Exception as e:
                print(f"⚠ Erro ao buscar informações de {name}: {e}")

        # Criar um DataFrame para melhor visualização
        df = pd.DataFrame(hawks_players, columns=['Nome', 'Altura', 'Peso', 'Idade', 'Experiência', 'Posição', 'Universidade', 'País', 'Salário'])

        # Criar diretório se não existir
        os.makedirs("data", exist_ok=True)

        # Salvar CSV
        file_path = "data/player_stats.csv"
        df.to_csv(file_path, index=False)

        # Exibir os dados coletados
        print("✅ Lista de jogadores salva em:", file_path)
        print(df)

    except Exception as e:
        print(f"❌ Erro ao obter os jogadores da NBA: {e}")

if __name__ == "__main__":
    fetch_nba_players()
