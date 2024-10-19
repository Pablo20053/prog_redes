'''
     Nombre: Juan Pablo López Ramírez
     Descfripción: API de Productos
     Fecha: 17/10/2024
    
'''
import requests
import time

while True:
     id = input('Ingresa el ID de produco :')
     if id.lower() == 'salir' or id.lower() =='s':
          break

     url = f"https://fakestoreapi.com/products/{id}"
 
     productos = requests.get(url).json()
     print(productos)
     time.sleep(2)

