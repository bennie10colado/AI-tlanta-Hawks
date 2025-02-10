# RF3 - PROJ 2
import pandas as pd
import os

def filter_player_games(season="2024-25", opponent_team="LAL"):
    """ Filtra e exibe os jogos dos jogadores do Atlanta Hawks contra um time específico. """
    try:
        file_path = f"data/player_game_logs_{season}.csv"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Arquivo não encontrado: {file_path}")
        df = pd.read_csv(file_path)

        if "Adversário" not in df.columns:
            raise ValueError("❌ A coluna 'Adversário' não foi encontrada no dataset!")

        # Filtrar os jogos contra o adversário específico
        df_filtered = df[df["Adversário"] == opponent_team]

        # Verificar se existem jogos contra o time escolhido
        if df_filtered.empty:
            print(f"⚠ Nenhum jogo encontrado contra {opponent_team} na temporada {season}.")
            return

        # Criar diretório se não existir
        os.makedirs("data", exist_ok=True)

        filtered_file_path = f"data/player_game_logs_filtered_{season}.csv"
        df_filtered.to_csv(filtered_file_path, index=False)
        print(f"✅ Dados filtrados salvos em: {filtered_file_path}")
        print(df_filtered.head())

    except Exception as e:
        print(f"❌ Erro ao filtrar as estatísticas dos jogadores: {e}")

if __name__ == "__main__":
    # Exemplo: Filtrar contra o Los Angeles Lakers (LAL)
    filter_player_games(season="2024-25", opponent_team="LAL")
