import unittest
from account import Account
from datetime import date


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.client = Account(
            forename='Sue',
            surname='Smith')
        self.client2 = Account(
            forename='Jeff',
            surname='Garlan',
            balance=10000)

    def test_account_name(self):
        self.assertEqual(self.client.forename, 'Sue')
        self.assertEqual(self.client.surname, 'Smith')

    def test_date_defaults_to_today(self):
        self.assertEqual(self.client.date, date.today().strftime('%d/%m/%Y'))

    def test_setting_initial_balance(self):
        self.assertEqual(self.client.balance, 0)
        self.assertEqual(self.client2.balance, 10000)

    def test_deposit(self):
        self.assertEqual(self.client.deposit(100.00), 10000)
        self.assertEqual(self.client.deposit(50), 15000)
        self.assertEqual(self.client2.deposit(100.00), 20000)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.client.withdraw(1)
        self.assertEqual(self.client2.withdraw(100.00), 0)
        with self.assertRaises(ValueError):
            self.client2.withdraw(1)


if __name__ == '__main__':
    unittest.main()
