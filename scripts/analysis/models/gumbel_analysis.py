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
    file_path = f"data/processed_player_game_logs_{season}.csv"
    output_path = f"data/gumbel_analysis_{season}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    def fit_gumbel(data):
        beta, mu = stats.gumbel_r.fit(data)
        return mu, beta

    results = []
    for stat in ["Pontos", "Rebotes", "Assistências"]:
        mu, beta = fit_gumbel(df[stat])

        for x in [10, 20, 30]:  # Valores de X para análise
            prob_acima = 1 - stats.gumbel_r.cdf(x, mu, beta)
            prob_abaixo = stats.gumbel_r.cdf(x, mu, beta)

            results.append([stat, x, prob_acima, prob_abaixo])

    df_results = pd.DataFrame(results, columns=["Estatística", "X", "Probabilidade Acima", "Probabilidade Abaixo"])

    os.makedirs("data", exist_ok=True)
    df_results.to_csv(output_path, index=False)

    print(f"✅ Análise de Gumbel salva em {output_path}!")

if __name__ == "__main__":
    gumbel_analysis()
