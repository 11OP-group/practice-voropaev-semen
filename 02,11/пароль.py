for i in range(3):
    password = input("Введите пароль:")

    if password == "admin":
        print("Доступ разрешон")
        break

else:
    print("Вход заблокирован")