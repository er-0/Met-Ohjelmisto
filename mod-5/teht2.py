number = float(input("Anna luku: "))
num_list = []
while number != "":
    num = float(number)
    num_list.append(num)
    number = input("Anna luku: ")
num_list.sort(reverse=True)
print(num_list[0:5])

#toimii kun annetaan ensin ainakin yksi luku ja vain lukuja tai tyhjä merkkijono