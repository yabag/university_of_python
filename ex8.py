my_list = [1, -1, 3, 4, 5]
flag = False
for i in range(0, len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            flag = True
            break

print(flag)
