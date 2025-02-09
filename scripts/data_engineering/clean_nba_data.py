import pandas as pd
import os

def clean_nba_data(season):
    """ Limpa e processa os dados da temporada fornecida. """
    file_path = f"data/games_{season}.csv"
    clean_file_path = f"data/clean_games_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # Criar a coluna 'TEAM'
        df["TEAM"] = df["TEAM_NAME"]

        # Criar a coluna 'WIN' (1 = vitória, 0 = derrota)
        df["WIN"] = df["WL"].map({"W": 1, "L": 0})

        # Determinar se foi um jogo em casa ou fora
        df["HOME_AWAY"] = df["MATCHUP"].apply(lambda x: "Home" if "vs." in x else "Away")

        # Determinar o time da casa e o time visitante
        df["HOME_TEAM"] = df.apply(lambda row: row["TEAM_ABBREVIATION"] if row["HOME_AWAY"] == "Home" else row["MATCHUP"].split(" @ ")[-1], axis=1)
        df["AWAY_TEAM"] = df.apply(lambda row: row["TEAM_ABBREVIATION"] if row["HOME_AWAY"] == "Away" else row["MATCHUP"].split(" @ ")[0], axis=1)

        # Determinar o adversário
        df["OPPONENT"] = df.apply(lambda row: row["AWAY_TEAM"] if row["HOME_AWAY"] == "Home" else row["HOME_TEAM"], axis=1)

        # Criar a coluna de pontos do adversário (PTS_OPP)
        df_opponent = df[["GAME_ID", "TEAM_ABBREVIATION", "PTS"]].rename(columns={"TEAM_ABBREVIATION": "OPPONENT", "PTS": "PTS_OPP"})
        df = df.merge(df_opponent, on=["GAME_ID", "OPPONENT"], how="left")

        # Salvar os dados limpos
        df.to_csv(clean_file_path, index=False)
        print(f"✅ Dados da temporada {season} limpos e salvos em {clean_file_path}!")

    except Exception as e:
        print(f"❌ Erro ao limpar dados da temporada {season}: {e}")

if __name__ == "__main__":
    clean_nba_data("2023-24")
    clean_nba_data("2024-25")
