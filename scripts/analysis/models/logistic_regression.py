import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def logistic_regression_analysis(season="2024-25"):
    """
    Modelo de Regressão Logística para prever desempenho acima ou abaixo da média.
    """
    file_path = f"data/processed_player_game_logs_{season}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    X = df[["Minutos"]]
    y = (df["Pontos"] > df["Pontos"].mean()).astype(int)

    model = LogisticRegression()
    model.fit(X, y)

    print(f"✅ Regressão Logística treinada! Score: {model.score(X, y)}")

if __name__ == "__main__":
    logistic_regression_analysis()
