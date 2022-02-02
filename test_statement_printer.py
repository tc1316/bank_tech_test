import unittest
from account import StatementPrinter
from unittest.mock import Mock, patch


class TestStatementPrinter(unittest.TestCase):
    def setUp(self):
        self.printer = StatementPrinter()
        self.mock_new_account, self.mock_deposit, self.mock_withdraw = Mock(), Mock(), Mock()

        self.mock_new_account.configure_mock(statement=[])
        self.mock_deposit.configure_mock(statement=[{
            "date": "10/01/2023",
            "amount": 100000,
            "balance": 100000,
            "transaction_type": "deposit"}])
        self.mock_withdraw.configure_mock(statement=[{
            "date": "14/01/2023",
            "amount": 50000,
            "balance": 50000,
            "transaction_type": "withdraw"}])

    def test_parse_transactions(self):
        self.assertEqual(
            self.printer.parse_transactions(
                self.mock_new_account), '')

        self.assertEqual(
            self.printer.parse_transactions(
                self.mock_deposit),
            '10/01/2023 || 1000.00 || || 1000.00')

        self.assertEqual(
            self.printer.parse_transactions(
                self.mock_withdraw),
            '14/01/2023 || || 500.00 || 500.00')

    @patch("builtins.print")
    def test_print_statement(self, mock_print):
        self.printer.print_statement(self.mock_new_account)
        mock_print.assert_called_with("date || credit || debit || balance\n")

        self.printer.print_statement(self.mock_deposit)
        mock_print.assert_called_with(
            "date || credit || debit || balance\n10/01/2023 || 1000.00 || || 1000.00")

        self.printer.print_statement(self.mock_withdraw)
        mock_print.assert_called_with(
            "date || credit || debit || balance\n14/01/2023 || || 500.00 || 500.00")


if __name__ == '__main__':
    unittest.main()
