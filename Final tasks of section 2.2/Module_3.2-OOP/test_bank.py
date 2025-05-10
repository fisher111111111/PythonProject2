class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств для снятия")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        # На CheckingAccount можно снимать сколько угодно, даже больше баланса
        self._BankAccount__balance -= amount  # прямое обращение к приватному атрибуту


# Пример использования

account = SavingsAccount("Иван Иванов")
account.deposit(500)
account.withdraw(100)
account.apply_interest()
print(f"Баланс после операций: {account.get_balance()}")

def test_balance_positive():
    test_account = SavingsAccount("Тестовый")
    test_account.deposit(500)
    test_account.withdraw(100)
    test_account.apply_interest()

    assert test_account.get_balance() > 0, "Баланс должен быть положительным"
