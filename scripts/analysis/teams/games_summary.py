# RF7 - PROJ 1
import pandas as pd
import os

def generate_games_summary(season):
    file_path = f"data/clean_games_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # Verificar colunas necessárias
        required_columns = ["GAME_DATE", "OPPONENT", "WL", "HOME_AWAY", "PTS", "PTS_OPP"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do Atlanta Hawks
        df_hawks = df[df["TEAM"] == "Atlanta Hawks"]

        # Criar resumo dos jogos
        df_summary = df_hawks[["GAME_DATE", "OPPONENT", "WL", "HOME_AWAY", "PTS", "PTS_OPP"]]
        df_summary.rename(columns={
            "GAME_DATE": "Data do Jogo",
            "OPPONENT": "Adversário",
            "WL": "Vitória/Derrota",
            "HOME_AWAY": "Casa/Fora",
            "PTS": "Placar Atlanta Hawks",
            "PTS_OPP": "Placar Adversário"
        }, inplace=True)

        df_summary.to_csv(f"data/games_summary_{season}.csv", index=False)
        print(f"✅ Resumo dos jogos salvo em data/games_summary_{season}.csv")

    except Exception as e:
        print(f"❌ Erro ao gerar resumo dos jogos: {e}")

if __name__ == "__main__":
    generate_games_summary("2023-24")
    generate_games_summary("2024-25")
