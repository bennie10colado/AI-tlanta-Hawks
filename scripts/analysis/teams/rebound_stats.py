# RF5 - PROJ 1
import pandas as pd
import os

def generate_rebound_stats(season, team_name="Atlanta Hawks"):
    """Gera estatísticas de rebotes conforme a Tabela 4 do projeto."""
    file_path = f"data/clean_games_{season}.csv"
    output_path = f"data/rebound_stats_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # 🔍 Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Criar FG2M (Cestas de 2 Pontos) se não existir
        if "FGM" in df.columns and "FG3M" in df.columns and "FG2M" not in df.columns:
            df["FG2M"] = df["FGM"] - df["FG3M"]
            #print("⚠️ Coluna FG2M não encontrada no dataset. Foi gerada automaticamente como `FGM - FG3M`.")

        # Garantir que todas as colunas necessárias estejam no dataset
        required_columns = ["TEAM_NAME", "REB", "OREB", "DREB", "PTS", "FG2M", "FG3M", "FTM"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            raise ValueError(f"🚨 Colunas ausentes no dataset: {missing_columns}")

        # Filtrar jogos do time desejado
        df_team = df[df["TEAM_NAME"].str.contains(team_name, case=False, na=False)]

        if df_team.empty:
            raise ValueError(f"🚨 Nenhum jogo encontrado para o time {team_name} na temporada {season}.")

        # Calcular estatísticas de rebotes e divisão de pontos (RF5 - Tabela 4)
        stats = {
            "Total Rebotes": [df_team["REB"].sum()],
            "Total Rebotes Ofensivos": [df_team["OREB"].sum()],
            "Total Rebotes Defensivos": [df_team["DREB"].sum()],
            "Total Pontos": [df_team["PTS"].sum()],
            "Total Cestas de 2 Pontos": [df_team["FG2M"].sum()],
            "Total Cestas de 3 Pontos": [df_team["FG3M"].sum()],
            "Total Lances Livres": [df_team["FTM"].sum()]
        }

        stats_df = pd.DataFrame(stats)

        # Criar diretório e salvar CSV
        os.makedirs("data", exist_ok=True)
        stats_df.to_csv(output_path, index=False)

        print(f"✅ Estatísticas de rebotes e divisão de pontos salvas em {output_path}")
        print(stats_df)

    except Exception as e:
        print(f"❌ Erro ao gerar estatísticas de rebotes: {e}")

if __name__ == "__main__":
    generate_rebound_stats("2023-24")
    generate_rebound_stats("2024-25")
