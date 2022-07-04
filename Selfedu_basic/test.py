
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

d = dict()

for n in lst_in:
    if n not in d:
        d[n] = n
        print(f'HTML-страница для адреса {d[n]}')
    else:
        print(f'Взято из кэша: HTML-страница для адреса {d[n]}')
