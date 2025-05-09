import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('corridas.db')

# Criar um cursor
cursor = conn.cursor()

# Ler o arquivo CSV com os dados das corridas
df = pd.read_csv(r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv')

# Inserir os dados na tabela
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO corridas (corredor, data, distancia_km, tempo_horas, pace_min_km)
    VALUES (?, ?, ?, ?, ?)
    ''', (row['Corredor'], row['Data'], row['Distância_km'], row['Tempo_horas'], row['Pace_min_km']))

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Todos os dados foram inseridos com sucesso!")
