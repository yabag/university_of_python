lst = input().split()
d = dict([[x for x in s.split('=')] for s in lst])

print(*sorted(d.items()))
# print(d)