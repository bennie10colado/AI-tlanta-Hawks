# RF6 - PROJ 1
import pandas as pd
import os

def generate_defensive_stats(season):
    file_path = f"data/clean_games_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # 🔍 Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Renomear TEAM_NAME para TEAM se necessário
        if "TEAM_NAME" in df.columns and "TEAM" not in df.columns:
            df.rename(columns={"TEAM_NAME": "TEAM"}, inplace=True)

        # Verificar colunas necessárias
        required_columns = ["TEAM", "STL", "DREB", "BLK", "TOV", "PF"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do Atlanta Hawks
        df_hawks = df[df["TEAM"] == "Atlanta Hawks"]

        # Calcular estatísticas defensivas
        stats = {
            "Total Jogos": [len(df_hawks)],
            "Roubos de Bola por Jogo": [df_hawks["STL"].mean()],
            "Rebotes Defensivos por Jogo": [df_hawks["DREB"].mean()],
            "Tocos por Jogo": [df_hawks["BLK"].mean()],
            "Erros por Jogo": [df_hawks["TOV"].mean()],
            "Faltas por Jogo": [df_hawks["PF"].mean()]
        }

        stats_df = pd.DataFrame(stats)
        stats_df.to_csv(f"data/defensive_stats_{season}.csv", index=False)
        print(f"✅ Estatísticas defensivas salvas em data/defensive_stats_{season}.csv")

    except Exception as e:
        print(f"❌ Erro ao gerar estatísticas defensivas: {e}")

if __name__ == "__main__":
    generate_defensive_stats("2023-24")
    generate_defensive_stats("2024-25")
