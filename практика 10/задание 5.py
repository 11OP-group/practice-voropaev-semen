balance = 1000

while True:
    print("\n1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")

    command = int(input("Выберите операцию: "))

    if command == 1:
        print("Ваш баланс:", balance, "руб.")
    elif command == 2:
        if balance >= 100:
            balance -= 100
            print("Снято")
        else:
            print("Недостаточно средств")
    elif command == 3:
        balance += 100
        print("100 рублей добавлено")
    elif command == 4:
        print("До свидания")
        break
    else:
        print("Неверная команда")