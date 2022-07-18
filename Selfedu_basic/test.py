import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

books = [s.split(': ') for s in lst_in]
d = {}

for book in books:
    if book[0] not in d:
        d[book[0]] = {book[1]}
    else:
        d[book[0]] |= {book[1]}
