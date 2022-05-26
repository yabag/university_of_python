class Customer:
    """Клиент телефонной компании.

    Расходы данного клиента ведуться на повременной основе."""

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб.".format(self.name, self.balance)

    @property
    def
