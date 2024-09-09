# Instalación de librerías necesarias
# pip install pandas scikit-learn
# Importar las librerías necesarias
import pandas as pd  # pandas: librería de Python para la manipulación y análisis de datos en estructuras tabulares
from sklearn.neighbors import NearestNeighbors  # NearestNeighbors: clase de la librería scikit-learn que implementa el algoritmo de vecinos más cercanos
# Crear un conjunto de datos de ejemplo
data = {
    'Usuario': ['Alice','Bob','jose','David'],  # Lista de nombres de usuarios
    'Producto_1': [5, 3, 0, 2],  # Preferencias (calificaciones) de los usuarios para el Producto 1
    'Producto_2': [4, 0, 2, 5],  # Preferencias (calificaciones) de los usuarios para el Producto 2
    'Producto_3': [0, 2, 5, 3]   # Preferencias (calificaciones) de los usuarios para el Producto 3
}
# Convertir el diccionario en un DataFrame (estructura de datos en forma de tabla) y establecer la columna 'Usuario' como índice (identificador único para cada fila)
df = pd.DataFrame(data).set_index('Usuario')
# Crear y entrenar el modelo de vecinos más cercanos
model = NearestNeighbors(n_neighbors=2, metric='cosine')  # n_neighbors=2: Número de vecinos más cercanos a buscar, metric='cosine': Tipo de métrica para calcular la similitud (similaridad basada en el ángulo entre vectores)
model.fit(df.values)  # Ajustar (entrenar) el modelo con los valores numéricos del DataFrame (datos de preferencias de productos)
# Buscar productos recomendados para un usuario específico
user_index = df.index.get_loc('Alice')  # Obtener el índice (posición) de 'Alice' en el DataFrame utilizando su nombre
distances, indices = model.kneighbors([df.iloc[user_index]])  # Encontrar los vecinos más cercanos al usuario 'Alice'; distances: distancias a los vecinos más cercanos, indices: índices de los vecinos en el DataFrame
# Mostrar recomendaciones
for i, (distance, index) in enumerate(zip(distances[0], indices[0])):  # Enumerar sobre las distancias y los índices de los vecinos más cercanos
    if df.index[index] != 'Alice':  # Asegurarse de que no se recomiende al mismo usuario ('Alice') como similar a sí mismo
        print(f'Recomendación del Producto {i + 1}: Usuario similar {df.index[index]} con distancia {distance:.2f}')  # Imprimir la recomendación con la distancia formateada a dos decimales