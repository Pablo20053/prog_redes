import requests

'''
Api que muestra la frase del dia 

'''

url = "https://frasedeldia.azurewebsites.net/api/phrase"

resp = requests.get(url)
datos = resp.json()
print(datos)