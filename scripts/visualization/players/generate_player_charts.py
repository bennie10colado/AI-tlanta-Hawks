import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_player_charts(season="2024-25"):
    """Gera gráficos de desempenho dos jogadores do Atlanta Hawks na temporada."""
    
    stats_path = f"data/player_statistics_{season}.csv"
    output_dir = f"data/charts/{season}"
    
    if not os.path.exists(stats_path):
        print(f"❌ Arquivo {stats_path} não encontrado.")
        return
    
    df = pd.read_csv(stats_path)

    # 🔍 Debug: Verificar colunas disponíveis
    print("📊 Colunas disponíveis em player_statistics:", df.columns.tolist())

    # Ajustar nome da coluna se necessário
    if "Jogador" not in df.columns:
        df.rename(columns={"Nome": "Jogador"}, inplace=True)

    # 🚨 Verificar se o DataFrame está vazio
    if df.empty:
        raise ValueError("🚨 O DataFrame carregado de player_statistics está vazio!")

    os.makedirs(output_dir, exist_ok=True)

    # 🔹 Gráfico 1: Distribuição de Pontos por Jogo
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Média Pontos"], kde=True, color="blue")
    plt.axvline(df["Média Pontos"].mean(), color='red', linestyle='dashed', label="Média")
    plt.axvline(df["Média Pontos"].median(), color='green', linestyle='dotted', label="Mediana")
    plt.title(f"Distribuição de Pontos por Jogo - {season}")
    plt.legend()
    plt.savefig(f"{output_dir}/distribuicao_pontos.png")
    print(f"✅ Distribuição de Pontos salva em {output_dir}/distribuicao_pontos.png")
    plt.close()

    # 🔹 Gráfico 2: Distribuição de Rebotes por Jogo
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Média Rebotes"], kde=True, color="purple")
    plt.axvline(df["Média Rebotes"].mean(), color='red', linestyle='dashed', label="Média")
    plt.axvline(df["Média Rebotes"].median(), color='green', linestyle='dotted', label="Mediana")
    plt.title(f"Distribuição de Rebotes por Jogo - {season}")
    plt.legend()
    plt.savefig(f"{output_dir}/distribuicao_rebotes.png")
    print(f"✅ Distribuição de Rebotes salva em {output_dir}/distribuicao_rebotes.png")
    plt.close()

    # 🔹 Gráfico 3: Distribuição de Assistências por Jogo
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Média Assistências"], kde=True, color="orange")
    plt.axvline(df["Média Assistências"].mean(), color='red', linestyle='dashed', label="Média")
    plt.axvline(df["Média Assistências"].median(), color='green', linestyle='dotted', label="Mediana")
    plt.title(f"Distribuição de Assistências por Jogo - {season}")
    plt.legend()
    plt.savefig(f"{output_dir}/distribuicao_assistencias.png")
    print(f"✅ Distribuição de Assistências salva em {output_dir}/distribuicao_assistencias.png")
    plt.close()

    # 🔹 Gráfico 4: Box Plot de Pontos, Rebotes e Assistências
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df[["Média Pontos", "Média Rebotes", "Média Assistências"]])
    plt.title(f"Box Plot de Pontos, Rebotes e Assistências - {season}")
    plt.savefig(f"{output_dir}/boxplot_stats.png")
    print(f"✅ Box Plot salvo em {output_dir}/boxplot_stats.png")
    plt.close()

    print(f"✅ Todos os gráficos gerados e salvos em '{output_dir}/'")

if __name__ == "__main__":
    generate_player_charts("2024-25")
