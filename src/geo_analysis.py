import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados
perfil = pd.read_csv('data/customer_profile_360.csv')
# Carregar o risco que calculámos no Problema 3 (assumindo que guardou)
try:
    risco_df = pd.read_csv('data/risco_clientes.csv')
    perfil = pd.merge(perfil, risco_df[['client_id', 'risco']], on='client_id', how='left')
except:
    print("Aviso: 'data/risco_clientes.csv' não encontrado. Analisando apenas dados geográficos.")

# 2. Agregação por Distrito
geo_summary = perfil.groupby('nome_distrito').agg({
    'saldo_medio': 'mean',
    'volume_movimentado': 'sum',
    'risco': 'mean', # % de incumprimento no distrito
    'salario_medio_distrito': 'first',
    'taxa_desemprego_96': 'first'
}).reset_index()

print("Resumo Geográfico (Primeiros 5 distritos):")
print(geo_summary.head())

# 3. Visualização: Correlação entre Desemprego e Risco
plt.figure(figsize=(10, 6))
sns.scatterplot(data=geo_summary, x='taxa_desemprego_96', y='risco', size='volume_movimentado', sizes=(50, 500))
plt.title('Impacto do Desemprego no Risco de Incumprimento por Distrito')
plt.xlabel('Taxa de Desemprego')
plt.ylabel('Média de Risco de Crédito')
plt.grid(True)
plt.savefig('data/geo_analysis.png')
plt.show()