# detectar_anomalias.py

import pandas as pd
from carregar_dados import carregar_dados

# Função para detectar anomalias
def detectar_anomalias(df):
    # Exemplo: detectar paces abaixo de 2 minutos por km
    anomalias = df[df['Pace_calculado'] < 2]
    if not anomalias.empty:
        print("Anomalias encontradas:")
        print(anomalias[['Corredor', 'Data', 'Distância_km', 'Tempo_horas', 'Pace_calculado']])
    else:
        print("Nenhuma anomalia encontrada.")

# Usando a função
if __name__ == "__main__":
    caminho = r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv'
    df = carregar_dados(caminho)
    df['Pace_calculado'] = (df['Tempo_horas'] * 60) / df['Distância_km']  # Recalcular o pace
    detectar_anomalias(df)
