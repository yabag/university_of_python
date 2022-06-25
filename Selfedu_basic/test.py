s = input().replace(' ', '')

x = s.replace('+', ' +').replace('-', ' -').split(' ')
total = 0

for i in x:
    i = int(i)
    total += i

print(total)
