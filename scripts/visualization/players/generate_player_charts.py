# RF10 - PROJ 2
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_player_charts(season="2024-25"):
    """
    Generates statistical charts comparing current season and career performance.
    """
    input_path = f"data/player_career_comparison_{season}.csv"
    output_dir = f"data/charts/players/{season}"

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"❌ File not found: {input_path}")

    # Load data
    df = pd.read_csv(input_path)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # 🎯 Box Plot - Points, Assists, Rebounds
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[["Média Pontos (Atual)", "Média Assistências (Atual)", "Média Rebotes (Atual)"]])
    plt.title("Box Plot - Player Performance")
    plt.savefig(f"{output_dir}/boxplot_performance.png")
    plt.close()

    # 🎯 Histogram - Points Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Média Pontos (Atual)"], bins=10, kde=True, color="blue")
    plt.axvline(df["Média Pontos (Atual)"].mean(), color="red", linestyle="--", label="Média")
    plt.title("Distribution of Points per Game")
    plt.legend()
    plt.savefig(f"{output_dir}/histogram_points.png")
    plt.close()

    print(f"✅ Player charts saved in {output_dir}")

if __name__ == "__main__":
    generate_player_charts("2024-25")
