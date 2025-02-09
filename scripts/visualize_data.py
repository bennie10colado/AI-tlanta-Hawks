import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("data/nba_hawks_stats.csv")

# Criar um gráfico de barras para vitórias e derrotas
plt.figure(figsize=(6,4))
plt.bar(["Vitórias", "Derrotas"], [df["WINS"].values[0], df["LOSSES"].values[0]], color=["green", "red"])
plt.title("Desempenho do Atlanta Hawks - Temporada 2023-24")
plt.ylabel("Quantidade")
plt.show()
