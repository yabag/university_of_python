import enum


class Options(enum.Enum):
    Nothing = 0
    CocaCola = 1
    Sprite = 2
    Fanta = 3


class Soda:
    """Запрашивает у пользователя желаемую добавку к газировке
    и выводит получившийся напиток."""

    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):

        if self.additive == Options.Nothing.value:
            print("Обычная газировка.")
        else:
            print("Газировка и {}".format(self.additive))


if __name__ == "__main__":
    drink = Soda(int(input("Введите желаемую добавку к газировке: ")))
    drink.show_my_drink()
