m = int(input("Введите число m:"))
n = int(input("Ведите число n (n > m):"))
for i in range(m, n + 1):
    cond1 = (i % 17 == 0)
    cond2 = (i % 10 == 9)
    cond3 = (i % 3 == 0 and i % 5 == 0)

    if cond1 or cond2 or cond3:
        print(i)

