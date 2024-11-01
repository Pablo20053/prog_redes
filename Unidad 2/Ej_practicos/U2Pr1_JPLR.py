'''
    Termine el 1

'''
import requests

def buscar_programa_por_nombre(nombre):

    url = f"https://api.tvmaze.com/search/shows?q={nombre}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]['show'] if data else None
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error al buscar el programa: {e}")
        return None

def buscar_programas_por_genero(genero):
    url = f"https://api.tvmaze.com/search/shows?q={genero}"
    try:
        response = requests.get(url)
        data = response.json()
        return [programa['show'] for programa in data] if data else []
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error al buscar programas por género: {e}")
        return []

def mostrar_detalles_programa(programa):
    
    print(f"Nombre: {programa['name']}")
    print(f"Resumen: {programa['summary']}")
    print(f"Género: {', '.join(programa['genres'])}")
    print(f"País: {programa['network']['country']['name'] if programa['network'] and programa['network'].get('country') else 'Desconocido'}")

def menu():
    """ menu para el usuario"""
    while True:
        print("\nMenú:")
        print("1. Buscar peli por nombre")
        print("2. Buscar pelis por género")
        print("3. Salir")
        opcion = input("introduce una opción: ")

        if opcion == '1':
            nombre = input("ingrese el nombre de la peli: ")
            programa = buscar_programa_por_nombre(nombre)
            if programa:
                mostrar_detalles_programa(programa)
            else:
                print("no se encontró la peli")

        elif opcion == '2':
            genero = input("ingrese el genero: ")
            programas = buscar_programas_por_genero(genero)
            if programas:
                print(f"Programas del género {genero}:")
                for programa in programas:
                    mostrar_detalles_programa(programa)
            else:
                print("No se encontraron programas de ese género.")

        elif opcion == '3':
            print("Adios")
            break

        else:
            print("Ingresa otra opción")

if __name__ == "__main__":
    menu()
    
