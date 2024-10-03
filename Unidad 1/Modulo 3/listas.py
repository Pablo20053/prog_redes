nombres = []
nombres.append('pablo')
nombres.insert(0, 'rafael')
nombres.insert(1, 'salma')
nombres_mayusculas = [nombre.upper() for nombre in nombres]
print(nombres_mayusculas)
nombres_mayusculas = sorted([nombre.upper() for nombre in nombres], reverse=True)
nombres_ordenados = sorted([nombre.upper() for nombre in nombres])
print(nombres_ordenados)
for nombre in nombres_ordenados:
  print(nombre)
  
nombres.pop(1)  # Elimina el elemento en el índice 1 (salma)
print(nombres)