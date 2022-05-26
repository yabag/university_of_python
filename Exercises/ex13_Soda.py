import enum


class Options(enum.Enum):
    Nothing = 'nothing'
    Others = ['CocaCola', 'Sprite', 'Fanta']


class Soda:
    """Запрашивает у пользователя желаемую добавку к газировке
    и выводит получившийся напиток."""

    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):

        if self.additive == Options.Nothing.value:
            print("Обычная газировка.")
        elif self.additive in Options.Others.value:
            print("Газировка и {}".format(self.additive))
        else:
            raise "Error"


if __name__ == "__main__":
    drink = Soda(input("Введите желаемую добавку к газировке: "))
    drink.show_my_drink()
