def word_converter_from_kir(string, reg=True, sep="-"):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

    if reg:
        string = string.lower()

    s = ""
    for c in string:
        if c == ' ':
            s += sep
        elif c in t:
            s += t[c]
        else:
            s += c

    return print(s)


s1 = input()
word_converter_from_kir(s1)
word_converter_from_kir(s1, sep='+')
