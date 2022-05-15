class Point2D:
    '''Точка на плоскости.'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        '''Вернуть строку в виде 'Точка 2D (x, y)'.'''
        return 'Точка 2D ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        '''Создать новый объект, как сумму координать self  и other.'''

        if isinstance(other, self.__class__):
            # Точка с точкой
            # Возвращаем новый объект!
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            # Точка и число
            # Добавим к обеим координатам self число other и вернем результат
            # Возвращаем старый, измененный объект!
            self.x += other
            self.y += other
            return self
        else:
            # В противном случае возбуждаем исключение
            raise TypeError('Не могу добавить {1} к {0}'.format(self.__class__, type(other)))


if __name__ == '__main__':
    p1 = Point2D(0, 5)
    p2 = Point2D(-5, 10)

    print(p1 + 2)    # (2, 7)
    print(p1 + 5.0)  # (7.0, 12,0)
    # TypeError: Не могу добавить <class 'str'> к <class '__main__.Point2D'>
    print(p1 + 'я строка')
