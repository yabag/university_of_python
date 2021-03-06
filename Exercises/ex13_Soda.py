from __future__ import annotations

import enum


class Options(enum.Enum):
    Cola = 'cocacola'
    Sprite = 'sprite'
    Fanta = 'fanta'

    @property
    def description(self) -> str:
        descriptions = {
            self.Cola: 'cocacola',
            self.Sprite: 'sprite',
            self.Fanta: 'fanta'
        }

        description = descriptions.get(self)
        if not description:
            raise ValueError(f'Описание не заполнено для {self.value}')

        return description


class Soda:
    """Запрашивает у пользователя желаемую добавку к газировке
    и выводит получившийся напиток."""

    def __init__(self, additive: Options | None = None):
        self.additive = additive

    def show_my_drink(self):
        if not self.additive:
            print("Обычная газировка.")
        else:
            print("Газировка и {}".format(self.additive.description))


if __name__ == "__main__":
    drink = Soda(input("Введите желаемую добавку к газировке: "))
    drink.show_my_drink()
