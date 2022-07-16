lst_nums = input().split()

d = {k: v for k, v in enumerate(lst_nums[1:], int(lst_nums[0]))}
print(d[4])
