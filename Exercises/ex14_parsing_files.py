ru_txt = open("ru.txt")
en_txt = open("en.txt")

s_ru = ru_txt.readlines()
s_en = en_txt.readlines()
new_ru = []
new_en = []

for line in s_ru:
    if "=" in line:
        x = line.split(' = ')
        new_ru.append(x[0])

for line in s_en:
    if "=" in line:
        x = line.split(' = ')
        new_en.append(x[0])

missed_str = []
for i in range(len(new_ru)):
    if new_ru[i] not in new_en:
        missed_str.append(new_ru[i])


print("В файле en.txt нет следующих строк:")
for i, elem in enumerate(missed_str):
    print(f'{i + 1}. {elem}')


ru_txt.close()
en_txt.close()
