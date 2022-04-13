def factorize_number(n):
    '''
        Раскладывает число на множители.
        Печатает их на экран.
        n - целое положительное число.
    '''

    divisor = 2
    while n > 1:
        if n % divisor == 0:
            print(divisor)
            n //= divisor
        else:
            divisor += 1


n = int(input())
factorize_number(n)
