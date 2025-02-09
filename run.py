import os

# Lista dos arquivos de saída esperados
csv_files = [
    "data/nba_teams.csv",
    "data/games_2023-24.csv",
    "data/games_2024-25.csv",
    "data/clean_games_2023-24.csv",
    "data/clean_games_2024-25.csv",
    "data/team_stats_2023-24.csv",
    "data/team_stats_2024-25.csv"
]

# Lista dos scripts a serem executados na ordem correta
scripts = [
    "fetch_nba_teams.py",
    "fetch_team_games.py",
    "clean_data.py",
    "analyze_data.py",
    "visualize_data.py"
]

# Criar a pasta "data" se não existir
os.makedirs("data", exist_ok=True)

print("🚀 Iniciando Pipeline de Dados da NBA...\n")

# Verificar se os arquivos CSV existem e executar os scripts na ordem
for script, csv_file in zip(scripts, csv_files):
    script_path = os.path.join("scripts", script)

    if os.path.exists(csv_file):
        print(f"🔄 Atualizando: {csv_file}...")
    else:
        print(f"🆕 Criando: {csv_file}...")

    print(f"📌 Executando {script}...")
    os.system(f"python {script_path}")

print("\n✅ Pipeline concluído com sucesso!")
