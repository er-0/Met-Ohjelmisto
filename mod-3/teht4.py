#4
year = int(input("Anna vuosiluku: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Vuosi on karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")
elif year % 4 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
