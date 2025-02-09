# RF2 - PROJ 1
import requests
import pandas as pd

def fetch_nba_standings():
    """Obtém a classificação atual da NBA por conferência e salva em CSV."""
    API_URL = "https://stats.nba.com/stats/leaguestandings"
    HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.nba.com/"}

    params = {
        "LeagueID": "00",
        "Season": "2023-24",
        "SeasonType": "Regular Season"
    }

    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=10)

        if response.status_code != 200:
            raise ValueError(f"Erro ao obter dados da API. Código: {response.status_code}")

        data = response.json()

        # 🔍 Adicionar depuração para entender a resposta da API
        print("📊 JSON da API:", data)

        if "resultSets" not in data or not data["resultSets"][0]["rowSet"]:
            raise ValueError("A API não retornou dados. Verifique se a temporada está em andamento.")

        df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])

        # 🔍 Verificar as colunas disponíveis
        print(f"📊 Colunas disponíveis na API: {df.columns.tolist()}")

        colunas_esperadas = ["TEAM_NAME", "CONF_NAME", "W_PCT", "WINS", "LOSSES"]
        colunas_existentes = [col for col in colunas_esperadas if col in df.columns]

        if not colunas_existentes:
            raise ValueError(f"A API não retornou colunas esperadas. Colunas disponíveis: {df.columns.tolist()}")

        df = df[colunas_existentes]
        df.rename(columns={"TEAM_NAME": "Time", "CONF_NAME": "Conferencia", "W_PCT": "Percentual_Vitórias",
                           "WINS": "Vitórias", "LOSSES": "Derrotas"}, inplace=True)

        df.to_csv("data/nba_standings.csv", index=False)
        print("✅ Classificação da NBA salva em data/nba_standings.csv")

    except Exception as e:
        print(f"❌ Erro ao obter classificação da NBA: {e}")

if __name__ == "__main__":
    fetch_nba_standings()
