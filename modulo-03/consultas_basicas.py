import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('corridas.db')
cursor = conn.cursor()

# Consulta 1: Contar o número de registros
cursor.execute("SELECT COUNT(*) FROM corridas")
num_registros = cursor.fetchone()[0]
print(f"Número de registros: {num_registros}")

# Consulta 2: Listar todos os corredores e suas respectivas distâncias
cursor.execute("""
    SELECT Corredor, SUM(Distancia_km) AS Distancia_Total
    FROM corridas
    GROUP BY Corredor
""")
distancia_corrida = cursor.fetchall()
print("\nDistância total por corredor:")
for corredor in distancia_corrida:
    print(corredor)

# Consulta 3: Verificar o tempo médio por corredor
cursor.execute("""
    SELECT Corredor, AVG(Tempo_horas) AS Tempo_Medio
    FROM corridas
    GROUP BY Corredor
""")
tempo_medio = cursor.fetchall()
print("\nTempo médio por corredor:")
for corredor in tempo_medio:
    print(corredor)

# Fechar a conexão
conn.close()
