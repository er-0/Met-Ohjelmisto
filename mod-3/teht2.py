#2
description_lux = "LUX on parvekkeellinen hytti yläkannella."
description_a = "A on ikkunallinen hytti autokannen yläpuolella."
description_b = "B on ikkunaton hytti autokannen yläpuolella."
description_c = "C on ikkunaton hytti autokannen alapuolella."
shipclass = input("Anna hyttiluokka: ").lower()

if shipclass == "lux":
    print(description_lux)
elif shipclass == "a":
    print(description_a)
elif shipclass == "b":
    print(description_b)
elif shipclass == "c":
    print(description_c)
else:
    print("Virheellinen hyttiluokka.")
