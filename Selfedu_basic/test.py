import time


def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a и b
    по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a

def test_nod(func):
    # --- тест №1 ---------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#tets1 - ok")
    else:
        print("#test1 - fail")

    # --- тест №2 ---------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#tets2 - ok")
    else:
        print("#test2 - fail")

    # --- тест №3 ---------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#tets3 - ok")
    else:
        print("#test3 - fail")


test_nod(get_nod)
