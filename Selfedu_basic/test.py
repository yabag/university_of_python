def over_six(s):
    return len(s) > 5


cities = input().split()

lst = [city for city in cities if over_six(city)]

print(*lst)
