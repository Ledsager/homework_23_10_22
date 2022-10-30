# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def input_mas():
    mas = []
    # mas = [int(i) for i in input().split()]
    mas = list(map(int, input().split()))
    return mas


def sum_test(op, a, b):
    return op(a, b)


def summa_even_element(list_a):
    sum = 0
    # for i in range(0, len(list_a)-1):
    #     if ((i+1) % 2) == 0:
    #         sum = sum + int(list_a[i])
    #         print(list_a)
    list_b=[list_a[i] for i in range(len(list_a)) if ((i+1) % 2) == 0]
    for i in range(len(list_b)):
        sum = sum_test(lambda x, y: x+y, sum, int(list_b[i])) # попытка использования lambda

    return sum


print('Введите массив переменных : ')
list_a = input_mas()
print(list_a)
print(f'Сумма элементов на нечетных позициях = {summa_even_element(list_a)} ')
