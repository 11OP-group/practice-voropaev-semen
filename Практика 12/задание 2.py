prices = [1500, 500, 2000, 3500, 1000, 4500]

print(f"Самый дорогой товар: {max(prices)}")

print(f"Самый дешевый товар: {min(prices)}")

total = sum(prices)
print(f"Общая стоимость: {total}")

average = total / len(prices)
print(f" Средняя цена: {average:.2f}")