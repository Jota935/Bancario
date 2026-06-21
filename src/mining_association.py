import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

print("A calcular Regras de Associação...")
perfil = pd.read_csv('data/customer_profile_360.csv')

# Para Regras de Associação, precisamos de dados binários (Verdadeiro/Falso)
cesto_produtos = pd.DataFrame()
cesto_produtos['tem_cartao'] = perfil['num_cartoes'] > 0
cesto_produtos['tem_emprestimo'] = perfil['emprestimo_ativo'] == 1
cesto_produtos['saldo_alto'] = perfil['saldo_medio'] > perfil['saldo_medio'].mean()
cesto_produtos['homem'] = perfil['genero'] == 'M'

# Aplicar o algoritmo Apriori
itemsets_frequentes = apriori(cesto_produtos, min_support=0.1, use_colnames=True)
regras = association_rules(itemsets_frequentes, metric="confidence", min_threshold=0.2)

print("\n=== REGRAS DE ASSOCIAÇÃO (TOP 5) ===")
# Mostrar quem compra o quê, ordenado pela "confiança" na regra
print(regras[['antecedents', 'consequents', 'support', 'confidence']].sort_values(by='confidence', ascending=False).head())