# RF10 - PROJ 1
import streamlit as st
import pandas as pd
import os

# Cache para evitar recarregamento repetitivo dos dados
@st.cache_data
def load_data(file_path):
    """Carrega dados do CSV de forma otimizada"""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def start_dashboard():
    """Inicializa o Dashboard do Atlanta Hawks no Streamlit"""
    st.set_page_config(page_title="NBA Dashboard - Atlanta Hawks", layout="wide")

    st.title("🏀 Dashboard - Atlanta Hawks")

    # 📂 Opção para selecionar temporada
    season = st.selectbox("📅 Selecione a Temporada:", ["2023-24", "2024-25"])

    # 📂 Caminhos dos arquivos de dados e gráficos

    file_path = f"data/team_stats_{season}.csv"
    image_dir = f"data/graphs/{season}"
    player_file_path = f"data/player_stats.csv"

    # 🚀 Criando abas de navegação
    tab1, tab2, tab3 = st.tabs(["📊 Estatísticas", "📈 Gráficos", "Jogadores"])

    # 📊 ABA 1 - Estatísticas do Time
    with tab1:
        st.subheader(f"📋 Estatísticas da Temporada {season}")

        # 📄 Carregar os CSVs de estatísticas
        stats_files = {
            "Estatísticas Gerais": f"data/team_stats_{season}.csv",
            "Resumo de Jogos": f"data/games_summary_{season}.csv",
            "Estatísticas Defensivas": f"data/defensive_stats_{season}.csv"
        }

        for title, file_path in stats_files.items():
            df = load_data(file_path)
            if df is not None:
                st.write(f"### {title}")
                st.dataframe(df, height=200)
            else:
                st.warning(f"⚠ Arquivo **{title}** não encontrado!")

    # 📈 ABA 2 - Gráficos de Desempenho
    with tab2:
        st.subheader(f"📈 Gráficos de Desempenho - {season}")

        # Lista de gráficos com seus respectivos nomes e caminhos corrigidos
        charts = {
            "Vitórias x Derrotas (Empilhado)": f"{image_dir}/barras_empilhadas.png",
            "Desempenho Casa/Fora (Barras)": f"{image_dir}/barras_agrupadas.png",
            "Frequência de Vitórias e Derrotas (Histograma)": f"{image_dir}/histograma.png",
            "Distribuição de Vitórias e Derrotas (Pizza)": f"{image_dir}/pizza.png",
            "Radar - Roubos e Faltas": f"{image_dir}/radar.png",
            "Sequência de Vitórias e Derrotas (Linhas)": f"{image_dir}/linhas.png",
            "Roubos de Bola x Erros por Jogo (Dispersão)": f"{image_dir}/dispersao.png",
            "Vitórias e Derrotas por Local (RF6 e RF7)": f"{image_dir}/rf6_rf7.png"
        }

        for title, file_path in charts.items():
            if os.path.exists(file_path):
                st.image(file_path, caption=title)
            else:
                st.warning(f"⚠ {title} não encontrado!")

    st.write("📊 Os gráficos são gerados automaticamente e exibidos no dashboard.")

    # ABA 3 - Info dos jogadores
    with tab3:
        df_stats = load_data(player_file_path)

        if df_stats is not None:
            st.write(f"### info dos players")
            st.dataframe(df_stats, height=300)

if __name__ == "__main__":
    start_dashboard()
