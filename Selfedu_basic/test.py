cities = tuple(input().split())
if "Москва" not in cities:
    cities += 'Москва',
print(*cities)
