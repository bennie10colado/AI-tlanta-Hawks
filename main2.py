import time
import os
import logging
import streamlit as st
from scripts.visualization.players.player_dashboard import start_player_dashboard

# Importação dos módulos de engenharia de dados
from scripts.data_engineering.fetch_nba_players import fetch_nba_players
from scripts.data_engineering.fetch_player_game_logs import fetch_player_game_logs
from scripts.data_engineering.fetch_game_logs import load_game_logs

# Importação dos módulos de análise de dados
from scripts.analysis.players.analyze_player_performance import analyze_player_statistics
from scripts.analysis.players.analyze_player_career import fetch_player_career_stats
from scripts.data_engineering.filter_player_games import filter_player_games

# Importação dos módulos de visualização
from scripts.visualization.players.generate_player_charts import generate_player_charts

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/errors.log", 
    level=logging.ERROR, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def executar_modulo(nome, funcao):
    """Executa uma função de um módulo e captura erros"""
    print(f"\n🚀 Iniciando {nome}...\n")
    try:
        funcao()
        time.sleep(1)
        print(f"✅ {nome} concluído com sucesso!\n")
    except Exception as e:
        print(f"⚠ Erro ao executar {nome}: {e}")
        logging.error(f"Erro ao executar {nome}: {e}")

if __name__ == "__main__":
    print("🎯 Iniciando Pipeline de Processamento dos Jogadores da NBA...\n")

    # 🚀 1. Data Engineering
    executar_modulo("Coleta de Jogadores do Atlanta Hawks (RF1)", fetch_nba_players)
    executar_modulo("Coleta de Estatísticas de Jogos dos Jogadores (RF2)", fetch_player_game_logs)

    # 🚀 2. Análise de Dados
    executar_modulo("Filtragem de Jogos Específicos (RF3)", lambda: filter_player_games(season="2024-25"))

    executar_modulo("Jogos dentro e fora de casa (RF4)", lambda: load_game_logs(season="2024-25"))

    executar_modulo("Análise Estatística dos Jogadores (RF5 - RF8)", lambda: analyze_player_statistics(season="2024-25"))
    executar_modulo("Comparação de Estatísticas de Carreira (RF9, RF10)", lambda: fetch_player_career_stats(season="2024-25"))

    # 🚀 3. Geração de Gráficos
    executar_modulo("Geração de Gráficos de Desempenho dos Jogadores (RF10)", lambda: generate_player_charts(season="2024-25"))

    # 🚀 4. Inicializar Dashboard com Streamlit
    print("\n✅ Pipeline concluído com sucesso! 🎉")
    print("🖥 Iniciando o Dashboard...\n")

    os.system("streamlit run scripts/visualization/players/player_dashboard.py")
