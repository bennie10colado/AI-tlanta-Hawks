import pandas as pd
import numpy as np
import os
from scipy import stats

def preprocess_data(season="2024-25"):
    """
    Pré-processa os dados dos jogadores para modelagem estatística e aprendizado de máquina.
    """
    file_path = f"data/player_game_logs_{season}.csv"
    output_path = f"data/processed_player_game_logs_{season}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Arquivo {file_path} não encontrado.")

    df = pd.read_csv(file_path)

    # Conversão de tempo de quadra para minutos decimais
    def convert_time_to_minutes(time_str):
        try:
            minutes, seconds = map(int, time_str.split(":"))
            return minutes + (seconds / 60)
        except:
            return np.nan

    df["Minutos"] = df["Tempo de Permanência do Jogador em Quadra"].astype(str).apply(convert_time_to_minutes)

    # Normalização de variáveis
    for col in ["Pontos", "Rebotes", "Assistências"]:
        df[col] = (df[col] - df[col].mean()) / df[col].std()

    # Tratamento de valores ausentes
    df.fillna(df.median(), inplace=True)

    os.makedirs("data", exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✅ Dados pré-processados salvos em {output_path}!")

if __name__ == "__main__":
    preprocess_data()
