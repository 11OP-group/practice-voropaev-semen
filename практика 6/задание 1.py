temperature = float(input("Введите температуру:"))
pressure = int(input("Введите давление:"))
pulse = int(input("Введите пульс:"))

if 36 <= temperature <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100:
    print("Состояние здоровье: нормальное")
elif (35 <= temperature < 36 or 37 < temperature <= 38) and \
     (105 <= pressure < 110 or 130 < pressure <= 140) and \
     (55 <= pulse < 60 or 100 < pulse <= 110):
    print("Состояние здоровья: легкое недомогание")

else:
    print("Состояние здоровье: требуется внимение врача")