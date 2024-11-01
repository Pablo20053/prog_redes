''' 
    Nombre: Juan Pablo López Ramírez
    Fecha: 14/10/2024
    Actividad: 2

'''
import requests

latitud = 20.52353
longitud = -100.8157
clave = "121fe9334e340bd2fb462592056e1546"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data = requests.get(main_api).json()
#print(json_data)
codigo = (json_data)
print(json_data["cod"])

'''
Codigo 200 = okey
codigo 401 = usuario no autorizado

'''

if codigo == 200:
    print(f" El codigo {codigo} indica que la respuesta es correcta")
else:
    print(f" El codigo {codigo} indica que algo anda mal")

  