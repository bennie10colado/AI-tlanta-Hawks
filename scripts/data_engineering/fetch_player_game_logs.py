# RF2 - PROJ 2
import pandas as pd
import os
from nba_api.stats.endpoints import playergamelogs, boxscoresummaryv2

def convert_minutes(minutes_decimal):
    """ Converte minutos decimais para formato MM:SS """
    try:
        total_seconds = int(float(minutes_decimal) * 60)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"  # Exemplo: 37.53 → "37:32"
    except:
        return "N/A"

def get_game_score(game_id):
    """ Busca o placar final do jogo usando o GAME_ID """
    try:
        boxscore = boxscoresummaryv2.BoxScoreSummaryV2(game_id=game_id).get_dict()
        linescore = boxscore['resultSets'][5]['rowSet']  # Linha com placar dos times

        team_scores = {row[3]: row[21] for row in linescore}  # {'ATL': 120, 'MIL': 115}
        return f"{team_scores.get('ATL', 'N/A')} - {team_scores.get('MIL', 'N/A')}"  # Exemplo: "120 - 115"
    except Exception as e:
        print(f"⚠ Erro ao buscar placar do jogo {game_id}: {e}")
        return "N/A"


def fetch_player_game_logs(season="2024-25"):
    """ Obtém e salva os dados de todos os jogos dos jogadores do Atlanta Hawks na temporada atual. """
    try:
        # IDs dos jogadores do Atlanta Hawks
        player_ids = {
            "Clint Capela": 203991,
            "Trae Young": 1629027,
            "Jalen Johnson": 1630552
        }

        # Lista para armazenar informações dos jogos dos jogadores
        game_logs = []

        # Buscar estatísticas dos jogos para cada jogador
        for name, player_id in player_ids.items():
            try:
                player_log = playergamelogs.PlayerGameLogs(player_id_nullable=player_id, season_nullable=season).get_dict()
                games = player_log['resultSets'][0]['rowSet']
                game_headers = player_log['resultSets'][0]['headers']  # Pegamos os nomes das colunas

                for game in games:
                    game_data = dict(zip(game_headers, game))

                    # Extração segura dos dados
                    #game_id = game_data.get("GAME_ID", "N/A")
                    game_date = game_data.get("GAME_DATE", "N/A")  # Data do jogo
                    matchup = game_data.get("MATCHUP", "N/A")  # Formato: "ATL @ MIL" ou "ATL vs. BOS"
                    win_loss = game_data.get("WL", "N/A")  # Vitória ou Derrota
                    points = game_data.get("PTS", 0)  # Pontos
                    rebounds = game_data.get("REB", 0)  # Rebotes
                    assists = game_data.get("AST", 0)  # Assistências
                    #game_score = get_game_score(game_id) # placar
                    game_score = "OFFLINE"
                    fg3_attempted = game_data.get("FG3A", 0)  # Tentativas de 3 pontos
                    fg3_made = game_data.get("FG3M", 0)  # Cestas de 3 pontos
                    minutes_played = convert_minutes(game_data.get("MIN", "0"))  # Tempo de quadra corrigido

                    # Determinar o adversário e se o jogo foi em casa ou fora
                    if "@" in matchup:
                        opponent = matchup.split(" @ ")[1]  # Time adversário
                        home_away = "Away"
                    else:
                        opponent = matchup.split(" vs. ")[1]  # Time adversário
                        home_away = "Home"

                    # Adicionar os dados à lista
                    game_logs.append([name, game_date, opponent, win_loss, home_away, points, rebounds, assists, game_score, fg3_attempted, fg3_made, minutes_played])

            except Exception as e:
                print(f"⚠ Erro ao buscar estatísticas de {name}: {e}")

        # Criar um DataFrame para melhor visualização
        df = pd.DataFrame(game_logs, columns=["Jogador", "Data do Jogo", "Adversário", "Vitória/Derrota", "Casa/Fora", "Pontos", "Rebotes",
                                              "Assistências", "Placar do Jogo", "Tentativas de 3 PTS", "Cestas de 3 PTS", "Tempo de Permanência do Jogador em Quadra"])

        # Criar diretório se não existir
        os.makedirs("data", exist_ok=True)

        # Salvar CSV
        file_path = f"data/player_game_logs_{season}.csv"
        df.to_csv(file_path, index=False)

        # Exibir os dados coletados
        print("✅ Estatísticas dos jogadores salvas em:", file_path)
        print(df.head())

    except Exception as e:
        print(f"❌ Erro ao obter as estatísticas dos jogadores: {e}")

if __name__ == "__main__":
    fetch_player_game_logs()
