import requests
import json
'''
    Nombre: Juan Pablo López Ramírez
    Fecha: 31/10/2024
    Descripción : Ejercicio 3 practic0 unidad 2

'''
def menu():
    
    print(" ********** Menu de Consultas de Futbol **********")
    print("1. Consultar un equipo")
    print("2. Consultar un jugador")
    print("3. Lista de ligas")
    print("4. Consultar liga por id")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Ingresa una opción valida")
        except ValueError:
            print("ingresa un numero")

def consultar_equipo(equipo):
    #Funcion para consultar un equipo
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={equipo}"
    response = requests.get(url)
    data = json.loads(response.text)

    if 'teams' in data:
        for team in data['teams']:
            print(f"Nombre del equipo: {team['strTeam']}")
            print(f"Liga: {team['strLeague']}")
            print(f"Descripción: {team['strDescriptionEN']}")
            print(f"Página oficial: {team['strWebsite']}")
            print(f"Estadio: {team['strStadium']}")
    else:
        print("Equipo no encontrado.")

def consultar_jugador(jugador):
    
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={jugador}"
    response = requests.get(url)
    data = json.loads(response.text)

    if 'player' in data:
        for player in data['player']:
            print(f"Nombre completo: {player['strPlayer']}")
            print(f"Nacionalidad: {player['strNationality']}")
            print(f"Equipo: {player['strTeam']}")
            print(f"Lugar de nacimiento: {player['strBirthLocation']}")
            print(f"Facebook: {player['strFacebook']}")
            print(f"Altura: {player['strHeight']}")
            print(f"Peso: {player['strWeight']}")
    else:
        print("Jugador no encontrado.")

def listar_ligas():
    #uncion para listar todas las ligas
    url = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
    response = requests.get(url)
    data = json.loads(response.text)

    if 'leagues' in data:
        for league in data['leagues']:
            print(f"ID: {league['idLeague']}")
            print(f"Nombre: {league['strLeague']}")
    else:
        print("No se encontraron ligas")

def consultar_liga(id_liga):
    
    url = f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={id_liga}"
    response = requests.get(url)
    data = json.loads(response.text)

    if 'leagues' in data:
        for league in data['leagues']:
            print(f"Nombre: {league['strLeague']}")

    else:
        print("Liga no encontrada.")

if __name__ == "__main__":
    while True:
        opcion = menu()

        if opcion == 1:
            equipo = input("Ingrese el nombre del equipo: ")
            consultar_equipo(equipo)
        elif opcion == 2:
            jugador = input("Ingrese el nombre del jugador: ")
            consultar_jugador(jugador)
        elif opcion == 3:
            listar_ligas()
        elif opcion == 4:
            id_liga = input("Ingrese el ID de la liga: ")
            consultar_liga(id_liga)
        elif opcion == 5:
            print("Bye :))")
            break