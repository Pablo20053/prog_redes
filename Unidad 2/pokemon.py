import requests
'''
    Api de POKEMON
    Juan Pablo López Ramírez
'''

def obtener_informacion_pokemon(pokemon):
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    json_data = requests.get(url).json()

    if json_data:
        print(f"Nombre: {json_data['name']}")
        print(f"ID de la Pokédex: {json_data['id']}")
        print(f"Altura: {json_data['height']} metros")
        print(f"Habilidades: {', '.join([habilidad['ability']['name'] for habilidad in json_data['abilities']])}")

        if 'gender' in json_data:
            print(f"Sexo: {json_data['gender']}")
        else:
            print("Sexo desconocido")

        print(f"Categoría: {json_data['species']['name']}")

        print("Movimientos:")
        for movimiento in json_data['moves']:
            print(f"- {movimiento['move']['name']}")
    else:
        print(f"No se encontró información para el Pokémon {pokemon}")

if __name__ == "__main__":
    while True:
        pokemon = input("Ingresa el nombre de un Pokémon (escribe 'salir' para terminar): ")

        if pokemon.lower() == "salir":
            break

        obtener_informacion_pokemon(pokemon)