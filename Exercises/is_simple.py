def is_simple_number(n):
    '''
        Определяет, является ли число простым.
        n - целое положительное число.
        Если простое, то возвращает True,
        а иначе - False
    '''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input())
print(is_simple_number(n))
