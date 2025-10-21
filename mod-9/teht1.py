from car import Car

car = Car("ABC-123", 142)
print(f"Rekisteritunnus {car.registration_number}, huippunopeus {car.top_speed} km/h, tämänhetkinen nopeus "
      f"{car.current_speed} km/h, kuljettu matka {car.distance_traveled} km.")