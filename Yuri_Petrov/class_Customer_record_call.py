class Customer:
    """Клиент телефонной компании."""

    def __init__(self, name, balance=0, call_plan="Повременный"):
        self.name = name
        self._balance = balance
        self.call_plan = call_plan  # "Повременный" по умолчанию

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб. Тариф: \"{}\"".format(self.name, self.balance, self.call_plan)

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

            - minutes (float): количество минут разговора.
            """
        # В реальности, эти значения могут читаться из базы данных
        if self.call_plan == "Повременный":
            # Фиксированная стоимость минуты в зависимости от типа звонка
            if call_type == "Г":
                self._balance -= minutes * 5
            elif call_type == "М":
                self._balance -= minutes * 1

        elif self.call_plan == "После10В2РазаДешевле":
            # После 10 минут звонка на городской номер
            # каждая вторая минута бесплатно
            if call_type == "Г":
                if minutes > 10:
                    bonus_minutes = (minutes - 10) // 2
                else:
                    bonus_minutes = 0
                self._balance -= (minutes - bonus_minutes) * 5
            elif call_type == "М":
                self._balance -= minutes * 1

        elif self.call_plan == "ПлатиМеньшеДо5Минут":
            # До 5 минут разговора в 2 раза дешевле тарифа 'Повременный',
            # после - в 2 раза дороже
            LIMIT_CHEAP = 5
            if minutes > LIMIT_CHEAP:
                cheap_minutes = LIMIT_CHEAP
                expensive_minutes = minutes - LIMIT_CHEAP
            else:
                cheap_minutes = minutes
                expensive_minutes = 0

            if call_type == "Г":
                self._balance -= cheap_minutes * 2.5 + expensive_minutes * 10
            elif call_type == "М":
                self._balance -= cheap_minutes * 0.5 + expensive_minutes * 2


if __name__ == "__main__":
    ivan = Customer("Иван Петров", 100)
    elena = Customer("Елена Миронова", 100, call_plan="После10В2РазаДешевле")
    ekaterina = Customer("Екатерина Ефимова", 100, call_plan="После10В2РазаДешевле")
    sergey = Customer("Сергей Васильев", 100, call_plan="ПлатиМеньшеДо5Минут")

    ivan.record_call("Г", 20)
    elena.record_call("Г", 20)
    ekaterina.record_call("М", 20)
    sergey.record_call("Г", 20)

print(ivan)         # "Иван Петров".        Баланс: 0 руб.      Тариф: "Повременный"
print(elena)        # "Елена Миронова".     Баланс: 25 руб.     Тариф: "После10В2РазаДешевле"
print(ekaterina)    # "Екатерина Ефимова".  Баланс: 80 руб.     Тариф: "После10В2РазаДешевле"
print(sergey)       # "Сергей Васильев".    Баланс: -62.5 руб.  Тариф: "ПлатиМеньшеДо5Минут"
