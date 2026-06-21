import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

print("A iniciar a Segmentação de Clientes (Problema 2)...")

# 1. Carregar a Visão 360º criada no Problema 1
# Nota: Assumindo que o script corre na raiz do projeto 'Bancario'
df = pd.read_csv('data/customer_profile_360.csv')

# 2. Selecionar as variáveis (features) comportamentais para a segmentação
# O K-Means precisa de dados numéricos contínuos para calcular distâncias
features = ['idade', 'saldo_medio', 'num_transacoes', 'volume_movimentado', 'num_cartoes']
X = df[features]

# 3. Normalizar os Dados (Passo CRÍTICO)
# O K-Means é muito sensível à escala. Como o volume_movimentado pode estar nos milhares e o num_cartoes é 1 ou 2,
# precisamos de colocar todas as variáveis na mesma escala matemática.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Aplicar o Algoritmo K-Means
# Vamos assumir a criação de 4 segmentos (pode ajustar este número depois usando o Método do Cotovelo)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['segmento_kmeans'] = kmeans.fit_predict(X_scaled)

# 5. Nomear / Analisar os Segmentos
# Vamos calcular as médias de cada variável por grupo para entender quem são
analise_segmentos = df.groupby('segmento_kmeans')[features].mean()
print("\n=== ANÁLISE DOS 4 SEGMENTOS DE CLIENTES (MÉDIAS) ===")
print(analise_segmentos.round(2))

# ==========================================
# 6. INTERPRETAÇÃO E ATRIBUIÇÃO DE PERFIS
# ==========================================
# Baseado nos resultados típicos do PKDD'99, podemos categorizá-los. 
# (Os limites dependem do resultado exato do agrupamento, o código abaixo é um classificador simplificado pós-análise)
def categorizar_segmento(row):
    if row['volume_movimentado'] > df['volume_movimentado'].quantile(0.75):
         return 'Cliente Premium (Alta Rentabilidade)'
    elif row['saldo_medio'] < df['saldo_medio'].quantile(0.25) and row['num_transacoes'] > df['num_transacoes'].mean():
         return 'Cliente de Risco (Baixo Saldo, Alta Movimentação)'
    elif row['num_transacoes'] < df['num_transacoes'].quantile(0.25):
         return 'Cliente Inativo'
    else:
         return 'Cliente Regular'

df['perfil_comportamental'] = df.apply(categorizar_segmento, axis=1)

# Guardar a base de dados agora com os segmentos!
df.to_csv('data/customer_segments_p2.csv', index=False)
print("\nSegmentação concluída com sucesso! Ficheiro guardado em 'data/customer_segments_p2.csv'")