import os

print("A compilar as descobertas do projeto...")

relatorio = """# Relatório Executivo: Análise de Dados Bancários (PKDD'99)

## Visão Geral do Projeto
Através de engenharia de dados, unificámos múltiplas tabelas transacionais e demográficas para criar uma **Visão 360º** de 4.500 clientes com 15 atributos vitais (Problema 1).

## Principais Conclusões

### 1. Segmentação de Clientes (K-Means)
Identificámos 4 perfis distintos. Destacam-se os "Clientes Premium" (Segmento 0 e 3), que movimentam volumes milionários, e os "Clientes Conservadores" (Segmento 2), com idade média de 65 anos e menor rotação de capital.

### 2. Previsão de Risco de Crédito
O nosso modelo de Inteligência Artificial previu o risco com **88.29% de acurácia**. No entanto, detetámos um desafio clássico de dados desequilibrados: o banco tem muito poucos maus pagadores, o que obriga o modelo a ser conservador e exige a aplicação futura de técnicas como o SMOTE.

### 3. Tendências e Evolução
Entre janeiro e maio de 1993, o banco registou um crescimento explosivo de mais de **1.500%** no volume transacionado, indicando uma fortíssima fase de expansão e adoção no mercado.

### 4. Inteligência Geográfica e Demográfica
* **O Paradoxo de Praga:** A capital (Praga) é a região com o maior salário médio (12.541) e o menor desemprego (0.43%), mas é apenas a 5ª região com mais clientes (547). 
* **O Risco do Desemprego:** Zonas rurais/industriais (ex: Breclav) mostram que taxas de desemprego mais altas correlacionam-se diretamente com maiores taxas de incumprimento bancário. O banco está atualmente muito exposto nas regiões de Moravia e Bohemia.

### 5. Comportamento e Demografia Interna
* **Frequência de Extratos:** Clientes que exigem extratos semanais ou por transação possuem saldos médios cerca de **40% superiores** aos clientes de extrato mensal.
* **Idade vs Crédito:** O crédito está fortemente concentrado nos Adultos e Seniores (~12.5% têm empréstimos). Os jovens (8.6%) e reformados (2.4%) têm pouca expressão neste produto.
* **Igualdade de Género:** Existe uma paridade quase perfeita entre clientes masculinos (2.292) e femininos (2.208), sem diferenças estatísticas significativas nos saldos médios ou atribuição de empréstimos.

## Recomendação Estratégica
A equipa de Marketing deve redirecionar o seu orçamento de aquisição de clientes para a região de **Praga**, focando em captar o capital de alto rendimento que atualmente escapa ao banco, diversificando assim o risco geográfico atualmente concentrado em zonas de maior desemprego.
"""

# Guardar o relatório
caminho_relatorio = 'data/relatorio_final.md'
with open(caminho_relatorio, 'w', encoding='utf-8') as f:
    f.write(relatorio)

print(f"\nO seu relatório completo foi guardado em '{caminho_relatorio}'.")
print("Projeto concluído com sucesso!")