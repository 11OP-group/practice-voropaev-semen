word = input("Введите слово: ")

letters = list(word)

reverse_letters = letters[::-1]

if letters == reverse_letters:
 print("Это палиндром")
else:
 print("Не палиндром")