'''
Функция определения наибольшего общего делителя двух чисел.
'''


def gcd(a, b):
    '''
    Функция определения наибольшего общего делителя двух чисел.
  a - целое положительное число
  b - целое положительное число
    '''
    if a < 0 or b < 0:
        raise ValueError('a and b must be greater than 0')
    return a if b == 0 else gcd(b, a % b)


def test_success_case():
    '''
    Тест успешного вызова gcd и проверка результатов.
    '''
    a = 2
    b = 4
    expected_result = 2

    result = gcd(a, b)

    assert result == expected_result


def test_error_case():
    '''
    При вызове gcd с отрицательными аргументами должны получить ValueError.
    '''

    a = -1
    b = -2
    expected_error = 'a and b must be greater than 0'
    actual_error = None

    try:
        gcd(a, b)
    except ValueError as exc:
        actual_error = exc

    assert expected_error == str(actual_error)


def run_tests():
    test_success_case()
    test_error_case()

    print('Success')


if __name__ == '__main__':
    run_tests()
