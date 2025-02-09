# RF8 - PROJ 1
import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_team_charts():
    for season in ["2023-24", "2024-25"]:
        file_path = f"data/team_stats_{season}.csv"
        output_path = f"data/vitorias_derrotas_{season}.png"

        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

            df = pd.read_csv(file_path)

            # 🔍 Debug: Verificar colunas disponíveis
            print(f"📊 Colunas disponíveis no dataset {season}: {df.columns.tolist()}")

            # Garantir que as colunas necessárias existem e são numéricas
            colunas = ["Vitórias Casa", "Vitórias Fora", "Derrotas Casa", "Derrotas Fora"]

            if not all(col in df.columns for col in colunas):
                raise ValueError(f"🚨 As colunas necessárias não estão no arquivo: {colunas}")
            
            # Converter valores para numérico e preencher NaN com 0
            df[colunas] = df[colunas].apply(pd.to_numeric, errors="coerce").fillna(0)

            # Verificar se o DataFrame tem pelo menos uma linha válida
            if df.empty or df[colunas].sum().sum() == 0:
                raise ValueError(f"🚨 Os dados da temporada {season} estão inválidos ou não contêm estatísticas de vitórias e derrotas.")

            # Criar pasta se não existir
            os.makedirs("data", exist_ok=True)

            # Criar gráfico de vitórias e derrotas
            plt.figure(figsize=(8, 6))
            valores = [df[col].iloc[0] for col in colunas]  # Pega os valores da primeira linha do CSV
            plt.bar(colunas, valores, color=["green", "blue", "red", "brown"])
            plt.title(f"Vitórias e Derrotas do Atlanta Hawks - Temporada {season}")
            plt.ylabel("Quantidade")
            plt.savefig(output_path)
            plt.show()
            
            print(f"✅ Gráfico gerado e salvo em {output_path}!")

        except Exception as e:
            print(f"❌ Erro ao gerar gráficos do time para {season}: {e}")

if __name__ == "__main__":
    generate_team_charts()
