import random

def list_sum(number_list):
    return sum(number_list)

numbers = []
for i in range(10):
    numbers.append(random.randint(0,50))
result = list_sum(numbers)
print(result)