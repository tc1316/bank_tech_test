from datetime import date, datetime
from dataclasses import dataclass, field
from email.utils import parsedate_to_datetime
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
        amount = abs(amount)*100
        self.__balance += amount
        self.__transaction_generator(amount, transaction_type="deposit")
        return self.__balance

    def withdraw(self, amount):
        amount = abs(amount)*100
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.__transaction_generator(amount, transaction_type="withdraw")
            return self.__balance
        else:
            raise ValueError("Insufficient funds")

    def set_date(self, new_date: str):
        self.date = datetime.strptime(
            new_date, '%d/%m/%Y').strftime('%d/%m/%Y')
        return self.date

    def __transaction_generator(self, amount, transaction_type=None):
        if transaction_type == None:
            raise TypeError("Needs to be a deposit or withdrawal")
        self.statement.append({ "date": self.date, "amount": amount, "balance": self.__balance, "transaction_type": transaction_type})
class StatementPrinter:
    def parse_transactions(self, account: Account):
        statement = []
        for t in account.statement:
            if t['transaction_type'] == "deposit":
                statement.append(f"{t['date']} || {(t['amount'] / 100):.2f} || || {(t['balance'] / 100):.2f}")
            elif t['transaction_type'] == "withdraw":
                statement.append(f"{t['date']} || || {(t['amount'] / 100):.2f} || {(t['balance'] / 100):.2f}")
        return "\n".join(statement[::-1])

    def print_statement(self, account: Account):
        print(f"date || credit || debit || balance\n{self.parse_transactions(account)}")

        

    




    
