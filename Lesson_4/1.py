"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit
import cProfile


# первый пример
def simple_num1(n=300):
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

print(timeit.timeit('simple_num1()', setup="from __main__ import simple_num1", number=1000))


# второй пример

number = input('Введите число: ')


def first(number):
    number = int(number)
    dec = 1
    count_even = 0
    count_odd = 0
    while number % dec != number:
        dec *= 10
        if (int((number % dec) // (dec / 10))) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


def second(number):
    number = list(number)
    count_even = len([i for i in number if int(i) % 2 == 0])
    count_odd = len([i for i in number if int(i) % 2 != 0])
    return count_even, count_odd


cProfile.run('first(number)')
cProfile.run('second(number)')