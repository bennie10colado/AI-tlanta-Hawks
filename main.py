import time
import os
import logging
import streamlit as st  # Importando Streamlit corretamente
from scripts.visualization.teams.team_dashboard import start_dashboard  # Importando a função certa

from scripts.data_engineering.fetch_nba_teams import fetch_nba_teams
from scripts.data_engineering.fetch_nba_standings import fetch_nba_standings
from scripts.data_engineering.fetch_team_games import fetch_team_games
from scripts.data_engineering.clean_nba_data import clean_nba_data

from scripts.analysis.teams.analyze_team_performance import analyze_team_performance
from scripts.analysis.teams.offensive_stats import generate_offensive_stats
from scripts.analysis.teams.defensive_stats import generate_defensive_stats
from scripts.analysis.teams.games_summary import generate_games_summary

from scripts.visualization.teams.generate_team_charts import generate_team_charts

# ✅ Criar a pasta `logs/` antes de configurar o logging
os.makedirs("logs", exist_ok=True)

# ✅ Configurar logging corretamente
logging.basicConfig(filename="logs/errors.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def executar_modulo(nome, funcao):
    """Executa uma função de um módulo e captura erros"""
    print(f"\n🚀 Iniciando {nome}...\n")
    try:
        funcao()
        time.sleep(1)
    except Exception as e:
        print(f"⚠ Erro ao executar {nome}: {e}")
        logging.error(f"Erro ao executar {nome}: {e}")

if __name__ == "__main__":
    print("🎯 Iniciando Pipeline de Processamento da NBA...\n")

    # 🚀 1. Data Engineering
    executar_modulo("Coleta de Times da NBA (RF1)", fetch_nba_teams)
    executar_modulo("Coleta da Classificação Atual (RF2)", fetch_nba_standings)
    executar_modulo("Coleta de Jogos (RF7)", lambda: fetch_team_games(1610612737))
    executar_modulo("Limpeza de Dados", lambda: clean_nba_data("2023-24"))
    executar_modulo("Limpeza de Dados", lambda: clean_nba_data("2024-25"))


    # 🚀 2. Análise de Dados
    executar_modulo("Análise de Desempenho do Time (RF3)", lambda: analyze_team_performance("2023-24"))
    executar_modulo("Análise de Desempenho do Time (RF3)", lambda: analyze_team_performance("2024-25"))
    executar_modulo("Estatísticas Ofensivas (RF4, RF5)", generate_offensive_stats)
    executar_modulo("Estatísticas Defensivas (RF6)", generate_defensive_stats)
    executar_modulo("Resumo dos Jogos (RF7)", generate_games_summary)

    # 🚀 3. Geração de Gráficos
    executar_modulo("Geração de Gráficos do Time (RF8)", generate_team_charts)

    # 🚀 4. Inicializar Dashboard com Streamlit
    print("\n✅ Pipeline concluído com sucesso! 🎉")
    print("🖥 Iniciando o Dashboard...\n")

    os.system("streamlit run scripts/visualization/teams/team_dashboard.py")
