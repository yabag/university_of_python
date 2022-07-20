def os_psth(disk, *args, sep="\\", **kwargs):
    # print(kwargs)
    args = (disk, ) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]

    path = sep.join(args)
    return path


p = os_psth("F:", " ~stepik.prg ",
            " Добрый, добрый Python (Питон) ",
            " 39\\p39. Функции.docx ",
            sep="/")
print(p)
