import pandas as pd
from nba_api.stats.static import teams

#RF1
def fetch_nba_teams():
    """ Obtém e salva a lista de times da NBA agrupados por Conferência. """
    nba_teams = teams.get_teams()
    df_teams = pd.DataFrame(nba_teams)

    # Definir a conferência manualmente
    east_teams = [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
        "Detroit Pistons", "Indiana Pacers", "Miami Heat", "Milwaukee Bucks", "New York Knicks", "Orlando Magic",
        "Philadelphia 76ers", "Toronto Raptors", "Washington Wizards"
    ]

    df_teams["Conferencia"] = df_teams["full_name"].apply(lambda x: "Leste" if x in east_teams else "Oeste")

    # Salvar os dados
    df_teams.to_csv("data/nba_teams.csv", index=False)
    print("✅ Lista de times salva em data/nba_teams.csv")

fetch_nba_teams()
