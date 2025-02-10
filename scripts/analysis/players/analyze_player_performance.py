# RF5, RF6, RF7 e RF8 - PROJ 2
import pandas as pd
import os

def analyze_player_statistics(season="2024-25", opponent=None):
    """
    Analisa estatísticas individuais dos jogadores do Atlanta Hawks na temporada e salva em um novo CSV.
    Inclui RF5, RF6, RF7 e RF8 com a possibilidade de filtrar por adversário.
    """
    game_logs_path = f"data/player_game_logs_{season}.csv"
    output_path = f"data/player_statistics_{season}.csv"

    try:
        if not os.path.exists(game_logs_path):
            raise FileNotFoundError(f"O arquivo {game_logs_path} não foi encontrado.")

        df_games = pd.read_csv(game_logs_path)

        # 🔍 Verificar colunas disponíveis
        print(f"📊 Colunas disponíveis no dataset de jogos {season}: {df_games.columns.tolist()}")

        # Garantir que as colunas essenciais estão no dataset
        colunas_necessarias = ["Jogador", "Casa/Fora", "Adversário", "Pontos", "Rebotes", "Assistências"]
        colunas_faltando = [col for col in colunas_necessarias if col not in df_games.columns]

        if colunas_faltando:
            raise ValueError(f"🚨 O dataset não contém as colunas necessárias: {colunas_faltando}")

        # **Filtrar jogadores específicos do Atlanta Hawks**
        hawks_players = ["Trae Young", "Jalen Johnson", "Clint Capela"]
        df_team = df_games[df_games["Jogador"].isin(hawks_players)]

        if df_team.empty:
            raise ValueError(f"🚨 Nenhum dado de jogador encontrado para os jogadores do Hawks na temporada {season}.")

        # **Se um adversário for especificado, filtrar os jogos contra ele**
        if opponent:
            df_team = df_team[df_team["Adversário"].str.strip().str.lower() == opponent.strip().lower()]
            if df_team.empty:
                print(f"⚠ Nenhum jogo encontrado contra {opponent}.")
                return

        # ✅ **RF5 - Cálculo da média**
        media_pontos = df_team["Pontos"].mean()
        media_rebotes = df_team["Rebotes"].mean()
        media_assistencias = df_team["Assistências"].mean()

        # ✅ **RF5A - Porcentagem de partidas abaixo da média**
        pct_abaixo_media_pontos = (df_team["Pontos"] < media_pontos).mean() * 100
        pct_abaixo_media_rebotes = (df_team["Rebotes"] < media_rebotes).mean() * 100
        pct_abaixo_media_assistencias = (df_team["Assistências"] < media_assistencias).mean() * 100

        # ✅ **RF6 - Mediana**
        mediana_pontos = df_team["Pontos"].median()
        mediana_rebotes = df_team["Rebotes"].median()
        mediana_assistencias = df_team["Assistências"].median()

        # ✅ **RF6A - Porcentagem abaixo da mediana**
        pct_abaixo_mediana_pontos = (df_team["Pontos"] < mediana_pontos).mean() * 100
        pct_abaixo_mediana_rebotes = (df_team["Rebotes"] < mediana_rebotes).mean() * 100
        pct_abaixo_mediana_assistencias = (df_team["Assistências"] < mediana_assistencias).mean() * 100

        # ✅ **RF7 - Moda e frequência**
        moda_pontos = df_team["Pontos"].mode().values[0] if not df_team["Pontos"].mode().empty else "N/A"
        moda_rebotes = df_team["Rebotes"].mode().values[0] if not df_team["Rebotes"].mode().empty else "N/A"
        moda_assistencias = df_team["Assistências"].mode().values[0] if not df_team["Assistências"].mode().empty else "N/A"

        freq_moda_pontos = (df_team["Pontos"] == moda_pontos).sum()
        freq_moda_rebotes = (df_team["Rebotes"] == moda_rebotes).sum()
        freq_moda_assistencias = (df_team["Assistências"] == moda_assistencias).sum()

        # ✅ **RF7A - Porcentagem abaixo da moda**
        pct_abaixo_moda_pontos = (df_team["Pontos"] < moda_pontos).mean() * 100
        pct_abaixo_moda_rebotes = (df_team["Rebotes"] < moda_rebotes).mean() * 100
        pct_abaixo_moda_assistencias = (df_team["Assistências"] < moda_assistencias).mean() * 100

        # ✅ **RF8 - Cálculo do Desvio Padrão**
        desvio_pontos = df_team["Pontos"].std()
        desvio_rebotes = df_team["Rebotes"].std()
        desvio_assistencias = df_team["Assistências"].std()

        # Se o desvio padrão for NaN, substituir por 0
        desvio_pontos = 0 if pd.isna(desvio_pontos) else desvio_pontos
        desvio_rebotes = 0 if pd.isna(desvio_rebotes) else desvio_rebotes
        desvio_assistencias = 0 if pd.isna(desvio_assistencias) else desvio_assistencias

        stats = {
            "Temporada": [season],
            "Adversário": [opponent if opponent else "Todos"],
            "Total Jogos": [len(df_team)],
            "Média Pontos": [media_pontos],
            "Média Rebotes": [media_rebotes],
            "Média Assistências": [media_assistencias],
            "Pct. Abaixo Média Pontos": [pct_abaixo_media_pontos],
            "Pct. Abaixo Média Rebotes": [pct_abaixo_media_rebotes],
            "Pct. Abaixo Média Assistências": [pct_abaixo_media_assistencias],
            "Mediana Pontos": [mediana_pontos],
            "Mediana Rebotes": [mediana_rebotes],
            "Mediana Assistências": [mediana_assistencias],
            "Pct. Abaixo Mediana Pontos": [pct_abaixo_mediana_pontos],
            "Pct. Abaixo Mediana Rebotes": [pct_abaixo_mediana_rebotes],
            "Pct. Abaixo Mediana Assistências": [pct_abaixo_mediana_assistencias],
            "Moda Pontos": [moda_pontos],
            "Moda Rebotes": [moda_rebotes],
            "Moda Assistências": [moda_assistencias],
            "Freq. Moda Pontos": [freq_moda_pontos],
            "Freq. Moda Rebotes": [freq_moda_rebotes],
            "Freq. Moda Assistências": [freq_moda_assistencias],
            "Pct. Abaixo Moda Pontos": [pct_abaixo_moda_pontos],
            "Pct. Abaixo Moda Rebotes": [pct_abaixo_moda_rebotes],
            "Pct. Abaixo Moda Assistências": [pct_abaixo_moda_assistencias],
            "Desvio Padrão Pontos": [desvio_pontos],
            "Desvio Padrão Rebotes": [desvio_rebotes],
            "Desvio Padrão Assistências": [desvio_assistencias]
        }


        stats_df = pd.DataFrame(stats)
        os.makedirs("data", exist_ok=True)
        stats_df.to_csv(output_path, index=False)

        print(f"✅ Estatísticas dos jogadores do Hawks para {season} salvas em {output_path}!")
        print(stats_df)

    except Exception as e:
        print(f"❌ Erro ao processar estatísticas dos jogadores do Hawks: {e}")

if __name__ == "__main__":
    #analyze_player_statistics("2024-25")
    analyze_player_statistics("2024-25", opponent="LAL")
