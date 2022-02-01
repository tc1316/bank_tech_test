from datetime import date, datetime
from dataclasses import dataclass, field
from typing import List


@dataclass
class Account:
    forename: str
    surname: str
    __balance: float = 0  # Stored in pence
    date = date.today().strftime('%d/%m/%Y')
    statement: List = field(default_factory=list)

    def __str__(self):
        return f"{self.forename} {self.surname} - Outstanding balance: {(self.__balance / 100):.2f} - Date: {self.date}"

    def deposit(self, amount):
        amount = abs(amount)
        amount *= 100
        self.__balance += amount
        self.__statement_generator(amount, entry_type="deposit")
        return self.__balance

    def withdraw(self, amount):
        amount = abs(amount)
        if self.__balance - amount >= 0:
            amount *= 100
            self.__balance -= amount
            self.__statement_generator(amount, entry_type="withdraw")
            return self.__balance
        else:
            raise ValueError("Insufficient funds")

    def set_date(self, new_date: str):
        self.date = datetime.strptime(
            new_date, '%d/%m/%Y').strftime('%d/%m/%Y')
        return self.date

    def print_statement(self):
        print(
            f"date || credit || debit || balance\n{self.__compile_statement()}")

    # Private method
    def __statement_generator(self, amount, entry_type=None):
        if entry_type == "deposit":
            self.statement.append(
                f"{self.date} || {(amount / 100):.2f} || || {(self.__balance / 100):.2f}")
        elif entry_type == "withdraw":
            self.statement.append(
                f"{self.date} || || {(amount / 100):.2f} || {(self.__balance / 100):.2f}")
        else:
            raise TypeError("Needs to be a deposit or withdrawal")

    def __compile_statement(self):
        str = ""
        for i in range(len(self.statement) - 1, -1, -1):
            str += f"{self.statement[i]}\n"
        return str


def main():
    test_account = Account("Jeff", "Garlan")
    print(test_account)
    test_account.deposit(10000)
    test_account.deposit(50)
    test_account.withdraw(25)
    test_account.withdraw(10)
    test_account.set_date("10/01/2023")
    test_account.withdraw(1000)
    test_account.print_statement()


if __name__ == '__main__':
    main()
