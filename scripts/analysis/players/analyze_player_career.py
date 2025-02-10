# RF9, RF10 - PROJ 2
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from nba_api.stats.endpoints import playercareerstats

def convert_time_to_minutes(time_str):
    """
    Converte tempo no formato MM:SS para minutos decimais.
    """
    try:
        minutes, seconds = map(int, time_str.split(":"))
        return minutes + (seconds / 60)
    except:
        return None  # Retorna None para valores inválidos

def fetch_player_career_stats(season="2024-25"):
    """
    Fetches the career statistics of players and compares them with the current season.
    Saves the data to a CSV file.
    """
    # Define player IDs
    player_ids = {
        "Clint Capela": 203991,
        "Trae Young": 1629027,
        "Jalen Johnson": 1630552
    }

    # Paths
    current_season_path = f"data/player_game_logs_{season}.csv"
    output_path = f"data/player_career_comparison_{season}.csv"

    # Load current season data
    if not os.path.exists(current_season_path):
        raise FileNotFoundError(f"❌ File not found: {current_season_path}")

    df_season = pd.read_csv(current_season_path)

    # Ensure required columns exist
    required_columns = ["Jogador", "Pontos", "Rebotes", "Assistências", "Tempo de Permanência do Jogador em Quadra"]
    for col in required_columns:
        if col not in df_season.columns:
            raise ValueError(f"🚨 Missing required column: {col}")

    # Normalize player names
    df_season["Jogador"] = df_season["Jogador"].str.strip()

    # Convert "Tempo de Permanência do Jogador em Quadra" to minutes
    df_season["Minutos"] = df_season["Tempo de Permanência do Jogador em Quadra"].astype(str).apply(convert_time_to_minutes)

    # Dictionary to store player statistics
    player_comparison = []

    # Fetch career data
    for player, player_id in player_ids.items():
        try:
            # Fetch career stats from NBA API
            career_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]

            # Extract career totals
            career_games = career_stats["GP"].sum()
            career_points = career_stats["PTS"].sum()
            career_assists = career_stats["AST"].sum()
            career_rebounds = career_stats["REB"].sum()

            # Compute career averages
            avg_career_points = career_points / career_games if career_games else 0
            avg_career_assists = career_assists / career_games if career_games else 0
            avg_career_rebounds = career_rebounds / career_games if career_games else 0

            # Current season stats
            player_df = df_season[df_season["Jogador"] == player]

            total_games = player_df.shape[0]
            total_points = player_df["Pontos"].sum()
            total_assists = player_df["Assistências"].sum()
            total_rebounds = player_df["Rebotes"].sum()

            avg_points = player_df["Pontos"].mean()
            avg_assists = player_df["Assistências"].mean()
            avg_rebounds = player_df["Rebotes"].mean()

            avg_minutes = player_df["Minutos"].mean()

            # Debugging: Verificar estatísticas processadas
            print(f"🔹 {player}: Jogos: {total_games}, Média PTS: {avg_points}, Média AST: {avg_assists}, Média REB: {avg_rebounds}, Minutos: {avg_minutes}")

            # Append data to the list
            player_comparison.append([
                season, player, total_games, avg_points, avg_assists, avg_rebounds, avg_minutes,
                career_games, avg_career_points, avg_career_assists, avg_career_rebounds
            ])

        except Exception as e:
            print(f"⚠ Error retrieving stats for {player}: {e}")

    # Convert to DataFrame
    columns = [
        "Temporada", "Jogador", "Total Jogos (Atual)", "Média Pontos (Atual)", "Média Assistências (Atual)", "Média Rebotes (Atual)", "Minutos por Jogo (Atual)",
        "Total Jogos (Carreira)", "Média Pontos (Carreira)", "Média Assistências (Carreira)", "Média Rebotes (Carreira)"
    ]
    df_comparison = pd.DataFrame(player_comparison, columns=columns)

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    df_comparison.to_csv(output_path, index=False)

    print(f"✅ Career vs. Current season statistics saved to {output_path}")
    print(df_comparison)

if __name__ == "__main__":
    fetch_player_career_stats("2024-25")
