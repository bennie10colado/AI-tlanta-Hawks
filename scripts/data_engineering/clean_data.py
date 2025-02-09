import pandas as pd

def clean_nba_data(season):
    """ Limpa e processa os dados da temporada fornecida. """
    df = pd.read_csv(f"data/games_{season}.csv")

    # Remover colunas irrelevantes
    df = df.drop(columns=["SEASON_ID", "GAME_STATUS_TEXT"], errors="ignore")

    # Converter datas para o formato correto
    df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])

    # Criar coluna de vitória/derrota
    df["WIN"] = df.apply(lambda x: 1 if x["WL"] == "W" else 0, axis=1)

    # Salvar dataset limpo
    df.to_csv(f"data/clean_games_{season}.csv", index=False)
    print(f"✅ Dados da temporada {season} limpos e salvos!")

clean_nba_data('2023-24')
clean_nba_data('2024-25')
