# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input("Введите трёхзначное число: "))
print("Сумма цифр введённого числа: %d" % (num // 100 + num // 10 % 10 + num % 10))
print("Произведение цифр введённого числа: %d" % ((num // 100) * (num // 10 % 10) * (num % 10)))