import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

add_in_menu = {k: v for k, v in [s.split('=') for s in lst_in]}

menu.update(add_in_menu)

print(**menu)
