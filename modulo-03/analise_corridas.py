import sqlite3

# Função para estabelecer conexão com o banco de dados
def conectar_db():
    return sqlite3.connect('corridas.db')

# Função para calcular o tempo médio total
def tempo_medio_total():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT AVG(Tempo_horas) AS Tempo_Medio
        FROM corridas
    """)
    tempo_medio = cursor.fetchone()[0]
    print(f"\nTempo médio total das corridas: {tempo_medio:.2f} horas")
    
    conn.close()

# Função para calcular o pace médio por corredor
def pace_medio_por_corredor():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, AVG(Tempo_horas / Distancia_km) AS Pace_Medio
        FROM corridas
        GROUP BY Corredor
    """)
    pace_medio = cursor.fetchall()
    print("\nPace médio por corredor (tempo por km):")
    for corredor in pace_medio:
        print(f"{corredor[0]}: {corredor[1]:.2f} horas/km")
    
    conn.close()

# Função para encontrar as corridas com o maior pace (mais lentas)
def maiores_paces():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, Distancia_km, Tempo_horas, (Tempo_horas / Distancia_km) AS Pace
        FROM corridas
        ORDER BY Pace DESC
        LIMIT 10
    """)
    maiores_paces = cursor.fetchall()
    print("\nTop 10 corridas com maior pace (mais lentas):")
    for corrida in maiores_paces:
        print(f"{corrida[0]}: {corrida[1]} km em {corrida[2]} horas, Pace: {corrida[3]:.2f} horas/km")
    
    conn.close()

# Função para encontrar as corridas com o menor pace (mais rápidas)
def menores_paces():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, Distancia_km, Tempo_horas, (Tempo_horas / Distancia_km) AS Pace
        FROM corridas
        ORDER BY Pace ASC
        LIMIT 10
    """)
    menores_paces = cursor.fetchall()
    print("\nTop 10 corridas com menor pace (mais rápidas):")
    for corrida in menores_paces:
        print(f"{corrida[0]}: {corrida[1]} km em {corrida[2]} horas, Pace: {corrida[3]:.2f} horas/km")
    
    conn.close()

# Função principal para rodar as análises
def main():
    tempo_medio_total()
    pace_medio_por_corredor()
    maiores_paces()
    menores_paces()

# Rodar o script
if __name__ == "__main__":
    main()
