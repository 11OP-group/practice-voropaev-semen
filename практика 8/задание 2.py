all_even = True

for i in range(10):
    n = int(input("Введите числа:"))
    if n % 2 != 0:
        all_even = False

if all_even:
    print("YES")
else:
    print("NO")