import random

def throw(sides):
    return random.randint(1,sides)

sides = int(input("Kuinka monta tahkoa nopalla on? "))
keep_throwing = True
while keep_throwing:
    number = throw(sides)
    if number == sides:
        keep_throwing = False
    print(number)
