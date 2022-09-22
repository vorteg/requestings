import requests
import json

if __name__ == "__main__":
    url = "https://httpbin.org/post"
    payload = {"test": "Probando esta cosa", "holi": "un saludo"}
    headers = {"Content-Type": "application/json", "Access-Token": "123213231"}
    response = requests.post(url, json=payload, headers=headers)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        # print(content)
        headers_response = response.headers
        server = headers_response["Server"]
        print(server)
