# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

N = 3
M = 5

matrix_arr = []

for i in range(N):
    str_arr = random.sample(range(1, 100), M)
    matrix_arr.append(str_arr)
    print(str_arr)

max_min_num = 0
for i in range(M):
    min_num = matrix_arr[0][i]
    for j in range(N):
        if matrix_arr[j][i] < min_num:
            min_num = matrix_arr[j][i]
    if min_num > max_min_num:
        max_min_num = min_num
print(max_min_num)