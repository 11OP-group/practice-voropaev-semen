points = int(input("Введите количество баллов:"))

if points >= 90:
    print("Оценка: 5 (отлично)")
elif points >= 75 and points < 90:
    print("Оченка: 4 (хорошо)")
elif points >= 60 and points < 75:
    print("Оченка: 3 (удовлетворительно)")
else:
    print("Оценка:(неудовлетворительно)")

print("Результат записан")