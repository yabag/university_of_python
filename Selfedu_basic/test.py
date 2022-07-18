def is_even(num):
    return num % 2 == 0


n = int(input())
while n != 1:
    if is_even(n):
        print(n)
    else:
        continue
    n = int(input())
