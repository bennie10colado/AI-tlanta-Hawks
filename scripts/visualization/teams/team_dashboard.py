# RF9, RF10 - PROJ 1
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

    # 📂 Caminhos dos arquivos de dados e gráficos
    file_path = "data/team_stats_2023-24.csv"
    image_path = "data/vitorias_derrotas_2023-24.png"

    # 🚀 Criando abas de navegação
    tab1, tab2 = st.tabs(["📊 Estatísticas", "📈 Gráficos"])

    # 📊 ABA 1 - Estatísticas do Time
    with tab1:
        df_stats = load_data(file_path)

        if df_stats is not None:
            st.write("### 📋 Estatísticas da Temporada 2023-24")
            st.dataframe(df_stats, height=300)
        else:
            st.warning("⚠ Arquivo de estatísticas não encontrado! Execute a análise de desempenho primeiro.")

    # 📈 ABA 2 - Gráficos de Desempenho
    with tab2:
        if os.path.exists(image_path):
            st.image(image_path, caption="Vitórias e Derrotas do Atlanta Hawks")
        else:
            st.warning("⚠ Gráfico não encontrado! Execute a geração de gráficos antes de visualizar.")

    st.write("Os gráficos são gerados automaticamente e exibidos no dashboard.")

if __name__ == "__main__":
    start_dashboard()
