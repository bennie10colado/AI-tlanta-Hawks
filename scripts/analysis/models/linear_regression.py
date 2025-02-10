import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def linear_regression_analysis(season="2024-25"):
    """
    Modelo de Regressão Linear para prever pontos, rebotes e assistências.
    """
    file_path = f"data/processed_player_game_logs_{season}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    X = df[["Minutos"]]
    y = df[["Pontos", "Rebotes", "Assistências"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    print(f"✅ Regressão Linear treinada! Coeficientes: {model.coef_}")

if __name__ == "__main__":
    linear_regression_analysis()
