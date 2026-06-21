import pandas as pd
from database import conectar

conn = conectar()

# Tabelas que já carregou
client = pd.read_sql("SELECT * FROM client", conn)
account = pd.read_sql("SELECT * FROM account", conn)
loan = pd.read_sql("SELECT * FROM loan", conn)

# Tabelas adicionais essenciais para a Visão 360º
disp = pd.read_sql("SELECT * FROM disp", conn)         # Liga clientes às contas (owner/disponent)
card = pd.read_sql("SELECT * FROM card", conn)         # Cartões associados aos clientes
trans = pd.read_sql("SELECT * FROM trans", conn)       # Transações das contas
district = pd.read_sql("SELECT * FROM district", conn) # Dados demográficos (Problema 8)

conn.close()