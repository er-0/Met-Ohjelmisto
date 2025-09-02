import random

def throw():
    return random.randint(1,6)

keep_throwing = True
while keep_throwing:
    number = throw()
    if number == 6:
        keep_throwing = False
    print(number)
