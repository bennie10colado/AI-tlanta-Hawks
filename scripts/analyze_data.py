import pandas as pd

# Carregar os dados
df = pd.read_csv("data/nba_hawks_stats.csv")

# Estatísticas básicas
print("🏀 Estatísticas do Atlanta Hawks - Temporada 2023-24")
print(f"Vitórias: {df['WINS'].values[0]}")
print(f"Derrotas: {df['LOSSES'].values[0]}")
print(f"Média de Pontos por Jogo: {df['PTS'].values[0]}")
print(f"Média de Assistências: {df['AST'].values[0]}")
print(f"Média de Rebotes: {df['REB'].values[0]}")
