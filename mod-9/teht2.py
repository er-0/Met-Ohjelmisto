from car import Car

car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(car.current_speed, "km/h")
car.accelerate(-200)
print(car.current_speed, "km/h")