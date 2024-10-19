'''
     Nombre: Juan Pablo López Ramírez
     Descfripción: API de Productos
     Fecha: 17/10/2024
    
'''
import requests

url = "https://fakestoreapi.com/products"
 
productos = requests.get(url)

for prod in productos.json():
    print(prod["title"] ,  "\t" ,prod["price"])

