# RF8 - PROJ 1
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_team_charts(season, team_name="Atlanta Hawks"):
    """Gera gráficos de desempenho do time para compor o Dashboard do projeto."""
    
    stats_path = f"data/team_stats_{season}.csv"
    games_path = f"data/games_summary_{season}.csv"
    defense_path = f"data/defensive_stats_{season}.csv"

    if not os.path.exists(stats_path) or not os.path.exists(games_path):
        print(f"❌ Arquivos necessários não encontrados para {season}.")
        return

    df_stats = pd.read_csv(stats_path)
    df_games = pd.read_csv(games_path)
    df_defense = pd.read_csv(defense_path) if os.path.exists(defense_path) else None

    if df_defense is None:
        print(f"⚠ Arquivo de estatísticas defensivas não encontrado para {season}. Alguns gráficos podem não ser gerados.")
        
    print(f"📊 Colunas disponíveis em team_stats_{season}: {df_stats.columns.tolist()}")
    if df_defense is not None:
        print(f"📊 Colunas disponíveis em defensive_stats_{season}: {df_defense.columns.tolist()}")
    os.makedirs(f"data/charts/{season}", exist_ok=True)

    print(f"📊 Primeiras linhas de df_games:\n{df_games.head()}")
    print(f"📊 Tipo de sns.countplot: {type(sns.countplot)}")
    
    # 🔹 Gráfico 1: Barras Empilhadas - Vitórias e Derrotas
    plt.figure(figsize=(8, 5))
    plt.bar(["Total"], df_stats["Total Vitórias"], color="green", label="Vitórias")
    plt.bar(["Total"], df_stats["Total Derrotas"], color="red", bottom=df_stats["Total Vitórias"], label="Derrotas")
    plt.title(f"Vitórias e Derrotas - {season}")
    plt.legend()
    plt.savefig(f"data/charts/{season}/barras_empilhadas.png")
    plt.close()

    # 🔹 Gráfico 2: Barras Agrupadas - Casa/Fora (Correção do `hue`)
    labels = ["Vitórias Casa", "Vitórias Fora", "Derrotas Casa", "Derrotas Fora"]
    values = [
        df_stats["Vitórias Casa"].values[0], df_stats["Vitórias Fora"].values[0],
        df_stats["Derrotas Casa"].values[0], df_stats["Derrotas Fora"].values[0]
    ]
    colors = ["green", "blue", "red", "brown"]

    plt.figure(figsize=(8, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette=dict(zip(labels, colors)), legend=False)
    plt.title(f"Desempenho em Casa e Fora - {season}")
    plt.savefig(f"data/charts/{season}/barras_agrupadas.png")
    plt.close()

    # 🔹 Gráfico 3: Histograma de Vitórias e Derrotas
    plt.figure(figsize=(8, 5))
    sns.histplot(df_games["Vitória/Derrota"], bins=2, color="purple")
    plt.title(f"Frequência de Vitórias e Derrotas - {season}")
    plt.savefig(f"data/charts/{season}/histograma.png")
    plt.close()

    # 🔹 Gráfico 4: Pizza - Percentual de Vitórias/Derrotas Casa/Fora
    plt.figure(figsize=(8, 5))
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f"Distribuição de Vitórias e Derrotas - {season}")
    plt.savefig(f"data/charts/{season}/pizza.png")
    plt.close()

    # 🔹 Gráfico 5: Radar - Média de Roubos de Bola e Faltas por Jogo
    if df_defense is not None:
        labels = ["Roubos de Bola", "Faltas"]
        values = [df_defense["Roubos de Bola por Jogo"].values[0], df_defense["Faltas por Jogo"].values[0]]

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values, color='blue', alpha=0.25)
        ax.plot(angles, values, color='blue', linewidth=2)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        plt.title(f"Radar - Roubos e Faltas - {season}")
        plt.savefig(f"data/charts/{season}/radar.png")
        plt.close()

    # 🔹 Gráfico 6: Linhas - Sequência de Vitórias/Derrotas (Correção do `replace`)
    plt.figure(figsize=(10, 5))
    if "Vitória/Derrota" in df_games.columns:
        sns.lineplot(x=range(len(df_games)), y=df_games["Vitória/Derrota"], marker="o")
        plt.title(f"Sequência de Vitórias e Derrotas - {season}")
        plt.savefig(f"data/charts/{season}/linhas.png")
        plt.close()
    else:
        print("⚠ ERRO: Coluna 'Vitória/Derrota' não encontrada no dataset!")

    # 🔹 Gráfico 7: Dispersão - Média de Roubos de Bola x Erros por Jogo
    if df_defense is not None:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df_defense["Roubos de Bola por Jogo"], 
                        y=df_defense["Erros por Jogo"],
                        label="Atlanta Hawks", color="blue")
        plt.title(f"Roubos de Bola x Erros por Jogo - {season}")
        plt.savefig(f"data/charts/{season}/dispersao.png")
        plt.close()

    # 🔹 Gráfico 8: Simples para RF6 e RF7 (Vitórias e Derrotas por Local)
    plt.figure(figsize=(8, 5))
    if "Casa/Fora" in df_games.columns and "Vitória/Derrota" in df_games.columns:
        sns.countplot(x=df_games["Casa/Fora"], hue=df_games["Vitória/Derrota"], palette={"W": "green", "L": "red"})
        plt.title(f"Vitórias e Derrotas por Local - {season}")
        plt.savefig(f"data/charts/{season}/rf6_rf7.png")
        plt.close()
    else:
        print("⚠ ERRO: Coluna 'Casa/Fora' ou 'Vitória/Derrota' não encontrada no dataset!")

    print(f"✅ Todos os gráficos gerados para {season} e salvos em 'data/charts/{season}/'")

if __name__ == "__main__":
    os.makedirs("data/charts", exist_ok=True)
    generate_team_charts("2023-24")
    generate_team_charts("2024-25")
