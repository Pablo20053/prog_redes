''' 
    Nombre: Juan Pablo López Ramírez
    Fecha: 14/10/2024
    Actividad: 1

'''
import requests

latitud = 20.40
longitud = 103.20
clave = "121fe9334e340bd2fb462592056e1546"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data = requests.get(main_api).json()
print(json_data)
print(json_data["name"])