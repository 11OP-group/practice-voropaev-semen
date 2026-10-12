
# Цены напитков
COFFEE = 3.50
TEA = 2.00
JUICE = 2.50
LEMONADE = 3.00
WATER = 1.00

# Вывод меню
print("===== МЕНЮ КАФЕ =====")
print("1. Кофе — 3.50 €")
print("2. Чай — 2.00 €")
print("3. Сок — 2.50 €")
print("4. Лимонад — 3.00 €")
print("5. Вода — 1.00 €")

choice = input("Выберите напиток (номер или название): ").lower().strip()

match choice:
    case "1" | "кофе":
        drink = "Кофе"
        price = COFFEE
    case "2" | "чай":
        drink = "Чай"
        price = TEA
    case "3" | "сок":
        drink = "Сок"
        price = JUICE
    case "4" | "лимонад":
        drink = "Лимонад"
        price = LEMONADE
    case "5" | "вода":
        drink = "Вода"
        price = WATER
    case _:
        print("Ошибка: такого напитка нет в меню!")
        exit()

try:
    quantity = int(input("Введите количество порций: "))

    if quantity <= 0:
        print("Ошибка: количество должно быть больше нуля!")
        exit()

    code = input("Введите код скидки (или нажмите Enter): ").upper().strip()

    total = price * quantity
    discount = 0

    if code == "CAFE10":
        discount = total * 0.10
    elif code != "":
        print("Промокод не найден. Скидка не применяется.")

    final_total = total - discount

    if quantity % 10 == 1 and quantity % 100 != 11:
        portion_word = "порция"
    elif 2 <= quantity % 10 <= 4 and not 12 <= quantity % 100 <= 14:
        portion_word = "порции"
    else:
        portion_word = "порций"

    print("\n" + "=" * 30)
    print("       КВИТАНЦИЯ КАФЕ")
    print("=" * 30)
    print(f"Напиток: {drink}")
    print(f"Цена за порцию: {price:.2f} €")
    print(f"Количество: {quantity} {portion_word}")
    print(f"Сумма: {total:.2f} €")
    print(f"Скидка: {discount:.2f} €")
    print(f"К оплате: {final_total:.2f} €")
    print("=" * 30)

except ValueError:
    print("Ошибка: введите количество целым числом!")
3