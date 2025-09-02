def converter(gallons):
    print(gallons*3.785)

gallons = float(input("Kuinka monta gallonaa? "))

while gallons >= 0:
    converter(gallons)
    gallons = float(input("Kuinka monta gallonaa? "))