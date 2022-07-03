import shlex
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список lst_in)

lst = [s.split() for s in lst_in]
print(lst)
d = {k: [] for k in [lst[i][1] for i in range(len(lst))]}
for k,v in lst:

print(d)
