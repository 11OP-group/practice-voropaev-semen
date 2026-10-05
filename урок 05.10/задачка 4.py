a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равностороний")
elif a == b or b == c or a == c:
    print("Равнлбедренный")
else:
    print("Разностороний")


