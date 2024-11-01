import requests
import json
'''
    Juan Pablo López Ramírez GIR0641

'''

def obtener_info_pais(nombre_pais):

    try:
        url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
        response = requests.get(url)
        response.raise_for_status()  # excepción si la solicitud no es exitosa

        datos_pais = response.json()[0]
        return {
            "nombre": datos_pais["name"]["common"],
            "capital": datos_pais["capital"][0],
            "poblacion": datos_pais["population"],
            "continente": datos_pais["continents"][0],
            "zona_horaria": datos_pais["timezones"][0]
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información del pais: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"La estructura de los datos esta erronea {e}")
        return None

if __name__ == "__main__":
    while True:
        opcion = input("Ingrese una opción (1: Buscar información de un país, 2: Salir): ")

        if opcion == "1":
            pais = input("Ingrese el nombre del país: ")
            info_pais = obtener_info_pais(pais)

            if info_pais:
                print(json.dumps(info_pais, indent=4))
            else:
                print("No se pudo encontro el pai")
        elif opcion == "2":
            print("Adios :))")
            break
        else:
            print("Opcion inválida. Por favor, ingrese 1 o 2.")