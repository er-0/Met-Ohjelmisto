import random

from classes.car import Car
from classes.race import Race

car_list = []

for i in range(1, 11):
    reg_number = "ABC-" + str(i)
    top_speed = random.randint(100, 200)

    car = Car(reg_number, top_speed)
    car_list.append(car)

derby = Race("Grand Demolition Derby", 8000, car_list)

race_finished = False
hours = 0
while not race_finished:
    derby.hour_passes()
    hours += 1
    race_finished = derby.race_finished()
    if hours % 10 == 0 or race_finished:
        print(f"\nStatus after {hours} hours:")
        derby.print_status()
