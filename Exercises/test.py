def opening_of_file():
    filename = input('Enter a filename: ')
    with open(filename) as f:
        lst_text = f.readlines()
    f.close()

    return lst_text


def split_by_sign(lst, sign='='):
    keys_of_lst = []

    for line in lst:
        if sign not in line:
            continue
        else:
            s = line.split(sign)
            keys_of_lst.append(s[0].strip())

    return keys_of_lst


if __name__ == '__main__':
    # text = opening_of_file()
    # print(split_by_sign(text))
    print(opening_of_file())
