"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import math
import timeit
import cProfile


def f3(n):
    # простой перебор
    N = n * 4
    lst = list(range(2, N))
    lst2 = []
    while True:
        for i in lst:
            check = True
            for j in lst:
                if i == j:
                    break
                elif i % j == 0:
                    check = False
                    break
            if check:
                lst2.append(i)
        if len(lst2) > n - 1:
            return lst2[n - 1]
        else:
            N += n
            lst = list(range(2, N))
            lst2 = []

def f2(n):
    # алгоритм «Решето Эратосфена»
    N = n * 4
    lst = list(range(N))
    lst[1] = 0
    m = 2
    while True:
        if lst[m] != 0:
            j = m ** 2
            while j < N:
                lst[j] = 0
                j += m
        m += 1
        if m >= math.sqrt(N):
            lst = [i for i in lst if i != 0]
            if len(lst) > n - 1:
                return lst[n - 1]
            else:
                m = 2
                N += n
                lst = list(range(N))
                lst[1] = 0


print("Время выполнения поиска простых чисел(1000 повторней):  ")
for i in range(1, 101, 9):
    print(f"Поиск простого числа № {i}")
    print(f"Время поиска без использования «Решета Эратосфена» - "
          f"{round(timeit.timeit('f3(i)', setup='from __main__ import f3, i', number=1000), 4)} с.")
    print(f"Время поиска c использованием  «Решета Эратосфена» - "
          f"{round(timeit.timeit('f2(i)', setup='from __main__ import f2, i', number=1000), 4)} с.")