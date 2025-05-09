import sqlite3

# Função para estabelecer a conexão com o banco de dados
def conectar_db():
    """Estabelece a conexão com o banco de dados SQLite."""
    return sqlite3.connect('corridas.db')

# Função para calcular o tempo médio total de todas as corridas
def tempo_medio_total():
    """
    Calcula o tempo médio das corridas registradas.
    Exibe o tempo médio de todas as corridas em minutos.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT AVG(Tempo_horas) AS Tempo_Medio
        FROM corridas
    """)
    tempo_medio = cursor.fetchone()[0]
    print(f"\nTempo médio total das corridas: {tempo_medio * 60:.2f} minutos")
    
    conn.close()

# Função para calcular o pace médio por corredor
def pace_medio_por_corredor():
    """
    Calcula o pace médio de cada corredor, ou seja, a média de tempo por quilômetro.
    Exibe o pace médio por corredor em minutos por quilômetro (min/km).
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, AVG((Tempo_horas * 60) / Distancia_km) AS Pace_Medio
        FROM corridas
        GROUP BY Corredor
    """)
    pace_medio = cursor.fetchall()
    print("\nPace médio por corredor (min/km):")
    for corredor in pace_medio:
        print(f"{corredor[0]}: {corredor[1]:.2f} min/km")
    
    conn.close()

# Função para encontrar as corridas com o maior pace (mais lentas)
def maiores_paces():
    """
    Exibe as 10 corridas com o maior pace (mais lentas) em minutos por quilômetro.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, Distancia_km, Tempo_horas, ((Tempo_horas * 60) / Distancia_km) AS Pace
        FROM corridas
        ORDER BY Pace DESC
        LIMIT 10
    """)
    maiores_paces = cursor.fetchall()
    print("\nTop 10 corridas com maior pace (mais lentas):")
    for corrida in maiores_paces:
        print(f"{corrida[0]}: {corrida[1]} km em {corrida[2]} horas, Pace: {corrida[3]:.2f} min/km")
    
    conn.close()

# Função para encontrar as corridas com o menor pace (mais rápidas)
def menores_paces():
    """
    Exibe as 10 corridas com o menor pace (mais rápidas) em minutos por quilômetro.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, Distancia_km, Tempo_horas, ((Tempo_horas * 60) / Distancia_km) AS Pace
        FROM corridas
        ORDER BY Pace ASC
        LIMIT 10
    """)
    menores_paces = cursor.fetchall()
    print("\nTop 10 corridas com menor pace (mais rápidas):")
    for corrida in menores_paces:
        print(f"{corrida[0]}: {corrida[1]} km em {corrida[2]} horas, Pace: {corrida[3]:.2f} min/km")
    
    conn.close()

# Função para encontrar os corredores com maior distância percorrida
def corredores_maior_distancia():
    """
    Exibe os 5 corredores que percorreram as maiores distâncias.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Corredor, SUM(Distancia_km) AS Distancia_Total
        FROM corridas
        GROUP BY Corredor
        ORDER BY Distancia_Total DESC
        LIMIT 5
    """)
    maior_distancia = cursor.fetchall()
    print("\nTop 5 corredores com maior distância percorrida:")
    for corredor in maior_distancia:
        print(f"{corredor[0]}: {corredor[1]} km")
    
    conn.close()

# Função para encontrar os tempos mais rápidos para corridas de diferentes distâncias
def tempos_mais_rapidos_por_distancia():
    """
    Exibe os tempos mais rápidos para cada distância de corrida.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Distancia_km, MIN(Tempo_horas) AS Tempo_Rapido
        FROM corridas
        GROUP BY Distancia_km
        ORDER BY Distancia_km
    """)
    tempos_rapidos = cursor.fetchall()
    print("\nTempos mais rápidos por distância:")
    for tempo in tempos_rapidos:
        print(f"{tempo[0]} km: {tempo[1] * 60:.2f} minutos")
    
    conn.close()

# Função principal para rodar todas as análises
def main():
    tempo_medio_total()
    pace_medio_por_corredor()
    maiores_paces()
    menores_paces()
    corredores_maior_distancia()
    tempos_mais_rapidos_por_distancia()

# Rodar o script
if __name__ == "__main__":
    main()
