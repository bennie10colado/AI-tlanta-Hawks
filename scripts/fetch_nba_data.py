import requests
import pandas as pd
import os

# Criar diretório de dados se não existir
os.makedirs("data", exist_ok=True)

class NBADataFetcher:
    API_URL = "https://stats.nba.com/stats/leaguedashteamstats"
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nba.com/",
    }

    def fetch_team_stats(self, season="2023-24"):
        params = {"Season": season, "SeasonType": "Regular Season", "PerMode": "PerGame"}
        response = requests.get(self.API_URL, headers=self.HEADERS, params=params)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
            return df
        else:
            raise Exception(f"API Error: {response.status_code}")

# Executar a coleta de dados
fetcher = NBADataFetcher()
df = fetcher.fetch_team_stats()

# Filtrar apenas o Atlanta Hawks
df_hawks = df[df["TEAM_NAME"] == "Atlanta Hawks"]

# Salvar os dados em CSV
csv_path = "data/nba_hawks_stats.csv"
df_hawks.to_csv(csv_path, index=False)
print(f"✅ Dados do Atlanta Hawks salvos em {csv_path}")
