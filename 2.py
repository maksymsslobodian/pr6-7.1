class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено на {amount}. Новий баланс: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято {amount}. Залишок: {self.__balance}")
        else:
            print("Недостатньо коштів або некоректна сума.")

    def get_balance(self):
        return self.__balance

# Тестування для 3 акаунтів
acc1 = BankAccount("Олексій", 1000)
acc2 = BankAccount("Марія", 500)
acc3 = BankAccount("Іван", 0)

acc1.deposit(500)
acc1.withdraw(200)


print(f"Баланс {acc3.owner}: {acc3.get_balance()}")