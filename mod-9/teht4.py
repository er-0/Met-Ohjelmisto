import random
from tabulate import tabulate

from car import Car


car_list = []

for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    top_speed = random.randint(100, 200)

    car = Car(reg_number, top_speed)
    car_list.append(car)


def race_hour(cars):
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
    for car in cars:
        if car.distance_traveled >= 10000:
            return True #a car (or multiple) has won the race
    return False


race_won = False
while not race_won:
    race_won = race_hour(car_list)

print(tabulate(car_list, headers=['Registration number', 'Top Speed', 'Final speed', 'Distance traveled']))