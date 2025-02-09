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

def load_html(file_path):
    """Carrega e exibe arquivos HTML no Streamlit"""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
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

    # 🚀 Criando abas de navegação
    tab1, tab2 = st.tabs(["📊 Estatísticas", "📈 Gráficos"])

    # 📊 ABA 1 - Estatísticas do Time
    with tab1:
        df_stats = load_data(file_path)

        if df_stats is not None:
            st.write(f"### 📋 Estatísticas da Temporada {season}")
            st.dataframe(df_stats, height=300)
        else:
            st.warning(f"⚠ Arquivo de estatísticas para {season} não encontrado! Execute a análise de desempenho primeiro.")

    # 📈 ABA 2 - Gráficos de Desempenho
    with tab2:
        st.subheader(f"📈 Gráficos de Desempenho - {season}")

        # 📊 Gráfico 1: Barras Empilhadas para Vitórias e Derrotas
        empilhadas_path = f"{image_dir}/barras_empilhado.png"
        if os.path.exists(empilhadas_path):
            st.image(empilhadas_path, caption="Vitórias x Derrotas")
        else:
            st.warning("⚠ Gráfico de Vitórias x Derrotas não encontrado!")

        # 📊 Gráfico 2: Barras Agrupadas para Casa/Fora
        agrupadas_path = f"{image_dir}/barras_agrupado.png"
        if os.path.exists(agrupadas_path):
            st.image(agrupadas_path, caption="Desempenho em Casa e Fora")
        else:
            st.warning("⚠ Gráfico de Casa/Fora não encontrado!")

        # 📊 Gráfico 3: Histograma de Vitórias e Derrotas
        histograma_path = f"{image_dir}/histograma.png"
        if os.path.exists(histograma_path):
            st.image(histograma_path, caption="Frequência de Vitórias e Derrotas")
        else:
            st.warning("⚠ Gráfico de Frequência não encontrado!")

        # 🥧 Gráfico 4: Pizza - Percentual de Vitórias e Derrotas
        pizza_path = f"{image_dir}/pizza.html"
        pizza_html = load_html(pizza_path)
        if pizza_html:
            st.components.v1.html(pizza_html, height=500)
        else:
            st.warning("⚠ Gráfico de Pizza não encontrado!")

        # 📌 Gráfico 5: Radar - Pontuação Marcada e Sofrida
        radar_path = f"{image_dir}/radar.html"
        radar_html = load_html(radar_path)
        if radar_html:
            st.components.v1.html(radar_html, height=500)
        else:
            st.warning("⚠ Gráfico de Radar não encontrado!")

        # 📉 Gráfico 6: Linha - Sequência de Vitórias e Derrotas
        sequencia_path = f"{image_dir}/sequencia.png"
        if os.path.exists(sequencia_path):
            st.image(sequencia_path, caption="Sequência de Vitórias e Derrotas")
        else:
            st.warning("⚠ Gráfico de Sequência não encontrado!")

        # 🎯 Gráfico 7: Dispersão - Pontos Marcados e Sofridos
        dispersao_path = f"{image_dir}/dispersao.html"
        dispersao_html = load_html(dispersao_path)
        if dispersao_html:
            st.components.v1.html(dispersao_html, height=500)
        else:
            st.warning("⚠ Gráfico de Dispersão não encontrado!")

    st.write("📊 Os gráficos são gerados automaticamente e exibidos no dashboard.")

if __name__ == "__main__":
    start_dashboard()
