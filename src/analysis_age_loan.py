import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a base de dados
perfil = pd.read_csv('data/customer_profile_360.csv')

# 2. Criar faixas etárias para facilitar a visualização
perfil['faixa_etaria'] = pd.cut(perfil['idade'],bins=[0, 25, 40, 60, 100], labels=['Jovem', 'Adulto', 'Sénior', 'Reformado'])

# 3. Comparar Idade vs Empréstimo Ativo
plt.figure(figsize=(10, 6))
sns.boxplot(x='faixa_etaria', y='idade', hue='emprestimo_ativo', data=perfil, palette='pastel')
plt.title('Distribuição de Idade por Empréstimo Ativo (0=Não, 1=Sim)')
plt.ylabel('Idade')
plt.show()

# 4. Estatísticas rápidas
age_stats = perfil.groupby('faixa_etaria')['emprestimo_ativo'].mean()
print("=== % DE EMPRÉSTIMOS ATIVOS POR FAIXA ETÁRIA ===")
print(age_stats * 100)