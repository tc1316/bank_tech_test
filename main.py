from account import Account, StatementPrinter


def main():
    test_account = Account("Jeff", "Garlin")
    printer = StatementPrinter()

    test_account.set_date("10/01/2023")
    test_account.deposit(1000)

    test_account.set_date("13/01/2023")
    test_account.deposit(2000)

    test_account.set_date("14/01/2023")
    test_account.withdraw(500)

    print(printer.parse_transactions(test_account))

    printer.print_statement(test_account)


if __name__ == '__main__':
    main()
