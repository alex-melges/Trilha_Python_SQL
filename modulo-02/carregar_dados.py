# carregar_dados.py

import pandas as pd

# Função para carregar os dados do CSV
def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    return df

# Usando a função
if __name__ == "__main__":
    caminho = r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv'
    df = carregar_dados(caminho)
    print(df.head())  # Exibe as primeiras linhas para checar
