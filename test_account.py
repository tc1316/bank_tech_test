import unittest
from account import Account

class TestCalc(unittest.TestCase):
  def setUp(self):
    self.client = Account(forename='Sue', surname='Smith', date_created='10/01/2023', initial_balance=0)
    self.client2 = Account(forename='Jeff', surname='Garlan', date_created='10/01/2023', initial_balance=100)

  def test_account_name(self):
    self.assertEqual(self.client.forename, 'Sue')
    self.assertEqual(self.client.surname, 'Smith')
    self.assertEqual(self.client.fullname, 'Sue Smith')

  def test_account_date_creation(self):
    self.assertEqual(self.client.date_created, '10/01/2023')

  def test_initial_balance(self):
    self.assertEqual(self.client.balance, 0)
    self.assertEqual(self.client2.balance, 100)

  def test_credit_account(self):
    self.assertEqual(self.client.credit(100),100)
    self.assertEqual(self.client2.credit(100),200)
  
  def test_debit_account(self):
    self.assertEqual(self.client2.credit(100),0)
    
  
  

