my_list = [int(i) for i in input()]
print(my_list)
averege = sum(my_list)/len(my_list)

for i in range(len(my_list)):
    if my_list[i] > averege:
        print(my_list[i])
