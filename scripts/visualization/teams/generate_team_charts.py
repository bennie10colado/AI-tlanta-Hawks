# RF8 - PROJ 1
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_team_charts(season, team_name="Atlanta Hawks"):
    """Gera gráficos de desempenho do time para compor o Dashboard do projeto."""
    
    # Caminhos dos arquivos
    stats_path = f"data/team_stats_{season}.csv"
    games_path = f"data/games_summary_{season}.csv"

    # Verificar se os arquivos existem
    if not os.path.exists(stats_path) or not os.path.exists(games_path):
        print(f"❌ Arquivos necessários não encontrados para {season}.")
        return

    # Carregar os dados
    df_stats = pd.read_csv(stats_path)
    df_games = pd.read_csv(games_path)

    # 🔍 Verificar as colunas disponíveis
    print(f"📊 Colunas disponíveis em team_stats_{season}: {df_stats.columns.tolist()}")

    # 🔹 Gráfico 1: Barras Empilhadas - Vitórias e Derrotas
    plt.figure(figsize=(8, 5))
    plt.bar(["Total"], df_stats["Total Vitórias"], color="green", label="Vitórias")
    plt.bar(["Total"], df_stats["Total Derrotas"], color="red", bottom=df_stats["Total Vitórias"], label="Derrotas")
    plt.title(f"Vitórias e Derrotas - {season}")
    plt.legend()
    plt.savefig(f"data/charts/{season}_barras_empilhadas.png")
    plt.close()

    # 🔹 Gráfico 2: Barras Agrupadas - Casa/Fora
    labels = ["Vitórias Casa", "Vitórias Fora", "Derrotas Casa", "Derrotas Fora"]
    values = [
        df_stats["Vitórias Casa"].values[0], df_stats["Vitórias Fora"].values[0],
        df_stats["Derrotas Casa"].values[0], df_stats["Derrotas Fora"].values[0]
    ]
    colors = ["green", "blue", "red", "brown"]
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette=colors, legend=False)
    plt.title(f"Desempenho em Casa e Fora - {season}")
    plt.savefig(f"data/charts/{season}_barras_agrupadas.png")
    plt.close()

    # 🔹 Gráfico 3: Histograma de Vitórias e Derrotas
    plt.figure(figsize=(8, 5))
    sns.histplot(df_games["Vitória/Derrota"], bins=2, color="purple")
    plt.title(f"Frequência de Vitórias e Derrotas - {season}")
    plt.savefig(f"data/charts/{season}_histograma.png")
    plt.close()

    # 🔹 Gráfico 4: Pizza - Percentual de Vitórias/Derrotas Casa/Fora
    plt.figure(figsize=(8, 5))
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f"Distribuição de Vitórias e Derrotas - {season}")
    plt.savefig(f"data/charts/{season}_pizza.png")
    plt.close()

    # 🔹 Gráfico 5: Linhas - Sequência de Vitórias/Derrotas
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=range(len(df_games)), y=df_games["Vitória/Derrota"].map({"Vitória": 1, "Derrota": 0}), marker="o")
    plt.title(f"Sequência de Vitórias e Derrotas - {season}")
    plt.savefig(f"data/charts/{season}_linhas.png")
    plt.close()

    print(f"✅ Gráficos gerados para {season} e salvos em 'data/charts/'")

if __name__ == "__main__":
    os.makedirs("data/charts", exist_ok=True)
    generate_team_charts("2023-24")
    generate_team_charts("2024-25")
