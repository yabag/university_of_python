class FootballPlayer:
    pass


if __name__ == "__main__":
    r9 = FootballPlayer()

    # При присвоении значения несуществующему полю класса Python дополняет класс
    # Синтаксически похож на словарь, где ключ указывается не в скобках [],  а через точку
    r9.name = "Рональдо"
    r9.birthday = "18/09/1976"
    r9.position = "Нападающий"
    r9.height = 1.83
    r9.wc_goals = 15

    print(r9.name, r9.birthday, r9.position, r9.height, r9.wc_goals)
