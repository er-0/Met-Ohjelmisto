import math

def price_per_area(diameter, price):
    area = math.pi*(diameter/2)**2
    return price/area

diameter1 = float(input("Pizzan 1 halkaisija: "))
price1 = float(input("Pizzan 1 hinta: "))
diameter2 = float(input("Pizzan 2 halkaisija: "))
price2 = float(input("Pizzan 2 hinta: "))

better_value = "Pizzalla 1 on parempi yksikköhinta."
if price_per_area(diameter1, price1) > price_per_area(diameter2, price2):
    better_value = "Pizzalla 2 on parempi yksikköhinta."

print(better_value)