# RF4, RF5 - PROJ 1
# RF4, RF5 - PROJ 1
import pandas as pd
import os

def generate_offensive_stats(season="2023-24"):
    file_path = f"data/clean_games_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # 🔍 Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Criar FG2M se não existir
        if "FG2M" not in df.columns and "FGM" in df.columns and "FG3M" in df.columns:
            df["FG2M"] = df["FGM"] - df["FG3M"]

        # Verificar colunas necessárias
        required_columns = ["TEAM_NAME", "PTS", "AST", "REB", "FG3M", "FG2M", "FTM"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do Atlanta Hawks
        df_hawks = df[df["TEAM_NAME"] == "Atlanta Hawks"]

        # Calcular estatísticas ofensivas
        stats = {
            "Total Jogos": [len(df_hawks)],
            "Pontos por Jogo": [df_hawks["PTS"].mean()],
            "Assistências por Jogo": [df_hawks["AST"].mean()],
            "Rebotes por Jogo": [df_hawks["REB"].mean()],
            "Cestas de 3 Pontos Convertidas": [df_hawks["FG3M"].mean()],
            "Cestas de 2 Pontos Convertidas": [df_hawks["FG2M"].mean()],
            "Lances Livres Convertidos": [df_hawks["FTM"].mean()]
        }

        stats_df = pd.DataFrame(stats)
        stats_df.to_csv(f"data/offensive_stats_{season}.csv", index=False)
        print(f"✅ Estatísticas ofensivas salvas em data/offensive_stats_{season}.csv")

    except Exception as e:
        print(f"❌ Erro ao gerar estatísticas ofensivas: {e}")

if __name__ == "__main__":
    generate_offensive_stats("2023-24")
    generate_offensive_stats("2024-25")
