# Задайте список из n чисел последовательности $(1+1/n)**n$ и выведите на экран их сумму.

import re


def DigitsMas(elem):
    result = 0
    mas = []
    mas=[round((1+1/i)**i, 5) for i in range(1, elem+1)]
    # for i in range(1, elem+1):
    #     result = result+(1+1/i)**i
    #     mas.append(round((1+1/i)**i, 5))
    for i,sum in enumerate(mas):
        result=result+sum
        print('(',i,',',sum,')',end='')
    return result


print('Введите целое число (n>0):')
n = int(input())
if (n % 1 == 0 and n > 0):
    print(f'\nСумма элемнтов последовательности = {DigitsMas(n)}')
else:
    print('введенное число не соответствует условию!')