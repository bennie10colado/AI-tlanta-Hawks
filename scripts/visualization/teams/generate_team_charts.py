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
            plt.bar(categorias, valores, color=["green", "red"])
            plt.title(f"Vitórias e Derrotas - {season}")
            plt.ylabel("Quantidade")
            plt.savefig(f"{output_dir}/barras_empilhado.png")
            plt.close()

            ## ✅ 2. Gráfico de Barras Agrupado (Casa e Fora)
            plt.figure(figsize=(8, 6))
            valores_casa_fora = [df[col].sum() for col in colunas]
            plt.bar(colunas, valores_casa_fora, color=["green", "blue", "red", "brown"])
            plt.title(f"Vitórias e Derrotas (Casa/Fora) - {season}")
            plt.ylabel("Quantidade")
            plt.savefig(f"{output_dir}/barras_agrupado.png")
            plt.close()

            ## ✅ 3. Gráfico de Histograma
            plt.figure(figsize=(8, 6))
            plt.hist([total_vitorias, total_derrotas], bins=2, color=["green", "red"], alpha=0.7, label=["Vitórias", "Derrotas"])
            plt.title(f"Frequência de Vitórias e Derrotas - {season}")
            plt.xlabel("Quantidade")
            plt.ylabel("Frequência")
            plt.legend()
            plt.savefig(f"{output_dir}/histograma.png")
            plt.close()

            ## ✅ 4. Gráfico de Pizza
            labels = colunas
            values = [df[col].sum() for col in colunas]
            fig_pizza = px.pie(
                names=labels,
                values=values,
                title=f"Distribuição de Jogos - {season}",
                color=labels,
                color_discrete_map={
                    "Vitórias Casa": "green",
                    "Vitórias Fora": "blue",
                    "Derrotas Casa": "red",
                    "Derrotas Fora": "brown"
                }
            )
            fig_pizza.write_html(f"{output_dir}/pizza.html")

            ## ✅ 5. Gráfico de Radar (Pontos Casa/Fora)
            categorias = ["Vitórias Casa", "Derrotas Casa", "Vitórias Fora", "Derrotas Fora"]
            valores = [df["Vitórias Casa"].sum(), df["Derrotas Casa"].sum(), df["Vitórias Fora"].sum(), df["Derrotas Fora"].sum()]
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(r=valores, theta=categorias, fill="toself", name="Atlanta Hawks"))
            fig_radar.update_layout(title=f"Desempenho de Pontuação - {season}", polar=dict(radialaxis=dict(visible=True)))
            fig_radar.write_html(f"{output_dir}/radar.html")

            ## ✅ 6. Gráfico de Linhas (Sequência de Vitórias e Derrotas)
            df_games = pd.read_csv(f"data/games_summary_{season}.csv")
            df_games["Placar Atlanta Hawks"] = pd.to_numeric(df_games["Placar Atlanta Hawks"], errors="coerce")
            df_games["Placar Adversário"] = pd.to_numeric(df_games["Placar Adversário"], errors="coerce")
            df_games["Resultado"] = df_games["Placar Atlanta Hawks"] - df_games["Placar Adversário"]

            plt.figure(figsize=(10, 6))
            plt.plot(df_games["Data do Jogo"], df_games["Resultado"], marker="o", linestyle="-", color="blue", label="Diferença de Pontos")
            plt.axhline(y=0, color="red", linestyle="--", label="Empate")
            plt.xlabel("Data")
            plt.ylabel("Diferença de Pontos")
            plt.title(f"Sequência de Vitórias e Derrotas - {season}")
            plt.legend()
            plt.xticks(rotation=45)
            plt.savefig(f"{output_dir}/sequencia.png")
            plt.close()

            ## ✅ 7. Gráfico de Dispersão - Pontos Marcados vs. Sofridos
            fig_disp = px.scatter(
                df_games,
                x="Placar Atlanta Hawks",
                y="Placar Adversário",
                title=f"Pontos Marcados vs. Pontos Sofridos - {season}",
                labels={"Placar Atlanta Hawks": "Pontos Hawks", "Placar Adversário": "Pontos Adversário"},
                color_discrete_sequence=["blue"]
            )
            fig_disp.write_html(f"{output_dir}/dispersao.html")

            print(f"✅ Gráficos gerados e salvos para {season}!")

        except Exception as e:
            print(f"❌ Erro ao gerar gráficos para {season}: {e}")

if __name__ == "__main__":
    generate_team_charts()
