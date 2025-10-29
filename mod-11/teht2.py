from classes.car import Car

class ElectricCar(Car):
    def __init__(self, registration_number, top_speed, battery_capacity_kwh):
        super().__init__(registration_number, top_speed)
        self.battery_capacity_kwh = battery_capacity_kwh

class GasolineCar(Car):
    def __init__(self, registration_number, top_speed, tank_volume_liters):
        super().__init__(registration_number, top_speed)
        self.tank_volume_liters = tank_volume_liters

electric = ElectricCar("ABC-15", 180, 52.5)
gas = GasolineCar("ACD-123", 165, 32.3)

electric.accelerate(170)
gas.accelerate(150)

for car in (electric, gas):
    car.drive(3)
    print(car.distance_traveled)


