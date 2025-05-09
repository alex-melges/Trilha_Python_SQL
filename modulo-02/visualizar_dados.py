# visualizar_dados.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from carregar_dados import carregar_dados

# Função para gerar gráficos
def visualizar_dados(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Gráfico de distância vs tempo
    sns.scatterplot(x='Distância_km', y='Tempo_horas', data=df)
    plt.title('Distância vs Tempo')
    plt.xlabel('Distância (km)')
    plt.ylabel('Tempo (horas)')
    plt.show()

# Usando a função
if __name__ == "__main__":
    caminho = r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv'
    df = carregar_dados(caminho)
    df['Pace_calculado'] = (df['Tempo_horas'] * 60) / df['Distância_km']  # Recalcular o pace
    visualizar_dados(df)
