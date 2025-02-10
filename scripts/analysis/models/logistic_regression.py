import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, auc

def logistic_regression_analysis(season="2024-25"):
    """
    Modelo de Regressão Logística para prever se um jogador marcará acima da média em pontos, rebotes e assistências.
    """
    file_path = f"data/processed_player_game_logs_{season}.csv"
    output_path = f"data/logistic_regression_results_{season}.csv"
    plot_dir = f"data/proj3/logistic_regression_plots_{season}/"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    # Criar diretório para gráficos
    os.makedirs(plot_dir, exist_ok=True)

    # Definir variáveis independentes (X)
    X = df[["Minutos", "Tentativas de 3 PTS", "Cestas de 3 PTS"]]

    # Criar dicionário para salvar métricas de desempenho
    results_dict = {}

    for target in ["Pontos", "Rebotes", "Assistências"]:
        # Criar variável alvo binária (1 se acima da média, 0 se abaixo)
        y = (df[target] > df[target].mean()).astype(int)

        # Divisão entre treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Criar e treinar modelo de regressão logística
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Fazer previsões
        y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probabilidade da classe positiva (acima da média)
        y_pred = model.predict(X_test)

        # Criar matriz de confusão
        cm = confusion_matrix(y_test, y_pred)

        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["≤ Média", "> Média"], yticklabels=["≤ Média", "> Média"])
        plt.xlabel("Predito")
        plt.ylabel("Real")
        plt.title(f"Matriz de Confusão - {target}")
        plt.savefig(os.path.join(plot_dir, f"confusion_matrix_{target.lower()}.png"))
        plt.close()

        # Criar curva ROC e calcular AUC
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)

        plt.figure(figsize=(6, 5))
        plt.plot(fpr, tpr, color="blue", lw=2, label=f"AUC = {roc_auc:.2f}")
        plt.plot([0, 1], [0, 1], color="gray", linestyle="dashed")
        plt.xlabel("Falsos Positivos")
        plt.ylabel("Verdadeiros Positivos")
        plt.title(f"Curva ROC - {target}")
        plt.legend()
        plt.savefig(os.path.join(plot_dir, f"roc_curve_{target.lower()}.png"))
        plt.close()

        # Salvar coeficientes do modelo
        coef_df = pd.DataFrame({"Variável": X.columns, "Coeficiente": model.coef_[0]})
        coef_df.to_csv(os.path.join(plot_dir, f"coeficients_{target.lower()}.csv"), index=False)

        # Salvar métricas no dicionário
        results_dict[target] = {
            "Acurácia": model.score(X_test, y_test),
            "AUC": roc_auc
        }

    # Converter para DataFrame e salvar
    results_df = pd.DataFrame.from_dict(results_dict, orient="index")
    results_df.to_csv(output_path)

    print(f"✅ Análise de Regressão Logística concluída com sucesso!")
    print(f"📁 Resultados salvos em {output_path}")
    print(f"📊 Gráficos e coeficientes salvos em {plot_dir}")

if __name__ == "__main__":
    logistic_regression_analysis()
