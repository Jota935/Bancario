import pandas as pd
import matplotlib.pyplot as plt
from load_data import trans

print("A iniciar a Análise de Tendências (Problema 4)...")

# 1. Converter data para datetime
trans['date'] = pd.to_datetime(trans['date'], format='%y%m%d')

# 2. Criar coluna de período (Ano-Mês)
trans['ano_mes'] = trans['date'].dt.to_period('M')

# 3. Agregar volume de transações por mês
tendencia = trans.groupby('ano_mes').agg(
    volume_total=('amount', 'sum'),
    numero_transacoes=('trans_id', 'count')
).reset_index()

# 4. Converter 'ano_mes' para string para plotar
tendencia['ano_mes'] = tendencia['ano_mes'].astype(str)

print("Tendência calculada:")
print(tendencia.head())

# 5. Visualização
plt.figure(figsize=(12, 6))
plt.plot(tendencia['ano_mes'], tendencia['volume_total'], marker='o', linestyle='-', color='b')
plt.title('Tendência do Volume de Transações (1993 - 1998)')
plt.xlabel('Data')
plt.ylabel('Volume Total')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('data/trend_analysis.png')
plt.show()

# Guardar os dados processados
tendencia.to_csv('data/trend_analysis.csv', index=False)
print("\nAnálise de tendências guardada em 'data/trend_analysis.csv' e gráfico em 'data/trend_analysis.png'")