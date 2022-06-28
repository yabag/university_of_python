N = int(input())

lst = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
print(lst)