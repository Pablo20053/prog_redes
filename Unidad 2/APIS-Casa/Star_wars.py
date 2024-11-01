import requests
'''
    API de Star Wars 
    Juan Pablo López Ramírez GIR0641

'''
def obtener_datos(endpoint):
    response = requests.get(f"https://www.swapi.tech/api/{endpoint}")
    data = response.json()
    return data['results']

def listar_elementos(elementos, tipo):
    for elemento in elementos:
        print(f"Nombre: {elemento['name']}")
        print(f"URL: {elemento['url']}")
        print("=" * 20) # Para que se vea bonito los elementos

def menu():
    while True:
        print("Menú:")
        print("1. Listar personajes")
        print("2. Listar planetas")
        print("3. Listar vehículos")
        print("4. Salir")

        print("******* Bienvenido al mundo de Star Wars ********")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            personajes = obtener_datos("people")
            listar_elementos(personajes, "Personajes")
        elif opcion == "2":
            planetas = obtener_datos("planets")
            listar_elementos(planetas, "Planetas")
        elif opcion == "3":
            vehiculos = obtener_datos("vehicles")
            listar_elementos(vehiculos, "Vehículos")
        elif opcion == "4":
            print("Adios :)")
            break
        else:
            print("ingresa una opción valida")

if __name__ == "__main__":
    menu()
