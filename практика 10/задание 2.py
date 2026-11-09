a = int(input("Введите первое число: "))

while True:
    b = int(input("Введите второе число: "))

    if b > a:
        break
    else:
        print("Ошибка. Введите число больше первого")

while True:
    c = int(input("Введите третье число: "))

    if c > b:
        break
    else:
        print("Ошибка. Введите число больше второго")

print("Последовательность принята")