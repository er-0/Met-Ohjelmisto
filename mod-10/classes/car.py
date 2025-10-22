class Car:
    def __init__(self, registration_number, top_speed, current_speed = 0, distance_traveled = 0):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.distance_traveled = distance_traveled

    def __iter__(self):
        yield self.registration_number
        yield self.top_speed
        yield self.current_speed
        yield self.distance_traveled

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def drive(self, hours):
        added_distance = hours * self.current_speed
        self.distance_traveled += added_distance

