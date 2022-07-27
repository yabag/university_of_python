def counter_add(start):
    def inner():
        nonlocal start
        start += 5
        return start

    return inner()


k = int(input())
cnt = counter_add(k)
print(cnt())
