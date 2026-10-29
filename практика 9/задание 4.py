n = int(input("Введите число:"))

count3 = 0
last_digit = n % 10
even_count = 0
sum_greater5 = 0
product_greater7 = 1
count05 = 0

while n > 0:
    digit = n % 10

    if digit == 3:
        count3 += 1

    if digit % 2 == 0:
        even_count += 1

    if digit > 5:
        sum_greater5 += digit

    if digit > 7:
        product_greater7 *= digit

    if digit == 0 or digit == 5:
        count05 += 1

    n //= 10

print(count3)
print(last_digit)
print(even_count)
print(sum_greater5)
print(product_greater7)
print(count05)