class Car:
    pass


d = {
    "model" : "Тойота",
    "color" : "Розовый",
    "number" : "О111АА77"
}

for i in d:
    setattr(Car, i, d[i])

print(Car.__dict__["color"])