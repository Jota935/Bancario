# Sistema de Data Mining e Inteligência Bancária (Caso PKDD'99)

Este projeto aplica a metodologia **KDD (Knowledge Discovery in Databases)** sobre uma base de dados transacional e demográfica de um banco checo (Dataset PKDD'99). O objetivo é consolidar dados dispersos numa Visão 360º do cliente e extrair inteligência de negócio através de modelos de clustering, classificação e deteção de anomalias.

---

## 🚀 Funcionalidades Principais

1. **Visão 360º do Cliente:** Integração e limpeza de 7 tabelas relacionais do MySQL para criar um perfil unificado.
2. **Segmentação Comportamental:** Agrupamento automático de clientes em 4 perfis distintos utilizando o algoritmo **K-Means**.
3. **Análise e Previsão de Risco:** Modelação preditiva com **Random Forest** para identificar potenciais clientes em incumprimento de crédito (Classes B e D).
4. **Deteção de Anomalias:** Identificação de transações financeiras atípicas e suspeitas usando **Isolation Forest**.
5. **Inteligência Geográfica e Temporal:** Mapeamento do impacto de indicadores socioeconómicos regionais e análise da evolução temporal do banco.

---

## 📂 Estrutura do Projeto

```text
Bancario/
│
├── data/                           # Ficheiros CSV gerados e consumidos pelos modelos
│   ├── customer_profile_360.csv    # Visão 360º consolidada
│   ├── customer_segments_p2.csv    # Dados dos clientes com os clusters do K-Means
│   └── risco_clientes.csv          # Base de empréstimos com scorings de risco
│
├── src/                            # Código-fonte do projeto
│   ├── database.py                 # Configuração da ligação ao MySQL (pkdd_bank)
│   ├── load_data.py                # Pipeline de extração e Engenharia de Dados (Visão 360º)
│   ├── check_dates.py              # Script utilitário para validação de integridade temporal
│   ├── segmentation.py             # Script de clustering (K-Means) e geração de gráficos
│   └── risk_analysis.py            # Script de modelação de risco e classificação
│
├── README.md                       # Documentação do projeto
└── requisitos.txt                  # Bibliotecas Python necessárias
🛠️ Pré-requisitos
Antes de executar o projeto, certifique-se de que tem instalado na sua máquina:

Python 3.10+ (Testado na versão 3.14)

MySQL Server com a base de dados pkdd_bank devidamente importada e com as tabelas financeiras populadas (client, account, trans, loan, disp, card, district).

Instalação de Dependências
Abra o terminal na raiz do projeto e instale as bibliotecas necessárias:

Bash
pip install pandas numpy scikit-learn matplotlib seaborn mysql-connector-python
⚙️ Configuração da Base de Dados
Antes de correr os scripts, verifique o ficheiro src/database.py para garantir que as credenciais do seu MySQL estão corretas:

Python
# src/database.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="O_SEU_UTILIZADOR",      # ex: "root"
        password="A_SUA_PASSWORD",
        database="pkdd_bank"          # Nome da base de dados unificada
    )
🏃‍♂️ Como Executar o Projeto (Passo a Passo)
A execução deve seguir uma ordem lógica, pois os scripts avançados dependem dos dados gerados pelos scripts iniciais:

Passo 1: Construir a Visão 360º
Este script vai extrair todas as tabelas do MySQL, fazer as junções relacionais (merges) e criar a base unificada na pasta data/.

Bash
python src/load_data.py
Resultado: Criação do ficheiro data/customer_profile_360.csv.

Passo 2: Executar a Segmentação de Clientes
Este script consome a Visão 360º, aplica o algoritmo K-Means e gera os gráficos de perfis.

Bash
python src/segmentation.py
Resultados: Criação do ficheiro data/customer_segments_p2.csv e dos gráficos de agrupamento.

Passo 3: Avaliar o Risco de Crédito e Anomalias
Este script foca-se na tabela de empréstimos e no histórico transacional para classificar o risco de incumprimento e detetar transações fora do padrão.

Bash
python src/risk_analysis.py
Resultados: Criação do ficheiro data/risco_clientes.csv e exportação dos gráficos de análise de risco e anomalias.

📊 Gráficos Exportados e Significados
Após rodar a pipeline completa, o sistema gera um conjunto de visualizações na raiz ou na pasta de relatórios:

Segments_p2.png: Dispersão dos 4 grupos de clientes identificados pelo K-Means.

Distribuicao_de_idade_por_emprestimo.png: Análise das faixas etárias vs saúde do crédito (Classes A, B, C, D).

demografica_regiao.png & geo_analysis.png: Distribuição geográfica dos clientes e correlação com desemprego e salários.

Detecao_de_anomalias.png: Isolamento visual de transações suspeitas através de Isolation Forest.

trend_analysis.png: Gráfico do crescimento do volume transacional ao longo do tempo.

analise_genero.png: Demonstração da paridade de género e equilíbrio de saldos no banco.
