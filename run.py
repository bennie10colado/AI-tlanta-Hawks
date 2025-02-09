import os
import time

# Definir scripts em ordem de execução
SCRIPTS = {
    "Data Engineering": [
        "scripts/data_engineering/fetch_nba_teams.py",
        "scripts/data_engineering/fetch_nba_standings.py",
        "scripts/data_engineering/fetch_team_games.py",
        "scripts/data_engineering/clean_data.py"
    ],
    "Análise de Dados": [
        "scripts/analysis/teams/analyze_team_performance.py",
        "scripts/analysis/teams/offensive_stats.py",
        "scripts/analysis/teams/defensive_stats.py",
        "scripts/analysis/teams/games_summary.py"
    ],
    "Geração de Gráficos": [
        "scripts/visualization/teams/generate_team_charts.py"
    ],
    "Dashboard": [
        "scripts/visualization/teams/team_dashboard.py"
    ]
}

def executar_scripts(modulo):
    """Executa todos os scripts dentro de um módulo"""
    print(f"\n🚀 Iniciando {modulo}...\n")
    for script in SCRIPTS[modulo]:
        if os.path.exists(script):
            print(f"📌 Executando {script}...")
            os.system(f"python {script}")
            time.sleep(1)  # Pequeno delay para evitar sobrecarga
        else:
            print(f"⚠ Erro: Script {script} não encontrado!")

if __name__ == "__main__":
    print("🎯 Iniciando Pipeline de Processamento da NBA...\n")

    for modulo in SCRIPTS:
        executar_scripts(modulo)

    print("\n✅ Pipeline concluído com sucesso! 🎉")
    print("🖥 Iniciando o Dashboard...\n")
    os.system("streamlit run scripts/visualization/teams/team_dashboard.py")
