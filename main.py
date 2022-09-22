import requests

if __name__ == "__main__":
    url = "https://www.google.com/"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        with open("google.html", "wb") as f:
            f.write(content)
