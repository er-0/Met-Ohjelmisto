#3
sex = input("Anna biologinen sukupuoli: ")
hemoglobin = float(input("Anna hemoglobiiniarvo (g/l): "))

low = "Hemoglobiiniarvo on matala."
normal = "Hemoglobiiniarvo on normaali."
high = "Hemoglobiiniarvo on korkea."

if sex == "nainen":
    if hemoglobin < 117:
        print(low)
    elif hemoglobin > 175:
        print(high)
    else:
        print(normal)

if sex == "mies":
    if hemoglobin < 134:
        print(low)
    elif hemoglobin > 195:
        print(high)
    else:
        print(normal)
