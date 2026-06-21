import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

print("A iniciar a Deteção de Anomalias...")
perfil = pd.read_csv('data/customer_profile_360.csv')

# Selecionar variáveis financeiras para procurar comportamentos estranhos
features =['saldo_medio', 'num_transacoes', 'volume_movimentado']
X = perfil[features].fillna(0)

# Configurar o modelo para detetar 5% de anomalias (clientes atípicos)
iso_forest = IsolationForest(contamination=0.05, random_state=42)
perfil['anomalia'] = iso_forest.fit_predict(X)

# Filtrar as anomalias (-1 significa anomalia, 1 significa normal)
anomalias = perfil[perfil['anomalia'] == -1]

print(f"\nForam detetadas {len(anomalias)} contas com comportamento anómalo!")
print("Top 5 contas mais anómalas (Possível fraude ou clientes VIP extremos):")
print(anomalias[['client_id', 'saldo_medio', 'volume_movimentado']].head())

# Visualizar as anomalias
plt.figure(figsize=(10, 6))
sns.scatterplot(data=perfil, x='saldo_medio', y='volume_movimentado', hue='anomalia', palette={1: 'blue', -1: 'red'})
plt.title('Deteção de Anomalias: Saldo vs Volume Movimentado (Vermelho = Anomalia)')
plt.show()