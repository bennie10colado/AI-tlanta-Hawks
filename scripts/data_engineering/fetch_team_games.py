import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder

# RF7 - PROJ 1
def fetch_team_games(team_id, season='2023-24'):
    """ Obtém jogos de um time específico e salva os dados em CSV. """
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id, season_nullable=season)
    games = gamefinder.get_data_frames()[0]

    # Salvar os jogos da temporada em CSV
    games.to_csv(f"data/games_{season}.csv", index=False)
    print(f"✅ Jogos da temporada {season} salvos em data/games_{season}.csv")

# Exemplo: Coletar jogos do Atlanta Hawks (ID: 1610612737)
fetch_team_games(1610612737, '2023-24')
fetch_team_games(1610612737, '2024-25')
