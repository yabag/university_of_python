n = int(input())
k = [64, 32, 16, 8, 4, 2, 1]
total = []

for i in k:
    while n >= i:
        n -= i
        total.append(i)

print(*total)
