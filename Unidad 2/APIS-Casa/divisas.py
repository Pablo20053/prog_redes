import requests
import json
'''
    Juan Pablo López Ramírez GIR0641

'''
def convertir_divisa():
  """Convierte una cantidad de una divisa a otra utilizando la API de exchangeratesapi.io."""

  while True:
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=ee3edc36f2757b78c0e2873358e8ecbc&base="

    # Obtener la divisa base y la cantidad a convertir
    base = input("Ingresa la divisa base (escribe 'salir' para terminar): ")
    if base.lower() == "salir":
      print("Adios :)")
      break

    cantidad = float(input("Cantidad a convertir: "))
    divisa_destino = input("Divisa a la que deseas convertir: ")

    try:
      response = requests.get(url + base)
      response.raise_for_status()  #  excepción si el estado HTTP no es exitoso
      data = response.json()

      # Verificar la clave "rates" y si la divisa destino existe
      if 'rates' not in data:
        print("La API no proporcionó los datos de las tasas de cambio.")
        continue
      if divisa_destino.upper() not in data['rates']:
        print(f"La divisa '{divisa_destino}' no está disponible.")
        continue

      #  conversión
      tasa_cambio = data['rates'][divisa_destino.upper()]
      resultado = cantidad * tasa_cambio
      print(f"{cantidad} {base} equivalen a {resultado} {divisa_destino}")

    except requests.exceptions.RequestException as e:
      print(f"Error en la solicitud: {e}")
    except json.JSONDecodeError as e:
      print(f"Error al decodificar la respuesta JSON: {e}")
    except ValueError:
      print("ingresa un número válido para la cantidad ")

if __name__ == "__main__":
  convertir_divisa()