import random

secret = random.randint(1, 10)

for i in range(3):
    guess = int(input("Введите число:"))

    if guess == secret:
        print("Угадал!")
        break
    elif guess < secret:
        print("Больше")
    else:
        print("Меньше")
else:
    print("Загаданное число:", secret)
