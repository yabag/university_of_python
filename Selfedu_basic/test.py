def is_isolate(a, b, c, d):
    if a+b+c+d > 1:
        return False
    else:
        return True


def verify(lst):
    flag = True
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[i][j] == 1:
                flag = is_isolate(lst[i][j], lst[i][j+1], lst[i+1][j], lst[i+1][j+1])
                if not flag:
                    return flag
    return flag
