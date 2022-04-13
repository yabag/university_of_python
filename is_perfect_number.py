def is_perfect_number(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n or n == 1:
        return True
    else:
        return False

n = int(input())
print(is_perfect_number(n))
