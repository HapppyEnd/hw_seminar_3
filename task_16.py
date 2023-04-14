from random import randint
"""Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
"""

count_list = int(input('Введите количество элеметнов списка: '))
number_x = int(input('Введите число, которое нужно найти: '))
count = 0
number_list = [randint(1, count_list) for i in range(count_list)]

for i in number_list:
    if number_x == i:
        count += 1
print(f'Число {number_x} встречается в списке {number_list} {count} раз.')
