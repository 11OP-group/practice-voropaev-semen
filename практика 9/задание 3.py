n = int(input("Введите число:"))

coins = 0

while n > 0:
    if n >= 25:
       coins += n // 25
       n %= 25
    elif n >= 10:
       coins += n // 10
       n %= 10
    elif n >= 5:
       coins += n // 5
       n %= 5
    else:
       coins += n
       n = 0

print(coins)