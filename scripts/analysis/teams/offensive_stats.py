# RF4 - PROJ 1
import pandas as pd
import os

def generate_offensive_stats(season, team_name="Atlanta Hawks"):
    """Gera estatísticas ofensivas conforme a Tabela 3 do projeto."""
    file_path = f"data/clean_games_{season}.csv"
    output_path = f"data/offensive_stats_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # 🔍 Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Criar FG2M (cestas de 2 pontos) se não existir
        if "FG2M" not in df.columns and "FGM" in df.columns and "FG3M" in df.columns:
            df["FG2M"] = df["FGM"] - df["FG3M"]

        # Garantir que todas as colunas necessárias estejam no dataset
        required_columns = ["TEAM_NAME", "PTS", "AST", "REB", "FG3M", "FG2M", "FTM", "HOME_AWAY", "WIN"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"🚨 Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do time desejado
        df_team = df[df["TEAM_NAME"].str.contains(team_name, case=False, na=False)]

        if df_team.empty:
            raise ValueError(f"🚨 Nenhum jogo encontrado para o time {team_name} na temporada {season}.")

        # Calcular estatísticas ofensivas (RF4 - Tabela 3)
        stats = {
            #"Temporada": [season],
            #"Time": [team_name],
            "Total Jogos": [len(df_team)],
            "Total Pontos": [df_team["PTS"].sum()],
            "Total Assistências": [df_team["AST"].sum()],
            "Total Rebotes": [df_team["REB"].sum()],
            "Total Cestas de 3 Pontos": [df_team["FG3M"].sum()],
            "Derrotas em Casa": [df_team[(df_team["WIN"] == 0) & (df_team["HOME_AWAY"].str.lower() == "home")].shape[0]],
            "Derrotas Fora de Casa": [df_team[(df_team["WIN"] == 0) & (df_team["HOME_AWAY"].str.lower() == "away")].shape[0]]
        }

        stats_df = pd.DataFrame(stats)

        # Criar diretório e salvar CSV
        os.makedirs("data", exist_ok=True)
        stats_df.to_csv(output_path, index=False)

        print(f"✅ Estatísticas ofensivas salvas em {output_path}")
        print(stats_df)

    except Exception as e:
        print(f"❌ Erro ao gerar estatísticas ofensivas: {e}")

if __name__ == "__main__":
    generate_offensive_stats("2023-24")
    generate_offensive_stats("2024-25")
