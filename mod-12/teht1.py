import requests

req = "https://api.chucknorris.io/jokes/random"
response = requests.get(req).json()
print(response["value"])