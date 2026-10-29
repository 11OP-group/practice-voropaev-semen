count = 0

while True:
    word = input()

    if word in ("стоп", "хватит", "достаточно"):
        break

    count += 1

print(count)