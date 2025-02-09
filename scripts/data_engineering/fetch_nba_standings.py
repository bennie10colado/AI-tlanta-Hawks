import requests
import pandas as pd

# RF2 - PROJ 1
def fetch_nba_standings():
    """ Obtém a classificação atual da NBA por conferência e salva em CSV. """
    API_URL = "https://stats.nba.com/stats/leaguestandings"
    HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.nba.com/"}

    params = {
        "LeagueID": "00",
        "Season": "2023-24",
        "SeasonType": "Regular Season"
    }

    response = requests.get(API_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])

        # Selecionar colunas relevantes
        df = df[["TeamName", "Conference", "WinPCT", "WINS", "LOSSES"]]
        df.rename(columns={"TeamName": "Time", "WinPCT": "Percentual_Vitórias", "WINS": "Vitórias", "LOSSES": "Derrotas"}, inplace=True)

        # Salvar os dados
        df.to_csv("data/nba_standings.csv", index=False)
        print("✅ Classificação da NBA salva em data/nba_standings.csv")
    else:
        print(f"❌ Erro ao obter dados da API. Código: {response.status_code}")

if __name__ == "__main__":
    fetch_nba_standings()
