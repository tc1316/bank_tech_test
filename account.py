from datetime import date
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Account:
    forename: str
    surname: str
    balance: float = 0  # Stored in pence
    date = date.today().strftime('%d/%m/%Y')
    statement: List = field(default_factory=list)

    def __str__(self):
        return f"{self.forename} {self.surname} - Outstanding balance: {self.balance / 100} - Date: {self.date}"

    def entry_generator(self, amount, entry_type=None):
        if entry_type == "deposit":
            self.statement.append(
                f"{self.date} || {(amount / 100):.2f} || || {(self.balance / 100):.2f}")
        elif entry_type == "withdraw":
            self.statement.append(
                f"{self.date} ||  || {(amount / 100):.2f}|| {(self.balance / 100):.2f}")
        else:
            raise TypeError("Needs to be a deposit or withdrawal")

    def deposit(self, amount):
        amount *= 100
        self.balance += amount
        self.entry_generator(amount, entry_type="deposit")
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            amount *= 100
            self.balance -= amount
            self.entry_generator(amount, entry_type="withdraw")
            return self.balance
        else:
            raise ValueError("Insufficient funds")

    def print_statement(self):
        print('date || credit || debit || balance')
        for i in range(len(self.statement) - 1, -1, -1):
            print(self.statement[i])


def main():
    test_account = Account("Jeff", "Garlan")
    print(test_account)
    test_account.deposit(100)
    test_account.deposit(50)
    test_account.withdraw(25)
    test_account.withdraw(10)
    test_account.print_statement()
    print(test_account)


if __name__ == '__main__':
    main()
