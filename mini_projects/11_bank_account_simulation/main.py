"""Mini Project 11: Bank Account Simulation"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.history.append(f"Withdraw: -{amount}")


def main():
    account = BankAccount("Hendra", 100000)
    account.deposit(50000)
    account.withdraw(30000)
    print(f"Balance: {account.balance}")
    print(account.history)


if __name__ == "__main__":
    main()
