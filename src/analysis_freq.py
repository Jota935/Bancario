import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a nossa base de dados unificada
perfil = pd.read_csv('data/customer_profile_360.csv')

# 2. Analisar média de saldo e volume por frequência de extrato
freq_analysis = perfil.groupby('frequency').agg({
    'saldo_medio': 'mean',
    'volume_movimentado': 'mean',
    'client_id': 'count'
}).rename(columns={'client_id': 'num_clientes'})

print("=== IMPACTO DA FREQUÊNCIA DE EXTRATOS ===")
print(freq_analysis.round(2))

# 3. Visualizar a diferença de saldo médio por frequência
plt.figure(figsize=(10, 5))
sns.barplot(x=freq_analysis.index, y='saldo_medio', data=freq_analysis, palette='viridis')
plt.title('Saldo Médio por Frequência de Extrato')
plt.ylabel('Saldo Médio')
plt.show()