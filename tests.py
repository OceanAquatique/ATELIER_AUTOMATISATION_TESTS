import requests

url = "https://coffee.alexflipnote.dev/random.json"

response = requests.get(url)

print("Status code :", response.status_code)
print("Content-Type :", response.headers.get("Content-Type"))
print("JSON :", response.json())
