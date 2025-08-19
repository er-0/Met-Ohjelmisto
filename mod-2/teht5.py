#5
leiv = float(input("Anna leiviskät: "))
naul = float(input("Anna naulat: "))
luod = float(input("Anna luodit: "))

nauloja = leiv * 20 + naul
luoteja = nauloja * 32 + luod
grammoja = luoteja * 13.3
print("Massa nykymittojen mukaan:")
print(f"{int(grammoja / 1000)} kilogrammaa ja {grammoja % 1000:.2f} grammaa.")