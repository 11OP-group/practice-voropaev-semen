count = 0

while True:
    n = int(input())

    if n % 7 != 0:
        break

    count += 1

print(count)