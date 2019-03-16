"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

k = 0
array = []

for i in range(0, 10):
    array.append(random.randint(1, 20))

print(array)

maks = 0
mini = array[0]
maks_p = 0
mini_p = 0

for i in array:
    if i > maks:
        maks = i
        maks_p = k
    if i < mini:
        mini = i
        mini_p = k
    k += 1

if mini_p < maks_p:
    j = mini_p + 1
else:
    j = maks_p + 1

summ = 0
while j < maks_p:
    summ += array[j]
    j += 1

print(f"{maks} {maks_p}     {mini} {mini_p}")
print(summ)