import enum


class Options(enum.Enum):
    nothing = 0
    cola = 1
    fanta = 2
    sprite = 3


class Soda:
    """Запрашивает у пользователя желаемую добавку к газировке
    и выводит получившийся напиток."""

    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        if self.additive == '0':
            print("Обычная газировка.")
        else:
            print("Газировка и {}".format(self.additive))


if __name__ == "__main__":
    drink = Soda(input("Введите желаемую добавку к газировке или 0 если хотите получить 'обычную газироку': "))
    drink.show_my_drink()
