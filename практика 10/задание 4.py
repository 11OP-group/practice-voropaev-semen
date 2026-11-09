total = 0

while True:
    price = int(input("Введите цену товара (0 - завершить): "))

    if price == 0:
        break
    elif price < 0:
        print("Ошибка цены")
        continue
    else:
        total += price

if total > 1000:
    total = total * 0.9

print("Итоговая сумма к оплате:", total)