import math


class Circle:
    """Окружность."""

    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y

        self.r = r

    def length(self):
        """Вернуть длину окружности."""

        return 2 * math.pi * self.r

    def square(self):
        """Вернуть площадь окружности."""

        return math.pi * self.r ** 2

    @property
    def r(self):
        # Определение свойства 'r': возвращает 'self._r' и позволяет работать с
        # радиусом извне, как с обычным атрибутом
        return self._r

    @r.setter
    def r(self, r):
        """Установить радиус окружности в 'r'.

        Метод может быть опущен, свойство 'r' должно быть доступно только для чтения.
        """

        assert r > 0, "Радиус должен быть положительным!"

        self._r = r

    def __str__(self):
        return "Окружность ({0.x}; {0.y}) радиус={0.r}".format(self)


if __name__ == "__main__":

    c = Circle(3, 4, 1)

    c.r *= 5  # Увеличили радиус в 5 раз

    print(c)  # Окружность (3, 4) радиус=5
    print(c.length(), c.square())  # 6.283185307179586 3.141592653589793

    c.r = -1  # AssertError: Радиус должен быть положительным!
