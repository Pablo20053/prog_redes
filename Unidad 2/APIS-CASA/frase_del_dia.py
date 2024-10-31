import requests

url = "https://frasedeldia.azurewebsites.net/api/phrase"

try:
    resp = requests.get(url)
    resp.raise_for_status()  # Levanta una excepción si la solicitud no fue exitosa
    datos = resp.json()

    frase = datos.get("frase", "No se pudo obtener la frase")
    autor = datos.get("autor", "Desconocido")

    print(f"Frase del día: '{frase}' - {autor}")
except requests.exceptions.RequestException as e:
    print(f"Error al obtener la frase: {e}")