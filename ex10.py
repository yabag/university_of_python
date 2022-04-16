garden = [input().split() for i in range(int(input()))]
total_of_flowers = [int(i[1]) for i in garden]

total_min = min(total_of_flowers)

total_string = []
flag = True
for i in range(len(total_of_flowers)):
    if total_of_flowers[i] % total_min == 0:
        string = total_of_flowers[i] / total_min
        total_string.append(string)
    else:
        flag = False

if not flag:
    print('Error: Посадка НЕВОЗМОЖНА!')
else:
    for i in range(len(total_of_flowers)):
        print(garden[i][0][:3] * total_min, sep=' ')
