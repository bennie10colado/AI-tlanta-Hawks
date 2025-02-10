# RF2 - PROJ 1
import os
import requests
import pandas as pd

def fetch_nba_standings():
    """Obtém a classificação atual da NBA por conferência e salva em CSV."""
    API_URL = "https://stats.nba.com/stats/leaguestandings"
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nba.com/",
        "Accept": "application/json"
    }

    params = {
        "LeagueID": "00",
        "Season": "2023-24",
        "SeasonType": "Regular Season"
    }

    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()  # Levanta erro para códigos HTTP ruins (4xx, 5xx)

        data = response.json()

        if "resultSets" not in data or not data["resultSets"][0]["rowSet"]:
            raise ValueError("A API não retornou dados. Verifique se a temporada está em andamento.")

        df = pd.DataFrame(data["resultSets"][0]["rowSet"], columns=data["resultSets"][0]["headers"])

        # 🔍 Verificar as colunas disponíveis
        print(f"📊 Colunas disponíveis na API: {df.columns.tolist()}")

        # Ajustar para os nomes corretos das colunas
        colunas_esperadas = ["TeamName", "Conference", "WinPct", "WINS", "LOSSES"]
        colunas_existentes = [col for col in colunas_esperadas if col in df.columns]

        if not colunas_existentes:
            raise ValueError(f"A API não retornou colunas esperadas. Colunas disponíveis: {df.columns.tolist()}")

        df = df[colunas_existentes]
        df.rename(columns={
            "TeamName": "Time",
            "Conference": "Conferencia",
            "WinPct": "Percentual_Vitórias",
            "WINS": "Vitórias",
            "LOSSES": "Derrotas"
        }, inplace=True)

        # Criar diretório para salvar o arquivo
        os.makedirs("data", exist_ok=True)

        df.to_csv("data/nba_standings.csv", index=False)
        print("✅ Classificação da NBA salva em data/nba_standings.csv")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar à API da NBA: {e}")
    except ValueError as e:
        print(f"❌ Erro nos dados recebidos: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    fetch_nba_standings()
