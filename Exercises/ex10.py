garden = [input().split() for i in range(int(input()))]
total_of_flowers = [int(i[1]) for i in garden]


def divisors_of_number(n):
    list_of_divisors = [i for i in range(1, n + 1) if n % i == 0]
    return list_of_divisors


lists_of_divisors = [divisors_of_number(i) for i in total_of_flowers]  # Создание списка делителей каждлго числа

a = max(lists_of_divisors)  # Список с наибольшим общим делителем

flag = False
num = 0
for i in a[-1:0:-1]:
    for j in lists_of_divisors:
        if i in j:  # если делитель в списке, продолжить
            flag = True
            continue
        else:
            num = 0
            break
    if flag:
        num = i  # наибольший общий делитель

if num == 0:
    print('error!')
else:
    total_of_string = [int(i / num) for i in total_of_flowers]  # Колличество строк одного цветка

    for i in range(len(total_of_string)):
        for j in range(total_of_string[i]):
            for k in range(num):
                print(garden[i][0][0:3], end=' ')
            print()
