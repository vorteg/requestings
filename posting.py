import requests
import json

if __name__ == "__main__":
    url = "https://httpbin.org/post"
    payload = {"test": "Probando esta cosa", "holi": "un saludo"}
    response = requests.post(url, json=payload)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)
