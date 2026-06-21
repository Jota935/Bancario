import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from load_data import loan

# 1. Carregar perfil 360 e preparar dados do empréstimo
perfil = pd.read_csv('data/customer_profile_360.csv')

# Filtrar apenas clientes com empréstimos
df_loan = loan[['account_id', 'status']]. copy()
# Criar variável alvo: 1 para default (status B ou D), 0 para pago (A ou C)
df_loan['risco'] = df_loan['status'].apply(lambda x: 1 if x in ['B', 'D'] else 0)

# Unir ao perfil
data = pd.merge(perfil, df_loan, on='account_id', how='inner')

# 2. Selecionar features para o treino
features = ['idade', 'saldo_medio', 'num_transacoes', 'volume_movimentado', 'valor_emprestimo', 'num_cartoes']
X = data[features]
y = data['risco']

# 3. Treinar o modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Avaliar
y_pred = model.predict(X_test)
print("=== RESULTADOS DO MODELO DE RISCO ===")
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2%}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Identificar os clientes de maior risco no teste
data['probabilidade_risco'] = model.predict_proba(data[features])[:, 1]
data.sort_values(by='probabilidade_risco', ascending=False).to_csv('data/risco_clientes.csv', index=False)
print("\nLista de clientes de maior risco guardada em 'data/risco_clientes.csv'")