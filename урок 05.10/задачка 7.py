color1 = input().split().lower()
color2 = input().split().lower()

valid_color = ["Красный","синий","желтый"]

if color1 not in valid_color or color2 not in valid_color:
    print("Ошибка")
elif (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
    print("фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
    print("оранживый")
elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
    print("зеленый")
else:
    print(color1)