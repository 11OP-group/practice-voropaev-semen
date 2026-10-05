age = int(input("Введите возраст:"))
has_document = input("Если ли у вас документы? (да/нет):").split().lower()
is_member = input("Вы член клуба? (да/нет) :").split().lower()

if is_member == "да" or (has_document == "да" and age > 18):
    print("Добро пожаловать в клуб!")
else:
    print("Вход воспрещен")