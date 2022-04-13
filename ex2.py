n = int(input())

for i in range(0, n):
    for j in range(0, n):
        if i == j or n - 1 - i == j:
            print(1, end=' ')
        else:
            print('-', end=' ')
    print()
