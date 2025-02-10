# RF8, RF9, RF10 - PROJ 1
import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go

def generate_team_charts():
    """Gera e salva os gráficos de desempenho da equipe para exibição no Streamlit."""
    for season in ["2023-24", "2024-25"]:
        file_path = f"data/team_stats_{season}.csv"
        output_dir = f"data/graphs/{season}"
        os.makedirs(output_dir, exist_ok=True)

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"🚨 O arquivo {file_path} não foi encontrado!")

            df = pd.read_csv(file_path)

            print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

            # Garantir que as colunas necessárias existem e são numéricas
            colunas = ["Vitórias Casa", "Vitórias Fora", "Derrotas Casa", "Derrotas Fora"]
            df[colunas] = df[colunas].apply(pd.to_numeric, errors="coerce").fillna(0)

            total_vitorias = df["Vitórias Casa"].sum() + df["Vitórias Fora"].sum()
            total_derrotas = df["Derrotas Casa"].sum() + df["Derrotas Fora"].sum()

            ## ✅ 1. Gráfico de Barras Empilhado (Vitórias x Derrotas)
            plt.figure(figsize=(8, 6))
            categorias = ["Vitórias", "Derrotas"]
            valores = [total_vitorias, total_derrotas]
            cores = ["green", "red"]
            plt.bar(categorias, valores, color=cores)
            plt.title(f"Vitórias e Derrotas - {season}")
            plt.ylabel("Quantidade")
            plt.savefig(f"{output_dir}/barras_empilhado.png", dpi=300, bbox_inches="tight")
            plt.close()

            ## ✅ 2. Gráfico de Barras Agrupado (Casa e Fora)
            plt.figure(figsize=(8, 6))
            valores_casa_fora = [df[col].sum() for col in colunas]
            plt.bar(colunas, valores_casa_fora, color=["green", "blue", "red", "brown"])
            plt.title(f"Vitórias e Derrotas (Casa/Fora) - {season}")
            plt.ylabel("Quantidade")
            plt.savefig(f"{output_dir}/barras_agrupado.png", dpi=300, bbox_inches="tight")
            plt.close()

            ## ✅ 3. Gráfico de Histograma
            plt.figure(figsize=(8, 6))
            plt.hist([total_vitorias, total_derrotas], bins=2, color=["green", "red"], alpha=0.7, label=["Vitórias", "Derrotas"])
            plt.title(f"Frequência de Vitórias e Derrotas - {season}")
            plt.xlabel("Quantidade")
            plt.ylabel("Frequência")
            plt.legend()
            plt.savefig(f"{output_dir}/histograma.png", dpi=300, bbox_inches="tight")
            plt.close()


        except Exception as e:
            print(f"❌ Erro ao gerar gráficos para {season}: {e}")

if __name__ == "__main__":
    generate_team_charts()
