import requests

from api_key import OPENWEATHER_API_KEY

municipality = input("Anna kunnan nimi: ")

#löytää vain openweathermapin ykköstuloksen:
req = f"http://api.openweathermap.org/geo/1.0/direct?q={municipality}&limit=1&appid={OPENWEATHER_API_KEY}"

try:
    response = requests.get(req)
    if response.status_code==200:
        try:
            res = response.json()[0]
            lat = (res["lat"])
            lon = (res["lon"])
            req_weather = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon="
                           f"{lon}&lang=fi&units=metric&appid="
                           f"{OPENWEATHER_API_KEY}")
            print(f"Sää paikassa {municipality}, {res['country']}:")
            try:
                response = requests.get(req_weather)
                if response.status_code == 200:
                    json_response = response.json()
                    print(json_response["weather"][0]["description"])
                    print(json_response["main"]["temp"], "astetta")
            except requests.exceptions.RequestException as e:
                print("Säähakua ei voitu suorittaa.")
        except IndexError:
            print("Kuntaa ei löytynyt.")
except requests.exceptions.RequestException as e:
    print ("Kuntahakua ei voitu suorittaa.")

