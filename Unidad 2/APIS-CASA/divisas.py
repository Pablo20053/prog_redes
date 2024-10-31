import requests
url = "http://api.exchangeratesapi.io/v1/latest?access_key=ee3edc36f2757b78c0e2873358e8ecbc&base="

base = input("Ingresa la divisa base: ")
cant = int(input("Cantidad : "))
div = input("Divisa: ")

try:
    resp = requests.get(url + base)
    data = resp.json()
    divisas = data["rates"]
except: 
    print("Ha habido un error")
if div.upper() in divisas.keys() :
    result = divisas[div.upper()] * cant
    print(f"Total: {result}")