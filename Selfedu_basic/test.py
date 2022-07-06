import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
d = dict.fromkeys(lst_in)

d_items = dict([[k, v] for k, v in [s.split() for s in lst_in]])

for item in d_items:
    d.setdefault()

print(d)