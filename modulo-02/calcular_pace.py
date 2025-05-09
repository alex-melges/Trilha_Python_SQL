# calcular_pace.py

import pandas as pd
from carregar_dados import carregar_dados

# Função para calcular o pace
def calcular_pace(df):
    df['Pace_calculado'] = (df['Tempo_horas'] * 60) / df['Distância_km']
    return df

# Usando a função
if __name__ == "__main__":
    caminho = r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv'
    df = carregar_dados(caminho)  # Carregar os dados
    df = calcular_pace(df)  # Calcular o pace
    print(df[['Corredor', 'Data', 'Distância_km', 'Tempo_horas', 'Pace_calculado']].head())  # Exibir as primeiras linhas
