import pandas as pd
import numpy as np
from load_data import client, account, disp, loan, card, trans, district

print("A iniciar a construção do Perfil Inteligente do Cliente (Visão 360º)...")

# ==========================================
# 1. TRATAMENTO E AGREGAÇÃO DE TRANSAÇÕES (trans)
# ==========================================
print("A processar agregações de transações...")
trans_agg = trans.groupby('account_id').agg(
    saldo_medio=('balance', 'mean'),
    num_transacoes=('trans_id', 'count'),
    volume_movimentado=('amount', 'sum')
).reset_index()


# ==========================================
# 2. TRATAMENTO DE CARTÕES (card) E RELAÇÕES (disp)
# ==========================================
print("A processar informações de cartões...")
card_disp = pd.merge(card, disp, on='disp_id', how='inner')
card_agg = card_disp.groupby('account_id').agg(
    num_cartoes=('card_id', 'count')
).reset_index()


# ==========================================
# 3. TRATAMENTO DE EMPRÉSTIMOS (loan)
# ==========================================
print("A processar informações de empréstimos...")
# NOTA: Assumindo que a tabela loan tem a coluna 'status'. 
# Se der erro aqui, é porque o 'status' também tem outro nome na sua BD!
if 'status' in loan.columns:
    loan['emprestimo_ativo'] = loan['status'].isin(['C', 'D']).astype(int)
else:
    loan['emprestimo_ativo'] = 1 # Fallback caso a coluna não exista

loan_features = loan[['account_id', 'amount', 'duration', 'payments', 'emprestimo_ativo']].rename(
    columns={'amount': 'valor_emprestimo', 'duration': 'duracao_emprestimo', 'payments': 'prestacao_mensal'}
)


# ==========================================
# 4. CONSTRUÇÃO DA BASE UNIFICADA (Merge Principal)
# ==========================================
print("A unificar tabelas relacionais...")
disp_owners = disp[disp['type'] == 'OWNER']

perfil = pd.merge(client, disp_owners, on='client_id', how='inner')
perfil = pd.merge(perfil, account, on='account_id', how='inner', suffixes=('_cliente', '_conta'))
perfil = pd.merge(perfil, trans_agg, on='account_id', how='left')
perfil = pd.merge(perfil, card_agg, on='account_id', how='left')
perfil = pd.merge(perfil, loan_features, on='account_id', how='left')

perfil['num_cartoes'] = perfil['num_cartoes'].fillna(0).astype(int)
perfil['emprestimo_ativo'] = perfil['emprestimo_ativo'].fillna(0).astype(int)
perfil['valor_emprestimo'] = perfil['valor_emprestimo'].fillna(0)
perfil['duracao_emprestimo'] = perfil['duracao_emprestimo'].fillna(0)
perfil['prestacao_mensal'] = perfil['prestacao_mensal'].fillna(0)
perfil['saldo_medio'] = perfil['saldo_medio'].fillna(0)
perfil['num_transacoes'] = perfil['num_transacoes'].fillna(0).astype(int)
perfil['volume_movimentado'] = perfil['volume_movimentado'].fillna(0)


# ==========================================
# 5. INTEGRAR DADOS DEMOGRÁFICOS (district)
# ==========================================
print("A integrar dados demográficos do distrito...")
district_features = district.rename(columns={
    'A1': 'district_id',
    'A2': 'nome_distrito',
    'A3': 'regiao',
    'A4': 'num_habitantes',
    'A11': 'salario_medio_distrito',
    'A13': 'taxa_desemprego_96'
})[['district_id', 'nome_distrito', 'regiao', 'num_habitantes', 'salario_medio_distrito', 'taxa_desemprego_96']]

# Como a sua tabela de clientes já tem district_id, usamos isso diretamente
perfil = pd.merge(perfil, district_features, left_on='district_id_cliente', right_on='district_id', how='left')


# ==========================================
# 6. ENGENHARIA DE ATRIBUTOS ADICIONAIS (Cálculo Simples da Idade)
# ==========================================
print("A calcular a idade a partir da coluna 'birth_date'...")

# Garantir que a coluna birth_date é tratada como data pelo Pandas
perfil['birth_date'] = pd.to_datetime(perfil['birth_date'])

# Como os dados do PKDD Bank são de 1999, calculamos a idade em relação a esse ano
perfil['idade'] = 1999 - perfil['birth_date'].dt.year

# Mudar o nome da coluna de 'gender' para 'genero' para manter o padrão
perfil = perfil.rename(columns={'gender': 'genero'})


# ==========================================
# 7. SELEÇÃO E LIMPEZA FINAL DO PERFIL 360º
# ==========================================
perfil_360 = perfil[[
    'client_id', 'account_id', 'genero', 'idade', 
    'nome_distrito', 'regiao', 'salario_medio_distrito', 'taxa_desemprego_96', 
    'frequency',         
    'saldo_medio',       
    'num_transacoes',    
    'volume_movimentado',
    'emprestimo_ativo',  
    'valor_emprestimo', 
    'num_cartoes'        
]].copy()

print(f"\nSucesso! Perfil 360º construído com {perfil_360.shape[0]} clientes e {perfil_360.shape[1]} atributos.")

# Guardar o perfil tratado
perfil_360.to_csv('data/customer_profile_360.csv', index=False)
print("\nFicheiro 'customer_profile_360.csv' guardado com sucesso na pasta data/!")