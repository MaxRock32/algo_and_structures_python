"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def get_help():
    print('\nСправка по операциям:')
    print('"0" - выход из программы')
    print('"+"- сложить числа')
    print('"-" - вычесть из числа 1 число 2')
    print('"*" - умножить числа')
    print('"/" - разделить число 1 на число 2. Число 2 != 0\n')


while True:
    get_help()
    opperation = input('Введите операцию которую выполнить:')
    if opperation == '0':
        break
    else:
        num1 = float(input('Введите число 1:'))
        num2 = float(input('Введите число 2:'))
        if opperation == '+':
            print('Сумма чисел = ', num1 + num2)
        elif opperation == '-':
            print('Разность чисел = ', num1 - num2)
        elif opperation == '*':
            print('Произведение чисел = ', num1 * num2)
        elif opperation == '/':
            if num2 != 0:
                print('Результат деления чисел =', num1 / num2)
            else:
                print('На ноль делить нельзя!')
        else:
            print('Вы выбрали непонятный знак операции!')