import pandas as pd
import numpy as np
import os
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def gumbel_analysis(season="2024-25"):
    """
    Modelagem estatística com distribuição de Gumbel para eventos extremos.
    """
    file_path = f"data/player_game_logs_{season}.csv"
    output_path = f"data/gumbel_analysis_{season}.csv"
    plot_dir = f"data/proj3/gumbel_plots_{season}/"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    os.makedirs(plot_dir, exist_ok=True)

    def fit_gumbel(data):
        beta, mu = stats.gumbel_r.fit(data)
        return mu, beta

    results = []
    for stat in ["Pontos", "Rebotes", "Assistências"]:
        mu, beta = fit_gumbel(df[stat])

        for x in [10, 20, 30]:  # Valores de X para análise
            prob_acima = 1 - stats.gumbel_r.cdf(x, mu, beta)
            prob_abaixo = stats.gumbel_r.cdf(x, mu, beta)
            prob_exato = stats.gumbel_r.pdf(x, mu, beta)

            results.append([stat, x, prob_acima, prob_abaixo, prob_exato])

        # Criar gráficos da distribuição ajustada
        x_vals = np.linspace(df[stat].min(), df[stat].max(), 1000)
        pdf_vals = stats.gumbel_r.pdf(x_vals, mu, beta)

        plt.figure(figsize=(8, 5))
        sns.histplot(df[stat], bins=20, kde=True, stat="density", label="Dados reais")
        plt.plot(x_vals, pdf_vals, label="Ajuste Gumbel", color="red", linestyle="dashed")
        plt.xlabel(stat)
        plt.ylabel("Densidade")
        plt.title(f"Distribuição de Gumbel - {stat}")
        plt.legend()

        # Salvar gráfico
        plt.savefig(os.path.join(plot_dir, f"gumbel_{stat.lower()}.png"))
        plt.close()

    df_results = pd.DataFrame(results, columns=["Estatística", "X", "Probabilidade Acima", "Probabilidade Abaixo", "Probabilidade Exata"])

    os.makedirs("data", exist_ok=True)
    df_results.to_csv(output_path, index=False)

    print(f"✅ Análise de Gumbel salva em {output_path}!")
    print(f"📊 Gráficos salvos em {plot_dir}")

if __name__ == "__main__":
    gumbel_analysis()
