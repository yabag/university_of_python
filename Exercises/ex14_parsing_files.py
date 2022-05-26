class Parsing:
    def __init__(self, file_1, file_2):
        self.file_1 = file_1
        self.file_2 = file_2

    def __str__(self):
        return "В файле '{}' нет следующих строк:\n".format(self.file_2)

    def parsing_files(self, file_1, file_2):
        pass


if __name__ == "__main__":
    p = Parsing('ru.txt', 'en.txt')
    print(p)
    # parsing_files()
