class Roman:
    '''Конвертация арабских цифр в римские.'''

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'Введённое число {}'.format(self.num)


if __name__ == "__main__":

    number = Roman(input('Введите число до 4000: '))
    print(number)
