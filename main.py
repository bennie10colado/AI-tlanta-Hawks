import time
import os
import logging
import streamlit as st
from scripts.visualization.teams.team_dashboard import start_dashboard

# Importação dos módulos de engenharia de dados
from scripts.data_engineering.fetch_nba_teams import fetch_nba_teams
from scripts.data_engineering.fetch_nba_players import fetch_nba_players
from scripts.data_engineering.fetch_nba_standings import fetch_nba_standings
from scripts.data_engineering.fetch_team_games import fetch_team_games
from scripts.data_engineering.clean_nba_data import clean_nba_data

# Importação dos módulos de análise de dados
from scripts.analysis.teams.analyze_team_performance import analyze_team_performance
from scripts.analysis.teams.offensive_stats import generate_offensive_stats
from scripts.analysis.teams.rebound_stats import generate_rebound_stats
from scripts.analysis.teams.defensive_stats import generate_defensive_stats
from scripts.analysis.teams.games_summary import generate_games_summary

# Importação dos módulos de visualização
from scripts.visualization.teams.generate_team_charts import generate_team_charts

# Criar a pasta `logs/`
os.makedirs("logs", exist_ok=True)

# Configurar logging
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
    executar_modulo("Coleta de Jogadores do Atlanta (RF1, PT2)", fetch_nba_players)
    executar_modulo("Coleta da Classificação Atual (RF2)", fetch_nba_standings)
    executar_modulo("Coleta de Jogos (RF7)", lambda: fetch_team_games(1610612737))
    
    for season in ["2023-24", "2024-25"]:
        executar_modulo(f"Limpeza de Dados {season}", lambda: clean_nba_data(season))

    # 🚀 2. Análise de Dados
    for season in ["2023-24", "2024-25"]:
        executar_modulo(f"Análise de Desempenho do Time (RF3) - {season}", lambda: analyze_team_performance(season))
        executar_modulo(f"Estatísticas Ofensivas (RF4) - {season}", lambda: generate_offensive_stats(season))
        executar_modulo(f"Divisão de Estatísticas (RF5) - {season}", lambda: generate_rebound_stats(season))
        executar_modulo(f"Estatísticas Defensivas (RF6) - {season}", lambda: generate_defensive_stats(season))

    for season in ["2023-24", "2024-25"]:
        executar_modulo(f"Resumo dos Jogos (RF7) - {season}", lambda: generate_games_summary(season))

    # 🚀 3. Geração de Gráficos
    executar_modulo("Geração de Gráficos do Time (RF8)", generate_team_charts(season))

    # 🚀 4. Inicializar Dashboard com Streamlit
    print("\n✅ Pipeline concluído com sucesso! 🎉")
    print("🖥 Iniciando o Dashboard...\n")

    os.system("streamlit run scripts/visualization/teams/team_dashboard.py")
