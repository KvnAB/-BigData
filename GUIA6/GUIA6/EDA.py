# Paso 2: Importación de librerías y carga de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos Iris desde seaborn
data = sns.load_dataset('iris')

# Ver las primeras filas del conjunto de datos
print("Primeras filas del conjunto de datos:")
print(data.head())

# Paso 3: Descripción general del conjunto de datos
print("\nDescripción general del conjunto de datos:")
print(data.describe())

# Paso 4: Identificación de valores atípicos (boxplots)
plt.figure(figsize=(12, 8))
sns.boxplot(data=data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
plt.title("Boxplot de las características del Iris")
plt.show()

# Paso 5: Visualización de la distribución de los datos (Histogramas)
data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].hist(bins=15, figsize=(12, 8))
plt.suptitle("Histogramas de las características del Iris")
plt.show()

# Paso 6: Relación entre las características (Gráficas de dispersión / Pairplot)
sns.pairplot(data, hue='species')
plt.suptitle("Pairplot de las características del Iris", y=1.02)
plt.show()

# Paso 7: Correlación entre características (Mapa de calor)
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Mapa de calor de la correlación entre características")
plt.show()

# Paso 8: Identificación de patrones entre especies
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='sepal_length', data=data)
plt.title("Comparación de la longitud del sépalo por especie")
plt.show()
