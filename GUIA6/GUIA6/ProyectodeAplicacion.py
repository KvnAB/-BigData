# Paso 1: Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Paso 2: Cargar el conjunto de datos Iris desde seaborn
data = sns.load_dataset('iris')

# Ver las primeras filas del conjunto de datos
print("Primeras filas del conjunto de datos Iris:")
print(data.head())

# Paso 3: Preprocesamiento de los datos
# Separar las variables predictoras (X) y la variable objetivo (y)
X = data.drop('species', axis=1)  # Las características (sin la columna 'species')
y = data['species']  # La variable objetivo (la especie de la flor)

# Dividir el dataset en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos para mejorar el rendimiento del modelo (opcional, pero recomendado para algunos modelos)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Paso 4: Crear el modelo de Árbol de Decisión y entrenarlo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Paso 5: Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Paso 6: Evaluación del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"\nPrecisión del modelo: {accuracy:.2f}")

# Reporte de clasificación
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# Paso 7: Visualización de la matriz de confusión
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.title("Matriz de Confusión")
plt.show()
