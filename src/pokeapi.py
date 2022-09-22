from urllib import response
import requests
import json


def get_pokemons(url, offset=0):
    args = {"offset": offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        if results:
            for pokemon in results:
                name = pokemon["name"]
                print(name)

        next2 = input("Continuar listando? [Y/N]").capitalize()

        if next2 == "Y":
            get_pokemons(url, offset=offset + 20)


if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon-form/"

    get_pokemons(url)
