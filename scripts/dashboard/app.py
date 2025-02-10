import streamlit as st
import pandas as pd
import os

# Cache para evitar recarregamento desnecessário dos dados
@st.cache_data
def load_data(file_path):
    """Carrega dados do CSV de forma otimizada"""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

def start_dashboard():
    """Inicializa o Dashboard Interativo no Streamlit"""
    st.set_page_config(page_title="NBA Analytics Dashboard", layout="wide")

    st.title("🏀 NBA Analytics Dashboard - Projeto 3")

    # 📂 Opção para selecionar temporada
    season = st.selectbox("📅 Selecione a Temporada:", ["2023-24", "2024-25"])

    # 📂 Diretórios de dados e imagens
    image_dir = f"data/charts/{season}"
    proj3_dir = f"data/proj3/"
    stats_dir = f"data/"
    models_dir = f"data/"

    # 🚀 Criando abas de navegação
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📊 Estatísticas", "📈 Gráficos", "🤖 Modelos Preditivos", "📌 Probabilidades", "📊 Comparações Avançadas"]
    )

    # 📊 ABA 1 - Estatísticas Gerais
    with tab1:
        st.subheader(f"📋 Estatísticas da Temporada {season}")

        stats_files = {
            "Estatísticas do Time": f"{stats_dir}/team_stats_{season}.csv",
            "Resumo de Jogos": f"{stats_dir}/games_summary_{season}.csv",
            "Estatísticas Defensivas": f"{stats_dir}/defensive_stats_{season}.csv"
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
        st.subheader(f"📊 Gráficos de Desempenho - {season}")

        charts = {
            "Vitórias x Derrotas (Empilhado)": f"{image_dir}/barras_empilhadas.png",
            "Desempenho Casa/Fora (Barras)": f"{image_dir}/barras_agrupadas.png",
            "Distribuição de Vitórias e Derrotas (Pizza)": f"{image_dir}/pizza.png",
            "Histograma de Desempenho": f"{image_dir}/histograma.png",
            "Radar - Roubos e Faltas": f"{image_dir}/radar.png",
            "Sequência de Vitórias e Derrotas (Linhas)": f"{image_dir}/linhas.png",
            "Dispersão: Roubos de Bola x Erros por Jogo": f"{image_dir}/dispersao.png"
        }

        for title, file_path in charts.items():
            if os.path.exists(file_path):
                st.image(file_path, caption=title)
            else:
                st.warning(f"⚠ {title} não encontrado!")

    # 📌 ABA 3 - Modelos Estatísticos e Machine Learning
    with tab3:
        st.subheader("📈 Modelos Estatísticos e Machine Learning")

        models = {
            "Gumbel - Análise de Eventos Extremos": f"{models_dir}/gumbel_analysis_{season}.csv",
            "Regressão Linear - Previsão de Estatísticas": f"{models_dir}/linear_regression_results_{season}.csv",
            "Regressão Logística - Classificação": f"{models_dir}/logistic_regression_results_{season}.csv",
            "GAMLSS - Modelagem Avançada": f"{models_dir}/gamlss_results_{season}.csv"
        }

        for title, file_path in models.items():
            df = load_data(file_path)
            if df is not None:
                st.write(f"### {title}")
                st.dataframe(df, height=200)
            else:
                st.warning(f"⚠ Arquivo **{title}** não encontrado!")

    # 🎯 ABA 4 - Probabilidades de Ocorrência
    with tab4:
        st.subheader("📌 Probabilidades de Ocorrência")

        prob_files = {
            "Probabilidades - Gumbel": f"{models_dir}/gumbel_analysis_{season}.csv",
            "Probabilidades - Reg. Logística": f"{models_dir}/probabilities_{season}.csv",
            "Probabilidades - GAMLSS": f"{models_dir}/gamlss_probabilities_Pontos_{season}.csv"
        }

        for title, file_path in prob_files.items():
            df = load_data(file_path)
            if df is not None:
                st.write(f"### {title}")
                st.dataframe(df, height=200)
            else:
                st.warning(f"⚠ Arquivo **{title}** não encontrado!")

    # 📊 ABA 5 - Comparações Avançadas (Gráficos do Projeto 3)
    with tab5:
        st.subheader("📊 Comparações Avançadas - Modelos Estatísticos")

        proj3_charts = {
            "Gumbel - Pontos": f"{proj3_dir}/gumbel_plots_{season}/gumbel_pontos.png",
            "Gumbel - Assistências": f"{proj3_dir}/gumbel_plots_{season}/gumbel_assistências.png",
            "Gumbel - Rebotes": f"{proj3_dir}/gumbel_plots_{season}/gumbel_rebotes.png",
            "Regressão Linear - Pontos": f"{proj3_dir}/linear_regression_plots_{season}/regression_pontos.png",
            "Regressão Linear - Assistências": f"{proj3_dir}/linear_regression_plots_{season}/regression_assistências.png",
            "Regressão Linear - Rebotes": f"{proj3_dir}/linear_regression_plots_{season}/regression_rebotes.png",
            "Regressão Logística - Curva ROC Pontos": f"{proj3_dir}/logistic_regression_plots_{season}/roc_curve_pontos.png",
            "Regressão Logística - Curva ROC Assistências": f"{proj3_dir}/logistic_regression_plots_{season}/roc_curve_assistências.png",
            "Regressão Logística - Curva ROC Rebotes": f"{proj3_dir}/logistic_regression_plots_{season}/roc_curve_rebotes.png",
            "GAMLSS - Pontos": f"{proj3_dir}/gamlss_plots_{season}/gamlss_pontos.png",
            "GAMLSS - Assistências": f"{proj3_dir}/gamlss_plots_{season}/gamlss_assistências.png",
            "GAMLSS - Rebotes": f"{proj3_dir}/gamlss_plots_{season}/gamlss_rebotes.png"
        }

        for title, file_path in proj3_charts.items():
            if os.path.exists(file_path):
                st.image(file_path, caption=title)
            else:
                st.warning(f"⚠ {title} não encontrado!")

if __name__ == "__main__":
    start_dashboard()
