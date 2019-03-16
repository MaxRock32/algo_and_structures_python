"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


N = 5
M = 4
matrix_arr = []

for i in range(M):
    user_arr = []
    user_sum = 0
    for j in range(N - 1):
        user_num = int(input('Введите число: '))
        user_arr.append(user_num)
        user_sum += user_num
        print(user_num, end=' ')
    user_arr.append(user_sum)
    print(user_sum)
    matrix_arr.append(user_arr)
print(matrix_arr)