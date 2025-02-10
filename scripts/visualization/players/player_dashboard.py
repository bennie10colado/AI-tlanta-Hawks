# RF10 - PROJ 2
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

# Cache para evitar recarregamento repetitivo dos dados
@st.cache_data
def load_data(file_path):
    """Carrega dados do CSV de forma otimizada"""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def start_player_dashboard():
    """Inicializa o Dashboard de Estatísticas dos Jogadores do Atlanta Hawks"""
    st.set_page_config(page_title="NBA Dashboard - Jogadores do Atlanta Hawks", layout="wide")

    st.title("🏀 Dashboard - Estatísticas dos Jogadores do Atlanta Hawks")

    # 📂 Opção para selecionar temporada
    season = st.selectbox("📅 Selecione a Temporada:", ["2024-25"])

    # 📂 Caminhos dos arquivos de dados e gráficos
    image_dir = f"data/charts/{season}"
    player_file_path = f"data/player_stats.csv"
    game_logs_path = f"data/game_logs.csv"
    player_game_logs_path = f"data/player_game_logs_{season}.csv"
    player_career_comparison_path = f"data/player_career_comparison_{season}.csv"

    # 🚀 Criando abas de navegação
    tab1, tab2, tab3 = st.tabs(["📊 Estatísticas Individuais", "📈 Gráficos de Desempenho", "🏆 Comparação de Carreira"])

    # 📊 ABA 1 - Estatísticas dos Jogadores
    with tab1:
        st.subheader(f"📋 Estatísticas da Temporada {season}")

        # 📄 Carregar os CSVs de estatísticas individuais
        stats_files = {
            "Estatísticas Gerais dos Jogadores": player_file_path,
            "Logs de Jogos dos Jogadores": player_game_logs_path,
        }

        for title, file_path in stats_files.items():
            df = load_data(file_path)
            if df is not None:
                st.write(f"### {title}")
                st.dataframe(df, height=200)
            else:
                st.warning(f"⚠ Arquivo **{title}** não encontrado!")


        df = load_data(game_logs_path)
        # Sidebar para seleção do time adversário
        opponent_selected = st.selectbox("Escolha um time adversário:", ["Todos"] + sorted(df["Adversário"].unique()))

        # Filtrar os jogos do adversário escolhido
        if opponent_selected != "Todos":
            df_filtered = df[df["Adversário"] == opponent_selected]
        else:
            df_filtered = df

        # Contar jogos dentro e fora de casa
        home_away_counts = df_filtered["Casa/Fora"].value_counts()

        # Exibir tabela de resultados
        st.write("### 📊 Quantidade de Jogos Dentro e Fora de Casa RF4")
        st.write(df_filtered)

        # Criar gráfico de barras
        fig, ax = plt.subplots(figsize=(5, 3))
        home_away_counts.plot(kind="bar", color=["blue", "red"], ax=ax)
        ax.set_ylabel("Número de Jogos")
        ax.set_xlabel("Localização do Jogo")
        ax.set_title("Quantidade de Jogos Dentro e Fora de Casa")
        st.pyplot(fig, use_container_width=False)


    # 📈 ABA 2 - Gráficos de Desempenho dos Jogadores
    with tab2:
        st.subheader(f"📈 Gráficos de Desempenho - {season}")

        # Lista de gráficos com seus respectivos nomes e caminhos corrigidos
        charts = {
            "Distribuição de Pontos por Jogo (Média, Mediana e Moda)": f"{image_dir}/distribuicao_pontos.png",
            "Distribuição de Rebotes por Jogo (Média, Mediana e Moda)": f"{image_dir}/distribuicao_rebotes.png",
            "Distribuição de Assistências por Jogo (Média, Mediana e Moda)": f"{image_dir}/distribuicao_assistencias.png",
            "Box Plot - Pontos, Rebotes e Assistências por Jogo": f"{image_dir}/boxplot_stats.png"
        }

        for title, file_path in charts.items():
            if os.path.exists(file_path):
                st.image(file_path, caption=title)
            else:
                st.warning(f"⚠ {title} não encontrado!")

    # 🏆 ABA 3 - Comparação de Carreira
    with tab3:
        st.subheader("🏆 Comparação de Carreira vs Temporada Atual")

        df_career_comparison = load_data(player_career_comparison_path)

        if df_career_comparison is not None:
            st.write(f"### Comparação de Estatísticas de Carreira e Temporada Atual")
            st.dataframe(df_career_comparison, height=200)
        else:
            st.warning("⚠ Arquivo de comparação de carreira não encontrado!")

    st.write("📊 Os gráficos e estatísticas são gerados automaticamente e exibidos no dashboard.")

if __name__ == "__main__":
    start_player_dashboard()
