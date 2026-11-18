n = int(input("Ввведите число:"))

numbers_list = []

for item in range(1, n + 1):
    if item % 2 != 0:
        numbers_list.append(item)

print(f"Список ненчетных чисел: {numbers_list}")
