class Point2D:
    '''Точка на плоскости.'''

    # Инициализирующий метод
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Строковое представление класса
    def __str__(self):
        '''Вернуть строку в виде 'Точка 2D (x, y)'.'''
        return 'Точка 2D ({}, {})'.format(self.x, self.y)

    def distance(self):
        '''Вернуть расстояние до центра координат.'''
        return (self.x ** 2 + self.y ** 2) ** 0.5


if __name__ == '__main__':
    p = Point2D(3, 4)
    print(p)  # Точка 2D (3, 4)

