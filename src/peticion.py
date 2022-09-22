import requests
import json

if __name__ == "__main__":
    url = "https://httpbin.org/get"
    args = {"test": "Probando esta cosa", "holi": "un saludo"}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        content = response.content
        json_format = response.json()
        print(json_format["args"])
        # content = json.loads(response.content)
        # print(content)
