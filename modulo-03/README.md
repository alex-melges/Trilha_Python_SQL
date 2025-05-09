# Módulo 03 — Introdução ao SQL + Python

## 🎯 Objetivo
Neste módulo, você aprenderá a integrar o SQL com o Python, utilizando o banco de dados SQLite para manipular e consultar dados de corridas de rua. Vamos explorar como realizar consultas básicas e avançadas em SQL, além de interagir com as tabelas diretamente do Python, usando a biblioteca **SQLite**.

## 🛠️ Ferramentas utilizadas
- Python 3.x
- VS Code
- Terminal / Prompt de comando
- Pandas
- SQLite (Banco de dados)
- SQLAlchemy (para interagir com o banco de dados)
- Git (para controle de versões)

---

## 📦 Conteúdo do módulo

### ✔️ Parte 1 — Preparação
- Criação e organização do banco de dados SQLite
- Instalação e configuração da biblioteca **SQLAlchemy**
- Conexão ao banco de dados com **SQLite** no Python

### ✔️ Parte 2 — Manipulação de Dados com SQL
- Criação de tabelas para armazenar dados de corridas
- Inserção de dados de corredores no banco de dados
- Realização de consultas SQL para extrair e filtrar informações relevantes

### ✔️ Parte 3 — Integração entre Python e SQL
- Interação com o banco de dados via **SQLAlchemy**
- Recuperação e manipulação de dados no Python usando SQL
- Exibição de resultados com **Pandas** para análise

### 🔍 Parte 4 — Extras
- Realização de consultas SQL mais complexas
- Exibição de resultados através de gráficos gerados no **Matplotlib** (opcional)
- Criação de funções para realizar consultas de maneira automatizada

---

## 📈 Resultado Esperado

Ao final deste módulo, você será capaz de:
- Criar e manipular bancos de dados SQLite a partir do Python
- Realizar consultas SQL diretamente do Python
- Analisar e visualizar dados extraídos do banco de dados
- Integrar Python e SQL para facilitar o processamento de grandes volumes de dados

---

## 🚀 Como executar

1. **Certifique-se de estar na pasta do módulo:**

```bash
cd modulo-03
```

2. **Criação do banco de dados e tabelas:**
Execute o arquivo `criar_banco.py` para criar o banco de dados SQLite e as tabelas necessárias para armazenar os dados de corridas:

```bash
python criar_banco.py
```

3. **Inserção dos dados no banco de dados:**
Após a criação das tabelas, execute o arquivo `inserir_dados.py` para inserir os dados dos corredores no banco de dados:

```bash
python inserir_dados.py
```

4. **Consulta aos dados:**
Por fim, execute os arquivos de consultas SQL para visualizar os resultados.

**Obs.: Instalação das bibliotecas necessárias:**
Antes de rodar os scripts, certifique-se de instalar as bibliotecas necessárias:

```bash
pip install pandas sqlalchemy sqlite3
```
---

## 📚 Próximo módulo
Módulo 04 — Limpeza e Tratamento de Dados