n = int(input())
my_list = [['-'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            my_list[i][j] = '1'

    for j in range(n - 1, -1, -1):
        if i == (n - 1 - j):
            my_list[i][j] = '1'
        print(my_list[i][j], end=' ')
    print()
