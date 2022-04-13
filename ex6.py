def is_simple_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n or n == 1:
        return True
    else:
        return False


def calculation_of_factorial(n):
    return calculation_of_factorial(n - 1) * n if n > 1 else 1


num = int(input())

for i in range(1, num + 1):
    if is_simple_number(i) == True:
        if i < 20:
            print(f'Найдено простое число: {i}')
            print(f'Это простое число меньше 20, его факториал равен {calculation_of_factorial(i)}')
        else:
            print(f'Найдено простое число: {i}')

    if is_perfect_number(i) == True:
        if i > 20:
            print(f'Найдено совершенное число: {i}')
            print(f'Это совершенное число болше 20, его корень равен {i**0.5}')
        else:
            print(f'Найдено совершенное число: {i}')

