# RF3 - PROJ 2
import pandas as pd
import os
import streamlit as st
from tabulate import tabulate

def filter_player_games(season="2024-25", opponent_team=None):
    """ Filtra e exibe os jogos dos jogadores do Atlanta Hawks contra um time específico. """
    try:
        # Caminho do arquivo de estatísticas dos jogos
        file_path = f"data/player_game_logs_{season}.csv"

        # Verificar se o arquivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Arquivo não encontrado: {file_path}")

        # Carregar os dados do CSV
        df = pd.read_csv(file_path)

        # Garantir que a coluna 'Adversário' existe
        if "Adversário" not in df.columns:
            raise ValueError("❌ A coluna 'Adversário' não foi encontrada no dataset!")

        # Se nenhum adversário for passado, listar os disponíveis
        if opponent_team is None:
            teams = df["Adversário"].unique()
            print("📌 Times disponíveis para filtrar:", teams)
            return teams

        # Filtrar os jogos contra o adversário específico
        df_filtered = df[df["Adversário"] == opponent_team]

        # Verificar se existem jogos contra o time escolhido
        if df_filtered.empty:
            print(f"⚠ Nenhum jogo encontrado contra {opponent_team} na temporada {season}.")
            return None

        # Criar diretório se não existir
        os.makedirs("data", exist_ok=True)

        # Caminho do arquivo filtrado
        filtered_file_path = f"data/player_game_logs_filtered_{season}_{opponent_team}.csv"

        # Salvar os dados filtrados em um novo arquivo CSV
        df_filtered.to_csv(filtered_file_path, index=False)

        # Exibir os dados filtrados no terminal (formato tabela)
        print(f"✅ Dados filtrados contra {opponent_team} salvos em: {filtered_file_path}")
        print(tabulate(df_filtered, headers="keys", tablefmt="pretty"))

        return df_filtered

    except Exception as e:
        print(f"❌ Erro ao filtrar as estatísticas dos jogadores: {e}")
        return None

# Interface Streamlit para visualização
def filter_player_games_streamlit():
    """ Interface interativa para seleção de partidas contra times específicos """
    st.title("📊 Estatísticas de Jogos Específicos")

    # Selecionar a temporada
    season = st.selectbox("📅 Selecione a Temporada:", ["2024-25", "2023-24"])

    # Buscar times disponíveis
    available_teams = filter_player_games(season)

    # Criar selectbox para o usuário escolher o adversário
    opponent_team = st.selectbox("🆚 Selecione o time adversário:", available_teams)

    # Exibir dados filtrados
    if opponent_team:
        df_filtered = filter_player_games(season, opponent_team)

        if df_filtered is not None:
            st.write(f"📊 Estatísticas contra o {opponent_team}:")
            st.dataframe(df_filtered)

if __name__ == "__main__":
    filter_player_games(season="2024-25", opponent_team="LAL")

