import math


class Circle:
    """Окружность."""

    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        # Радиус self._r устанавливается через метод-сеттер set_r(),
        # который проверяет устанавливаемое значение

        self.set_r(r)

    def legth(self):
        """Вернуть длину окружности."""

        return 2 * math.pi * self._r

    def square(self):
        """Вернуть площадь окружности."""

        return math.pi * self._r ** 2

    def get_r(self):
        """Вернуть радиус."""

        return self._r

    def set_r(self, r):
        """Установить радиус в значение 'r'."""

        # Устанавливаем только положительный радиус

        assert r > 0, "Радиус должен быть положительным!"

        self._r = r

    def __str__(self):

        return "Окружность ({0.x}; {0.y}) радиус={0._r}".format(self)


if __name__ == "__main__":

    c = Circle(3, 4, 1)
    print(c)  # Окружность (3, 4) радиус=1
    print(c.legth(), c.square())  # 6.283185307179586 3.141592653589793

    c.set_r(-1)  # AssertionError: Радиус должен быть положительным!
