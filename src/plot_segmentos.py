import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/customer_segments_p2.csv')

# Gráfico de dispersão: Saldo vs Volume Movimentado
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='saldo_medio', y='volume_movimentado', hue='segmento_kmeans', palette='viridis')
plt.title('Segmentação de Clientes: Saldo Médio vs Volume Movimentado')
plt.show()