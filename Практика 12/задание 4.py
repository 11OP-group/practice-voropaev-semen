import  random

marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

for i in range(5):
    marks.append(random.randint(2, 5))

conmt_fives = 0
cont_twos = 0

for item in marks:
    if item == 5:
        conmt_fives += 1
    if item == 2:
        cont_twos += 1

print(f"Список оценок: {marks}")
print(f"Количество пятерок: {conmt_fives}")
print(f"Количество двоек: {cont_twos}")
