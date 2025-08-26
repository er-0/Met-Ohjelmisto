import random

points = int(input("Kuinka monella pisteellä lasketaan? "))
number = 1
insidecircle = 0

while number <= points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        insidecircle += 1
    number += 1

approx = 4 * insidecircle / points
print(approx)