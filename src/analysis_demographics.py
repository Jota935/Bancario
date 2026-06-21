import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a base de dados
perfil = pd.read_csv('data/customer_profile_360.csv')

# 2. Agrupar por Região (Macro visão)
demografia_regiao = perfil.groupby('regiao').agg(
    num_clientes=('client_id', 'count'),
    salario_medio=('salario_medio_distrito', 'mean'),
    desemprego_medio=('taxa_desemprego_96', 'mean')
).reset_index().sort_values(by='num_clientes', ascending=False)

print("=== PERFIL DEMOGRÁFICO POR REGIÃO ===")
print(demografia_regiao.round(2))

# 3. Visualização: Número de clientes vs Salário Médio
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfico de barras para o número de clientes
sns.barplot(x='regiao', y='num_clientes', data=demografia_regiao, color='lightblue', ax=ax1)
ax1.set_ylabel('Número de Clientes', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
plt.xticks(rotation=45)

# Gráfico de linha para o salário médio (eixo secundário)
ax2 = ax1.twinx()
sns.lineplot(x='regiao', y='salario_medio', data=demografia_regiao, color='red', marker='o', ax=ax2, linewidth=2)
ax2.set_ylabel('Salário Médio', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Concentração de Clientes e Salário Médio por Região')
plt.tight_layout()
plt.show()