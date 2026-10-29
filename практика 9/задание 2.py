count = 0
found = False

while True:
    name = input("Введите имена:")

    if name == "Александра":
        found = True
    elif name == "Левон":
        break
    elif found:
        count += 1

print(count)