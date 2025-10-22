from .elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = self.create_elevators(number_of_elevators)

    def create_elevators(self, number):
        elev_list = []
        for i in range(number):
            elev_list.append(Elevator(self.bottom_floor, self.top_floor))
        return elev_list

    def run_elevator(self, elevator_id, destination_floor):
        dest = self.elevators[elevator_id]
        dest.go_to_floor(destination_floor)
        print(vars(dest))

    def fire_alarm(self):
        for elev in range(self.number_of_elevators):
            self.run_elevator(elev, self.bottom_floor)