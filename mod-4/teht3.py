number = input("Anna luku: ")
if int(number):
    smallest = int(number)
    largest = int(number)
    while number!="":
        number = input("Anna luku: ")
        if number == "":
            break
        number = int(number)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    print(f"Suurin luku on {largest} ja pienin {smallest}.")

#toimii kun syötetään vain numeroita tai tyhjä merkkijono