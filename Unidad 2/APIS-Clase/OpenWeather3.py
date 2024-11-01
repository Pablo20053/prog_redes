''' 
    Nombre: Juan Pablo López Ramírez
    Fecha: 14/10/2024
    Actividad: 2

'''
import requests
import time
latitud= 19.4450
longitud=-99.1310
clave="121fe9334e340bd2fb462592056e1546"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data=requests.get(main_api).json()
#print(json_data)

codigo = json_data['cod']

while True:
    latitud=input("Ingresa la latitud: ")
    if latitud.lower()=="salir" or latitud.lower()=="s":
        break
    longitud=input("Ingresa la longitud: ")
    if latitud.upper()=="SALIR" or latitud.upper()=="S":
        break
    main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
    
    json_data=requests.get(main_api).json()
    codigo = json_data['cod']

    if codigo==200:
        print(f"El codigo {codigo} indica que la respuesta es correcta")
        print(f"Latitud:  {json_data["coord"]["lat"]}")
        print(f"Longitud:  {json_data["coord"]["lon"]}")
        print(f"Velocidad de viento:   {json_data["wind"]["speed"]}")      
        print(f"Temperatura:  {json_data["main"]["temp"]}")
        print(f"Humedad:  {json_data["main"]["humidity"]}")
        print(f"Clima: {json_data["weather"][0]["main"]}")        
    else:
        print(f"El codigo {codigo} indica que la respuesta es incorrecta")
        
    time.sleep(3)  
 
