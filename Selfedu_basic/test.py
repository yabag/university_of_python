s = input()
link = '+7(xxx)xxx-xx-xx'
flag = True

for i, l in enumerate(s):
    if l == link[i]:
        continue
    elif l.isdigit() and 'x' == link[i]:
        continue
    else:
        flag = False
        break

print("ДА" if flag else "НЕТ")
