airports = {}
task = ""

while task != "3":
    task = input("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman (2) vai lopettaa (3)? ")
    if task == "1":
        airport_code = input("Anna ICAO-koodi: ")
        airport_name = input("Anna kentän nimi: ")
        airports[airport_code] = airport_name
    if task == "2":
        airport_code = input("Anna ICAO-koodi: ")
        if airport_code in airports:
            print(f"Kentän nimi on {airports[airport_code]}")
        else:
            print("Ei löytynyt.")