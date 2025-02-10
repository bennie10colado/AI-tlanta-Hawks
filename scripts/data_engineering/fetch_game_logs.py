import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playergamelogs

# Função para carregar os dados dos jogadores do Atlanta Hawks
def load_game_logs(season="2024-25"):
    player_ids = {
        "Clint Capela": 203991,
        "Trae Young": 1629027,
        "Jalen Johnson": 1630552
    }

    game_logs = []
    
    for name, player_id in player_ids.items():
        player_log = playergamelogs.PlayerGameLogs(player_id_nullable=player_id, season_nullable=season).get_dict()
        games = player_log['resultSets'][0]['rowSet']
        headers = player_log['resultSets'][0]['headers']
        
        for game in games:
            game_data = dict(zip(headers, game))
            matchup = game_data["MATCHUP"]
            home_away = "Home" if "vs." in matchup else "Away"
            opponent = matchup.split("vs. ")[-1] if "vs." in matchup else matchup.split("@ ")[-1]
            
            game_logs.append({
                "Jogador": name,
                "Data do Jogo": game_data["GAME_DATE"],
                "Adversário": opponent,
                "Casa/Fora": home_away,
                "Vitória/Derrota": game_data["WL"]
            })

    df = pd.DataFrame(game_logs)
    df.to_csv("data/game_logs.csv", index=False)

    return df

