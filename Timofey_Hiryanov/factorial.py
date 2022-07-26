def f(n):
    assert n >= 0, "Факториал отрицательного числа не определён"
    if n == 0:
        return 1
    return f(n - 1) * n


factorial = f(int(input()))
print(factorial)
