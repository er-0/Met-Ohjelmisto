'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.'''
number = int(input("Anna kokonaisluku: "))
prime = True
if number < 2:
    print("Luku ei ole alkuluku.")
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")