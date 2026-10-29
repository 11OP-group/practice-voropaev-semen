import random

secret = random.randint(1, 100)
attempts = 0

print("Угадай число от 1 до 100!")

while True:
    guess = int(input("Введи число: "))
    attempts += 1

    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")
    else:
        print("Поздравляю! Ты угадал число!")
        print("Количество попыток:", attempts)
        break