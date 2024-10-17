import pandas as pd

# CSV
df_airbnb = pd.read_csv('/mnt/data/airbnb.csv')

def buscar_alojamiento(vecindario=None, precio_max=None, capacidad_min=None):
    filtrado = df_airbnb
    
    if vecindario:
        filtrado = filtrado[filtrado['neighborhood'].str.contains(vecindario, case=False)]
    
    if precio_max:
        filtrado = filtrado[filtrado['price'] <= precio_max]
    
    if capacidad_min:
        filtrado = filtrado[filtrado['accommodates'] >= capacidad_min]
    
    return filtrado

resultado = buscar_alojamiento(vecindario='Belém', precio_max=60, capacidad_min=2)
print(resultado)
