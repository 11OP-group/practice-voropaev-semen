numbers = [10, 20, 30, 40, 50]

search_number = int(input("Введите число: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search_number:
        print(f"Индекс числа: {i}")
        found = True
        break

if not found:
  print("Нет такого числа")