things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}


things_wight = {v: k for k, v in things.items()}
sorted(things_wight)
# print(things_wight)

N = int(input())*1000

while N > 0:
    the_whitest_thing = sorted(things_wight).pop(-1)
    print(things_wight[the_whitest_thing])
    N -= int(the_whitest_thing)
    del things_wight[the_whitest_thing]

N = float(input()) * 1000

my_lst = [(k, v) for k, v in things.items()]
my_lst.sort(key=lambda x: x[1], reverse=True)

bag = []

for thing in my_lst:
    if thing[1] <= N:
        bag.append(thing[0])
        N -= thing[1]
    else:
        continue

print(*bag)
