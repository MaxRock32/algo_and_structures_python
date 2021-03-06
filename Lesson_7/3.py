"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint

number = int(input("Введите натуральное число: "))
data = [randint(-number, number) for _ in range(number * 2 + 1)]


def median(data):
    data = sorted(data)
    i = 0
    a = 0
    b = 0
    if len(data) % 2 != 0:
        return data[len(data) // 2]
    else:
        a = len(data) // 2 - 1
        b = len(data) // 2
        i = (data[a] + data[b]) / 2
        return i

print(f"Исходный массив:\t{data}")
print(f"Медиана:\t\t\t{median(data)}")