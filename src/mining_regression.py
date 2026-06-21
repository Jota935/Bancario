import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("A treinar o modelo de Regressão!")
perfil = pd.read_csv('data/customer_profile_360.csv')

# Variáveis que influenciam o saldo
features = ['idade', 'num_transacoes', 'salario_medio_distrito', 'taxa_desemprego_96']
X = perfil[features].fillna(0)
y = perfil['saldo_medio'].fillna(0)

# Dividir dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar Regressão Linear
modelo_reg = LinearRegression()
modelo_reg.fit(X_train, y_train)

# Avaliar
y_pred = modelo_reg.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"\n=== RESULTADOS DA REGRESSÃO ===")
print(f"R² Score (Precisão do Modelo): {r2:.4f}")
print("Nota: Se o R² for baixo, significa que o saldo bancário depende de fatores mais complexos do que apenas a idade e o salário da região.")