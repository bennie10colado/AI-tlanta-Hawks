# RF3 - PROJ 1
import pandas as pd
import os

def analyze_team_performance(season, team_name="Atlanta Hawks"):
    """Obtém estatísticas do time e salva em CSV."""
    file_path = f"data/clean_games_{season}.csv"
    output_path = f"data/team_stats_{season}.csv"

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

        df = pd.read_csv(file_path)

        # 🔍 Debug: Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

        # Garantir que as colunas essenciais estão no dataset
        colunas_necessarias = ["TEAM", "HOME_AWAY", "WIN"]
        colunas_faltando = [col for col in colunas_necessarias if col not in df.columns]

        if colunas_faltando:
            raise ValueError(f"🚨 O dataset não contém as colunas necessárias: {colunas_faltando}")

        # Filtrar apenas jogos do time desejado
        df_team = df[df["TEAM"].str.contains(team_name, case=False, na=False)]

        if df_team.empty:
            raise ValueError(f"🚨 Nenhum jogo encontrado para o time {team_name} na temporada {season}.")

        # Contagem de vitórias e derrotas
        total_vitorias = df_team["WIN"].sum()
        total_derrotas = len(df_team) - total_vitorias  # Evita contagem errada de jogos
        
        # Contagem de vitórias e derrotas separadas por casa e fora
        vitorias_casa = df_team[(df_team["WIN"] == 1) & (df_team["HOME_AWAY"].str.lower() == "home")].shape[0]
        vitorias_fora = df_team[(df_team["WIN"] == 1) & (df_team["HOME_AWAY"].str.lower() == "away")].shape[0]
        derrotas_casa = df_team[(df_team["WIN"] == 0) & (df_team["HOME_AWAY"].str.lower() == "home")].shape[0]
        derrotas_fora = df_team[(df_team["WIN"] == 0) & (df_team["HOME_AWAY"].str.lower() == "away")].shape[0]

        # Criar dicionário com estatísticas corrigidas
        stats = {
            #"Temporada": [season],
            #"Time": [team_name],
            "Total Jogos": [total_vitorias + total_derrotas],
            "Total Vitórias": [total_vitorias],
            "Vitórias Casa": [vitorias_casa],
            "Vitórias Fora": [vitorias_fora],
            "Total Derrotas": [total_derrotas],
            "Derrotas Casa": [derrotas_casa],
            "Derrotas Fora": [derrotas_fora]
        }

        # Criar DataFrame e salvar CSV
        stats_df = pd.DataFrame(stats)
        os.makedirs("data", exist_ok=True)  # Criar diretório caso não exista
        stats_df.to_csv(output_path, index=False)

        print(f"✅ Estatísticas do time {team_name} para {season} salvas em {output_path}!")
        print(stats_df)

    except Exception as e:
        print(f"❌ Erro ao processar estatísticas do time {team_name}: {e}")

if __name__ == "__main__":
    analyze_team_performance("2023-24")
    analyze_team_performance("2024-25")
