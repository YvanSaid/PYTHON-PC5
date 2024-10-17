
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

file_path = '/mnt/data/0.txt' 
columns = ['VideoID', 'Usuario', 'Edad', 'Categoria', 'Duracion', 'Views', 'Rate', 'Likes', 'Dislikes']
data = pd.read_csv(file_path, sep='\t', names=columns)

filtered_data = data[['VideoID', 'Edad', 'Categoria', 'Views', 'Rate']]

categorias_seleccionadas = ['Sports', 'Film & Animation', 'Music']
filtered_data = filtered_data[filtered_data['Categoria'].isin(categorias_seleccionadas)]

client = MongoClient("mongodb://localhost:27017/")
db = client['youtube_db']
collection = db['videos']

collection.insert_many(filtered_data.to_dict('records'))

categoria_counts = filtered_data['Categoria'].value_counts()
plt.figure(figsize=(10, 6))
categoria_counts.plot(kind='bar')
plt.title('Número de videos por categoría')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de videos')
plt.show()

categoria_views = filtered_data.groupby('Categoria')['Views'].mean()
plt.figure(figsize=(10, 6))
categoria_views.plot(kind='bar', color='orange')
plt.title('Promedio de vistas por categoría')
plt.xlabel('Categoría')
plt.ylabel('Promedio de vistas')
plt.show()

print("Los datos han sido exportados a MongoDB en la base de datos 'youtube_db', colección 'videos'.")
print("Asegúrate de configurar MongoDB para acceso externo si deseas compartir un enlace directo.")
