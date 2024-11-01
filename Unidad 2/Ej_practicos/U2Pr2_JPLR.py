import requests
'''
    Nombre: Juan Pablo López Ramírez
    Fecha: 31/10/2024
    Descripción : Ejercicio 2 practic0 unidad 2
    Termine el 2

'''
#Funcion Linea
def linea(simbolo, longitud):
    for _ in range(longitud):
        print(simbolo, end="")
    print()

#Funcion para buscar libros por titulos
def buscar_libro(titulo):
    url = f"https://openlibrary.org/search.json?title={titulo}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['docs']
    else:
        print("Error en la solicitud")
        return []

if __name__ == "__main__":
    linea("#", 20)
    print("Bienvenido a Open Library")
    linea("#", 20)

    while True:
        titulo = input("Ingrese el título del libro (o 'salir' para terminar): ")
        if titulo.lower() == 'salir':
            break

        resultados = buscar_libro(titulo)

        if resultados:
            #Imprimir todos los libros que coincidan
            for libro in resultados:
                print(f"Título: {libro['title']}")
                print(f"Autor: {libro['author_name'][0]}") 
                print(f"Enlace: https://openlibrary.org{libro['key']}")
                linea("*", 20)
        else:
            print("No se encontraron resultados.")