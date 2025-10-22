from tabulate import tabulate
import random


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    # print_status, which prints out the current information of each car as a clear, formatted table.
    def print_status(self):
        print(tabulate(self.cars, headers=['Registration number', 'Top Speed', 'Final speed', 'Distance traveled']))

    # race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= 10000:
                return True  # a car (or multiple) has won the race
        return False