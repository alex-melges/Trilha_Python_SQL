import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados de corridas
df = pd.read_csv('dados_corridas.csv')

# Mostrar as primeiras linhas do dataset
print("Dados iniciais:")
print(df.head())

# Calcular o Pace médio geral
pace_medio = df['Pace_min_km'].mean()
print(f"\nPace médio das corridas: {pace_medio:.2f} minutos por km")

# Média por corredor
print("\nPace médio por corredor:")
pace_corredores = df.groupby('Corredor')['Pace_min_km'].mean()
print(pace_corredores)

# Média por distância
print("\nPace médio por distância:")
pace_distancias = df.groupby('Distância_km')['Pace_min_km'].mean()
print(pace_distancias)

# 📊 Gráfico 1: Pace médio por corredor (barras)
plt.figure(figsize=(10, 5))
pace_corredores.plot(kind='bar', color='skyblue')
plt.title('Pace médio por Corredor')
plt.ylabel('Pace (min/km)')
plt.xlabel('Corredor')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📈 Gráfico 2: Pace médio por distância (linhas)
plt.figure(figsize=(8, 4))
pace_distancias.plot(marker='o', linestyle='-', color='green')
plt.title('Pace médio por Distância')
plt.ylabel('Pace (min/km)')
plt.xlabel('Distância (km)')
plt.grid(True)
plt.tight_layout()
plt.show()
