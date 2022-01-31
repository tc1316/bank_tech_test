# Account class
from dataclasses import dataclass


@dataclass()
class Account:
    forename: str
    surname: str
    date_created: str
    balance: int = 0

    def fullname(self):
      return f"{self.forename} {self.surname}"

    def credit(self, amount):
        self.balance += amount
        return self.balance        

    def debit(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError("Insufficient funds")


def main():
    test_account = Account("Jeff", "Garlan", '10/03/2023')
    print(test_account)
    test_account.credit(100)
    print(test_account)
    test_account.debit(201)


if __name__ == '__main__':
    main()
