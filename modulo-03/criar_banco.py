import sqlite3

# Conectar ou criar um banco de dados SQLite
conn = sqlite3.connect('corridas.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar a tabela corridas
cursor.execute('''
CREATE TABLE IF NOT EXISTS corridas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    corredor TEXT NOT NULL,
    data TEXT NOT NULL,
    distancia_km REAL NOT NULL,
    tempo_horas REAL NOT NULL,
    pace_min_km REAL NOT NULL
)
''')

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela criados com sucesso!")
