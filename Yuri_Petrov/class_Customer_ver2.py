class Customer:
    """Клиент телефонной компании.

    Расходы данного клиента ведуться на повременной основе."""

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб.".format(self.name, self.balance)

    @property
    def balance(self):
        """Вернуть баланс клиента.

        Свойство 'balance' доступно только для чтения:
        давать доступ на изменение его напрямую было бы неправильно."""
        return self._balance

    def record_payment(self, amount_paid):
        """Пополнить баланс клиента на 'amount_paid' руб."""
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.

        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;

            - minutes (int): количество минут разговора.
            """
        if call_type == "Г":
            self._balance -= minutes * 5
        elif call_type == "М":
            self._balance -= minutes * 1


class CustomerFree2ndMinutesAfter10(Customer):
    """Клиент телефонной компании (потомок Customer).

    После 10 минут звонка на городской номер, каждая вторая минута бесплатно;
    в остальном как "Повременный".

    Все атрибуты, что предоставляет Customer, доступны и здесь, достаточно
    изменить только те, которые должны работать по-другому."""

    def record_call(self, call_type, minutes):
        # Данный метод переопределяет соответствующий метод родителя

        # Определяем количество бесплатных минут
        if call_type == "Г" and minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        # Вызываем родительский метод расчета
        super().record_call(call_type, minutes - bonus_minutes)


class CustomerTwiceCheaperFirst5Minutes(Customer):
    """Клиент телефонной компании (потомок Customer).

    До 5 минут разговора в 2 раза дешевле тарифа "Повременный",
    после - в 2 раза дороже.

    Все атрибуты, что предоставляет Customer, доступны и здесь, достаточно
    изменить только те, которые должны работать по-другому."""

    def record_call(self, call_type, minutes):
        # Данный метод переопределяет соответствующий метод родителя

        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0

        # Вызываем родительский метод расчета
        super().record_call(call_type, cheap_minutes / 2 + expensive_minutes * 2)


if __name__ == "__main__":

    ivan = Customer("Иван Петров", 100)
    # Елена, Екатерина и Сергей теперь экземпляры других классов
    elena = CustomerFree2ndMinutesAfter10("Елена Миронова", 100)
    ekaterina = CustomerFree2ndMinutesAfter10("Екатерина Ефимова", 100)
    sergey = CustomerTwiceCheaperFirst5Minutes("Сергей Васильев", 100)

    ivan.record_call("Г", 20)
    elena.record_call("Г", 20)
    ekaterina.record_call("М", 20)
    sergey.record_call("Г", 20)

    print(ivan)
    print(elena)
    print(ekaterina)
    print(sergey)
