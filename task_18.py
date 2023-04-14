from random import randint
"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""
count_list = int(input('Введите количество элеметнов списка: '))
number_x = int(input('Введите число X: '))

number_list = [randint(0, count_list) for i in range(count_list)]
print(number_list)
min_diff = [abs(number_x-i) for i in number_list]

result = [
    number_list[i] for i in range(len(min_diff))
    if min(min_diff) == min_diff[i]]

print(f'{set(result)} самый близкий по величине элемент к числу {number_x}.')
