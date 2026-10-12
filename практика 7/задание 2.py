
import random

status = input("Введите статус заказа: ").lower().strip()

match status:
    case "pending":
        name = "В ожидании"
        description = "Заказ принят и ожидает обработки."
        emoji = "⏳"
        time = random.randint(1, 3)

    case "processing":
        name = "В обработке"
        description = "Заказ собирают и готовят к отправке."
        emoji = "⚙️"
        time = random.randint(1, 2)

    case "shipped":
        name = "Отправлено"
        description = "Заказ передан службе доставки."
        emoji = "🚚"
        time = random.randint(2, 7)

    case "delivered":
        name = "Доставлено"
        description = "Заказ успешно доставлен получателю."
        emoji = "✅"
        time = 0

    case "cancelled":
        name = "Отменено"
        description = "Заказ был отменён."
        emoji = "❌"
        time = 0

    case _:
        name = None
        print("Ошибка: неизвестный статус заказа!")

if name is not None:
    print("\n" + "=" * 35)
    print("       ОТСЛЕЖИВАНИЕ ЗАКАЗА")
    print("=" * 35)
    print(f"Статус: {emoji} {name}")
    print(f"Описание: {description}")
    print(f"Примерное время ожидания: {time} дн.")
    print("=" * 35)
