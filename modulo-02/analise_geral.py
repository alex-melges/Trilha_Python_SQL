# analise_geral.py

import pandas as pd
from carregar_dados import carregar_dados

# Função para análise geral
def analise_geral(df):
    # Exemplo de análise simples
    print(f"Total de corridas: {len(df)}")
    print(f"Distância média percorrida: {df['Distância_km'].mean():.2f} km")
    print(f"Tempo médio: {df['Tempo_horas'].mean():.2f} horas")

# Usando a função
if __name__ == "__main__":
    caminho = r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv'
    df = carregar_dados(caminho)
    analise_geral(df)
