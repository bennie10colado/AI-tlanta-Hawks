import os

print("🚀 Iniciando o projeto AI-tlanta Hawks...")

# Rodar coleta de dados
print("\n🔄 Coletando dados da NBA...")
os.system("python scripts/fetch_nba_data.py")

# Rodar análise de estatísticas
print("\n📊 Gerando estatísticas...")
os.system("python scripts/analyze_data.py")

# Gerar gráficos
print("\n📈 Criando visualizações...")
os.system("python scripts/visualize.py")

print("\n✅ Projeto finalizado!")
