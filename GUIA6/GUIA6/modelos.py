# Paso 1: Importación de bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Paso 2: Cargar el conjunto de datos Iris desde seaborn
data = sns.load_dataset('iris')

# Ver las primeras filas del conjunto de datos
print("Primeras filas del conjunto de datos Iris:")
print(data.head())

# Paso 3: Preparación de los datos
# Variables predictoras
X = data[['sepal_length', 'sepal_width', 'petal_width']]

# Variable objetivo
y = data['petal_length']

# Dividir en conjuntos de entrenamiento y prueba (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)

# Paso 4: Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Mostrar coeficientes del modelo
print("\nCoeficientes del modelo:", model.coef_)
print("Intersección (intercepto):", model.intercept_)

# Paso 5: Realizar predicciones
y_pred = model.predict(X_test)

# Mostrar algunas predicciones comparadas con valores reales
predictions_df = pd.DataFrame({
    'Real': y_test.values,
    'Predicción': y_pred
})
print("\nPredicciones vs Valores reales:")
print(predictions_df.head())

# Paso 6: Evaluación del modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nError cuadrático medio (MSE): {mse:.2f}")
print(f"Coeficiente de determinación R²: {r2:.2f}")

# Paso 7: Visualización de resultados
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         color='red', linewidth=2, label="Línea de referencia")
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Valores reales vs Predicciones")
plt.legend()
plt.grid(True)
plt.show()
