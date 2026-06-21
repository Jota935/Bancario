import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a base de dados
perfil = pd.read_csv('data/customer_profile_360.csv')

# 2. Calcular métricas financeiras por género
genero_stats = perfil.groupby('genero').agg({
    'client_id': 'count',
    'saldo_medio': 'mean',
    'volume_movimentado': 'sum',
    'emprestimo_ativo': 'sum'
}).rename(columns={'client_id': 'num_clientes'})

print("=== ESTATÍSTICAS FINANCEIRAS POR GÉNERO ===")
print(genero_stats.round(2))

# 3. Visualização Dupla (Clientes e Saldo Médio)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Distribuição de Clientes
sns.barplot(x=genero_stats.index, y='num_clientes', data=genero_stats, palette='pastel', ax=axes[0])
axes[0].set_title('Número de Clientes por Género')
axes[0].set_ylabel('Quantidade de Clientes')

# Gráfico 2: Saldo Médio
sns.barplot(x=genero_stats.index, y='saldo_medio', data=genero_stats, palette='dark', ax=axes[1])
axes[1].set_title('Saldo Médio por Género')
axes[1].set_ylabel('Saldo Médio')

plt.tight_layout()
plt.show()