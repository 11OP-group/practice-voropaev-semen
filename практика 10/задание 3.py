maximum = 0

while True:
    number = int(input("Введите натуральное число (0 - выход): "))

    if number == 0:
        break
    elif number > maximum:
        maximum = number
    else:
        continue

print("Самое большое число:", maximum)