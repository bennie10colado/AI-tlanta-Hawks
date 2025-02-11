import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pygam import PoissonGAM, LinearGAM

def gamlss_analysis(season="2024-25"):
    """
    Modelo GAMLSS para prever pontos, rebotes e assistências no próximo jogo.
    """
    file_path = f"data/processed_player_game_logs_{season}.csv"
    output_path = f"data/gamlss_results_{season}.csv"
    plot_dir = f"data/proj3/gamlss_plots_{season}/"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    # Criar diretório para gráficos
    os.makedirs(plot_dir, exist_ok=True)

    # Definir variáveis independentes (X) e dependentes (y)
    X = df[["Minutos", "Tentativas de 3 PTS", "Cestas de 3 PTS"]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    results_dict = {}

    for target in ["Pontos", "Rebotes", "Assistências"]:
        # Garantir que os valores de `y` sejam ≥ 0 e inteiros para o modelo Poisson
        y = df[target].clip(lower=0).to_numpy(dtype=np.int64)  # Corrigido para evitar FutureWarning

        # Criar modelos GAMLSS: PoissonGAM e LinearGAM
        gam_poisson = PoissonGAM().fit(X_scaled, y)
        gam_linear = LinearGAM().fit(X_scaled, y)

        # Fazer previsões para os dados de entrada
        predictions_poisson = gam_poisson.predict(X_scaled)
        predictions_linear = gam_linear.predict(X_scaled)

        # Calcular estatísticas de probabilidade
        stats_summary = {
            "mean": df[target].mean(),
            "median": df[target].median(),
            "mode": df[target].mode()[0],
            "max": df[target].max(),
            "min": df[target].min()
        }

        prob_results = []
        for stat_name, value in stats_summary.items():
            prob_above_poisson = (predictions_poisson > value).mean()
            prob_below_poisson = (predictions_poisson < value).mean()
            prob_exact_poisson = (predictions_poisson == value).mean()

            prob_above_linear = (predictions_linear > value).mean()
            prob_below_linear = (predictions_linear < value).mean()
            prob_exact_linear = (predictions_linear == value).mean()

            prob_results.append([target, stat_name, value, prob_above_poisson, prob_below_poisson, prob_exact_poisson,
                                 prob_above_linear, prob_below_linear, prob_exact_linear])

        # Criar DataFrame para os resultados
        prob_df = pd.DataFrame(prob_results, columns=[
            "Estatística", "Métrica", "Valor",
            "Probabilidade Acima (Poisson)", "Probabilidade Abaixo (Poisson)", "Probabilidade Exata (Poisson)",
            "Probabilidade Acima (Linear)", "Probabilidade Abaixo (Linear)", "Probabilidade Exata (Linear)"
        ])

        prob_df.to_csv(f"data/gamlss_probabilities_{target}_{season}.csv", index=False)

        # Criar gráficos de dispersão comparando valores reais e preditos
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=df[target], y=predictions_poisson, alpha=0.7, label="PoissonGAM")
        sns.scatterplot(x=df[target], y=predictions_linear, alpha=0.7, label="LinearGAM")
        plt.xlabel("Real")
        plt.ylabel("Predito")
        plt.title(f"Previsão com GAMLSS - {target}")
        plt.legend()
        plt.savefig(os.path.join(plot_dir, f"gamlss_{target.lower()}.png"))
        plt.close()

        # Salvar métricas no dicionário
        results_dict[target] = {
            "Poisson Mean Prediction": predictions_poisson.mean(),
            "Linear Mean Prediction": predictions_linear.mean()
        }

    # Converter para DataFrame e salvar
    results_df = pd.DataFrame.from_dict(results_dict, orient="index")
    results_df.to_csv(output_path)

    print(f"✅ Análise GAMLSS concluída com sucesso!")
    print(f"📁 Resultados salvos em {output_path}")
    print(f"📊 Gráficos e probabilidades salvos em {plot_dir}")

if __name__ == "__main__":
    gamlss_analysis()
