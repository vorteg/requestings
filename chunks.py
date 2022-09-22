from urllib import response
import requests
import json

if __name__ == "__main__":
    url = "https://i.imgur.com/Ma9uBCm.jpeg"

    response = requests.get(
        url, stream=True
    )  # Realiza la peticion sin descargar el contenido

    with open("image.jpeg", "wb") as file:
        for chunk in response.iter_content():  # Descarga el contenido poco a poco
            file.write(chunk)

    response.close()
