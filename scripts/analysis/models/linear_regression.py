import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, mean_squared_error, r2_score

def linear_regression_analysis(season="2024-25"):
    """
    Modelo de Regressão Linear para prever pontos, rebotes e assistências.
    """
    file_path = f"data/processed_player_game_logs_{season}.csv"
    output_path = f"data/linear_regression_results_{season}.csv"
    prob_output_path = f"data/probabilities_{season}.csv"
    plot_dir = f"data/proj3/linear_regression_plots_{season}/"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    # Criar diretório para gráficos
    os.makedirs(plot_dir, exist_ok=True)

    # Definir variáveis independentes (X) e dependentes (y)
    X = df[["Minutos", "Tentativas de 3 PTS", "Cestas de 3 PTS"]]
    y = df[["Pontos", "Rebotes", "Assistências"]]

    # Calcular estatísticas para cada variável dependente
    stats_summary = {}
    for col in y.columns:
        stats_summary[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "mode": df[col].mode()[0],  # Pegando a primeira moda encontrada
            "max": df[col].max(),
            "min": df[col].min()
        }

    # Divisão entre treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar e treinar modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fazer previsões
    y_pred = model.predict(X_test)

    # Criar dataframe de resultados
    results = pd.DataFrame({
        "Real_Pontos": y_test["Pontos"].values,
        "Predito_Pontos": y_pred[:, 0],
        "Real_Rebotes": y_test["Rebotes"].values,
        "Predito_Rebotes": y_pred[:, 1],
        "Real_Assistências": y_test["Assistências"].values,
        "Predito_Assistências": y_pred[:, 2]
    })

    # Cálculo de probabilidades acima/abaixo das estatísticas
    prob_results = []
    for col in y.columns:
        for stat_name, value in stats_summary[col].items():
            prob_acima = (results[f"Real_{col}"] > value).mean()
            prob_abaixo = (results[f"Real_{col}"] < value).mean()

            prob_results.append([col, stat_name, value, prob_acima, prob_abaixo])

    prob_df = pd.DataFrame(prob_results, columns=["Estatística", "Métrica", "Valor", "Probabilidade Acima", "Probabilidade Abaixo"])

    # Salvar resultados
    results.to_csv(output_path, index=False)
    prob_df.to_csv(prob_output_path, index=False)

    # Criar matriz de confusão binária para cada estatística
    for col in y.columns:
        threshold = stats_summary[col]["mean"]  # Definir a média como ponto de corte
        y_real_binary = (results[f"Real_{col}"] > threshold).astype(int)
        y_pred_binary = (results[f"Predito_{col}"] > threshold).astype(int)

        cm = confusion_matrix(y_real_binary, y_pred_binary)

        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["≤ Média", "> Média"], yticklabels=["≤ Média", "> Média"])
        plt.xlabel("Predito")
        plt.ylabel("Real")
        plt.title(f"Matriz de Confusão - {col}")

        plt.savefig(os.path.join(plot_dir, f"confusion_matrix_{col.lower()}.png"))
        plt.close()

    print(f"✅ Análise de Regressão Linear concluída com sucesso!")
    print(f"📁 Resultados salvos em {output_path}")
    print(f"📊 Probabilidades salvas em {prob_output_path}")
    print(f"🖼 Gráficos salvos em {plot_dir}")

if __name__ == "__main__":
    linear_regression_analysis()
