'''
Задача.

У Клэр есть n видов цветов.
Она хочет посадить цветы строго с одинаковым количеством в каждом ряду, и так, чтобы в одном ряду были цветы только одного типа.

Необходимо написать программу, которая:

 1. Получает количество видов цветов N
 2. Вводит названия N цветов и количество цветов каждого типа
 3. Выводит набор цветов в саду Клэр, который удовлетворяет её условиям (выводятся первые 3 буквы наименования) в том же порядке, что и производился ввод
 4. Если такую рассадку цветов создать нельзя, то вывести сообщение об ошибке
'''

garden = [input().split() for i in range(int(input()))]  # Создание списков, на основе вводимых данных с клавиатуры
total_of_flowers = [int(i[1]) for i in garden]


def gcd(a, b):
    '''
    Функция определения наибольшего общего делителя двух чисел.
    '''
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


for i in range(0, len(total_of_flowers) - 1):
    if i == 0:
        a = total_of_flowers[i]
        a = gcd(a, total_of_flowers[i + 1])
    else:
        a = gcd(a, total_of_flowers[i + 1])

if a == 1:
    print('error!')
else:
    total_of_string = [int(i / a) for i in total_of_flowers]

    for i in range(len(total_of_string)):    # Распечатка получившейся клумбы
        for j in range(total_of_string[i]):
            for k in range(a):
                print(garden[i][0][0:3], end=' ')
            print()
