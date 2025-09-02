import random

def even_numbers(number_list):
    evens = []
    for i in number_list:
        if i % 2 == 0:
            evens.append(i)
    return evens


numbers = []
for i in range(10):
    numbers.append(random.randint(0,50))

print(numbers)
print(even_numbers(numbers))