import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv(r'C:\Users\User\Documents\Projetos de Programação\Trilha_Python_SQL\modulo-01\dados_corridas.csv')

# Configurar estilo do Seaborn
sns.set(style="whitegrid")

# Criar gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Distância_km', y='Tempo_horas', hue='Corredor')

# Títulos e rótulos
plt.title('Distância vs Tempo de Corrida')
plt.xlabel('Distância (km)')
plt.ylabel('Tempo (horas)')

# Mostrar o gráfico
plt.tight_layout()
plt.show()
