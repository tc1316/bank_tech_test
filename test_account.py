import unittest
from account import Account
from datetime import date


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.client = Account(
            forename='Sue',
            surname='Smith')

    def test_account_name(self):
        self.assertEqual(self.client.forename, 'Sue')
        self.assertEqual(self.client.surname, 'Smith')

    def test_date_defaults_to_today(self):
        self.assertEqual(self.client.date, date.today().strftime('%d/%m/%Y'))

    def test_date_can_be_set(self):
        self.assertEqual(self.client.set_date("10/01/2023"), "10/01/2023")
        with self.assertRaises(ValueError):
            self.client.set_date("10 Jan 2023")

    def test_balance_cannot_be_accessed(self):
        with self.assertRaises(AttributeError):
            self.client.__balance += 0

    def test_deposit(self):
        self.assertEqual(self.client.deposit(100), 10000)
        self.assertEqual(self.client.deposit(50), 15000)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.client.withdraw(1)

        self.client.deposit(100)
        self.assertEqual(self.client.withdraw(100.00), 0)
        with self.assertRaises(ValueError):
            self.client.withdraw(1)

    def test_dataclass_str_method(self):
        self.assertEqual(
            self.client.__str__(),
            f"Sue Smith - Outstanding balance: 0.00 - Date: {date.today().strftime('%d/%m/%Y')}")

        self.client.deposit(96.12)
        self.assertEqual(
            self.client.__str__(),
            f"Sue Smith - Outstanding balance: 96.12 - Date: {date.today().strftime('%d/%m/%Y')}")

        self.client.set_date("10/01/2023")
        self.assertEqual(
            self.client.__str__(),
            "Sue Smith - Outstanding balance: 96.12 - Date: 10/01/2023")

    def test_statement(self):
        self.assertEqual(self.client.statement, [])

        self.client.deposit(96.12)
        self.assertEqual(
            self.client.statement,
            [f"{date.today().strftime('%d/%m/%Y')} || 96.12 || || 96.12"])

        self.client.set_date("10/01/2023")
        self.client.withdraw(23.59)
        self.assertEqual(self.client.statement,
                         [f"{date.today().strftime('%d/%m/%Y')} || 96.12 || || 96.12",
                          '10/01/2023 || || 23.59 || 72.53'])


if __name__ == '__main__':
    unittest.main()
