# RF7 - PROJ 1
import pandas as pd
import os

def generate_games_summary(season, team_name="Atlanta Hawks"):
    """Gera o resumo dos jogos do time conforme a Tabela 6 do projeto."""
    file_path = f"data/clean_games_{season}.csv"
    output_path = f"data/games_summary_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Garantir que todas as colunas necessárias estejam no dataset
        required_columns = ["GAME_DATE", "OPPONENT", "WL", "HOME_AWAY", "PTS", "TEAM_NAME"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"🚨 Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do time desejado
        df_team = df[df["TEAM_NAME"].str.contains(team_name, case=False, na=False)].copy()  # ✅ Evita o `SettingWithCopyWarning`

        if df_team.empty:
            raise ValueError(f"🚨 Nenhum jogo encontrado para o time {team_name} na temporada {season}.")

        df_summary = df_team[["GAME_DATE", "OPPONENT", "WL", "HOME_AWAY", "PTS"]].copy()

        df_summary.rename(columns={
            "GAME_DATE": "Data do Jogo",
            "OPPONENT": "Adversário", #TODO: as vezes, o código invés de colocar somente o nome do time inimigo, ele coloca como "ATL vs. MIL, ATL vs. SAS..." invés de somente "MIL ou SAS"
            "WL": "Vitória/Derrota",
            "HOME_AWAY": "Casa/Fora",
            "PTS": "Placar"
        }, inplace=True)

        os.makedirs("data", exist_ok=True)
        df_summary.to_csv(output_path, index=False)

        print(f"✅ Resumo dos jogos salvo em {output_path}")
        print(df_summary.head())

    except Exception as e:
        print(f"❌ Erro ao gerar resumo dos jogos: {e}")

if __name__ == "__main__":
    generate_games_summary("2023-24")
    generate_games_summary("2024-25")
