"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

import random

n = int(input("Введите нижнюю границу для целых чисел"))
m = int(input("Введите верхнюю границу для целых чисел"))

print(random.randint(n, m))

k = float(input("Введите нижнюю границу для вещественных чисел"))
l = float(input("Введите верхнюю границу для вещественных чисел"))

print(random.uniform(k, l))

a = ord(input("Введите нижнюю границу для символа"))
b = ord(input("Введите верхнюю границу для символа"))

print(chr(random.randint(a, b)))