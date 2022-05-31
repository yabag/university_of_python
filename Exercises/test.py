import enum


class Additive(enum.Enum):
    SUGAR = 'sugar'
    LEMON = 'lemon'
    ICE = 'ice'


    @property
    def description(self) -> str:
        descriptions = {
            self.SUGAR: 'сахар',
            self.LEMON: 'лимон',
            self.ICE: 'лёд'
        }

        description = descriptions.get(self)
        if not description:
            raise ValueError(f'Описание не заполнено для {self.value}')

        return description


class Soda:
    """Запрашивает у пользователя желаемую добавку к газировке
    и выводит получившийся напиток."""

    def __init__(self, additive: Additive | None = None):
        self.additive = additive

    def show_my_drink(self):
        if not self.additive:
            print("Обычная газировка.")
        else:
            print("Газировка и {}".format(self.additive.description))


if __name__ == "__main__":
    drink = Soda(Additive.ICE)
    drink.show_my_drink()
