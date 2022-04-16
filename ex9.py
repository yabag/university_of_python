my_list = '004730474730000047738300000007374730747'
count1 = 0
count2 = 0

for x in my_list:
    if x == '0':
        count1 += 1
    elif count2 < count1:
            count2 = count1
            count1 = 0
print(count2)
