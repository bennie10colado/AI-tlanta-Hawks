import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_player_charts(season="2024-25"):
    """Gera gráficos de desempenho dos jogadores do Atlanta Hawks na temporada, considerando todos os jogos."""
    
    logs_path = f"data/player_game_logs_{season}.csv"  # ✅ Usar dados brutos de cada jogo
    output_dir = f"data/charts/{season}"
    
    if not os.path.exists(logs_path):
        print(f"❌ Arquivo {logs_path} não encontrado.")
        return
    
    df = pd.read_csv(logs_path)

    # 🔍 Debug: Verificar colunas disponíveis
    print("📊 Colunas disponíveis no arquivo de logs:", df.columns.tolist())

    # ✅ Verificar se as colunas essenciais existem
    colunas_necessarias = ["Jogador", "Pontos", "Rebotes", "Assistências"]
    colunas_faltando = [col for col in colunas_necessarias if col not in df.columns]

    if colunas_faltando:
        raise ValueError(f"🚨 O dataset não contém as colunas necessárias: {colunas_faltando}")

    os.makedirs(output_dir, exist_ok=True)

    stats = ["Pontos", "Rebotes", "Assistências"]
    colors = {"Pontos": "blue", "Rebotes": "purple", "Assistências": "orange"}

    for stat in stats:
        plt.figure(figsize=(8, 5))

        # 🔹 Gráfico de Distribuição com dados reais de cada jogo
        sns.histplot(df[stat], kde=True, color=colors[stat])

        # ✅ Cálculo de Estatísticas
        mean_value = df[stat].mean()
        median_value = df[stat].median()
        mode_values = df[stat].mode().values  # Moda pode ter múltiplos valores
        
        # 🔹 Adicionar linhas de referência
        plt.axvline(mean_value, color='red', linestyle='dashed', label=f"Média ({mean_value:.1f})")
        plt.axvline(median_value, color='green', linestyle='dotted', label=f"Mediana ({median_value:.1f})")

        # 🔹 Adicionar todas as modas como linhas verticais
        for mode in mode_values:
            plt.axvline(mode, color='yellow', linestyle='dashdot', label=f"Moda ({mode:.1f})")

        # 📌 Configurações do gráfico
        plt.title(f"Distribuição de {stat} por Jogo - {season}")
        plt.xlabel(stat)
        plt.legend()
        
        # 💾 Salvar o gráfico
        plt.savefig(f"{output_dir}/distribuicao_{stat.lower()}.png")
        print(f"✅ Distribuição de {stat} salva em {output_dir}/distribuicao_{stat.lower()}.png")
        plt.close()

    # 🔹 Gráfico de Box Plot com dados individuais
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df[stats], palette=colors.values())

    # 📌 Configuração do Box Plot
    plt.title(f"Box Plot de Pontos, Rebotes e Assistências - {season}")
    plt.ylabel("Valores por Jogo")

    # 💾 Salvar Box Plot
    plt.savefig(f"{output_dir}/boxplot_stats.png")
    print(f"✅ Box Plot salvo em {output_dir}/boxplot_stats.png")
    plt.close()
    print(f"✅ Todos os gráficos gerados e salvos em '{output_dir}/'")

if __name__ == "__main__":
    generate_player_charts("2024-25")
