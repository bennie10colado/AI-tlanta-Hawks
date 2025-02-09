import pandas as pd

def analyze_team_performance(season):
    df = pd.read_csv(f"data/clean_games_{season}.csv")

    wins = df["WIN"].sum()
    losses = len(df) - wins

    stats = {
        "Total Jogos": [len(df)],
        "Total Vitórias": [wins],
        "Total Derrotas": [losses]
    }

    stats_df = pd.DataFrame(stats)
    stats_df.to_csv(f"data/team_stats_{season}.csv", index=False)
    print(f"✅ Estatísticas do time salvas em data/team_stats_{season}.csv")

analyze_team_performance('2023-24')
analyze_team_performance('2024-25')
