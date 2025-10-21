from car import Car

car = Car("ABC-123", 142, 60,2000)
car.drive(1.5)
print(f"Ajettu matka on {int(car.distance_traveled)} kilometriä.")