import random

numbers = []

for item in range(5):
    numbers.append(random.randint(1, 100))

min_index = numbers.index(min(numbers))

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print(f"Изменённый список: {numbers}")