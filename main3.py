import time
import os
import logging
from scripts.data_engineering.preprocess_data import preprocess_data
from scripts.analysis.models.gumbel_analysis import gumbel_analysis
from scripts.analysis.models.linear_regression import linear_regression_analysis
from scripts.analysis.models.logistic_regression import logistic_regression_analysis

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/errors.log", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def executar_modulo(nome, funcao):
    print(f"\n🚀 Iniciando {nome}...\n")
    try:
        funcao()
        time.sleep(1)
    except Exception as e:
        print(f"⚠ Erro ao executar {nome}: {e}")
        logging.error(f"Erro ao executar {nome}: {e}")

if __name__ == "__main__":
    print("🎯 Iniciando Pipeline de Modelagem Estatística e ML...\n")

    executar_modulo("Pré-processamento de Dados", preprocess_data)
    executar_modulo("Análise Estatística (Gumbel)", gumbel_analysis)
    executar_modulo("Regressão Linear", linear_regression_analysis)
    #executar_modulo("Regressão Logística", logistic_regression_analysis)

    print("\n✅ Pipeline concluído com sucesso! 🎉")
