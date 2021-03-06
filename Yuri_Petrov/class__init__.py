class Point2D:
    '''Точка на плоскости.'''

    # Инициализирующий метод (специальный метод с __)
    def __init__(self, x, y):
        self.x = x  # Поля читаются и записываются через 'self'
        self.y = y  # 'self' указывает на текущий экземпляр класса

    # Обычный метод объекта (метод экземпляра класса) имеет те же правила
    # наименования, что и  обычные функции

    def distance(self):
        '''Вернуть расстояние до центра координат.'''
        return (self.x ** 2 + self.y ** 2) ** 0.5


if __name__ == '__main__':
    # Создание объекта (экземпляра класса)
    # Передаём параметры, которые теперь требует '__init__()'
    # Параметр 'self' не передаётся явно, но содержит ссылку на 'p'
    p = Point2D(3, 4)

    # При выводе объекта на экран по умолчанию отображается имя класса
    print(p)

    # После инициализации доступны атрибуты 'p.x' и 'p.y',
    # где хранятся переданные при создании объекта значения
    print(p.x, p.y)  # 3 4

    # Вызов обычного метода
    print('Расстояние до центра координат: {:.2f}'.format(p.distance()))  # 5
