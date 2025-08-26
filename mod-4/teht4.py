import random

goal = random.randint(1,10)
guess = ''
while guess != goal:
    guess = int(input("Arvaa numero väliltä 1-10: "))
    if guess > goal:
        print("Liian suuri arvaus.")
    elif guess < goal:
        print("Liian pieni arvaus.")
    elif guess == goal:
        print("Oikein!")

#toimii kun syötetään numero
