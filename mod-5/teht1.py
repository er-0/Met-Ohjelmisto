import random

dice = int(input("Kuinka monta arpakuutiota? "))
end_sum = 0

for i in range(dice):
    throw = random.randint(1,6)
    end_sum += throw

print(end_sum)