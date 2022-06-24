s = input()
num = '0123456789'
flag = True

for i, d in enumerate(s):
    if not flag:
        flag = False
        break
    elif not s.startswith('+7('):
        flag = False
    elif (i == 6 and d == ')') or ((i == 10 or i == 13) and (d not in '-')):
        flag = False
    elif



