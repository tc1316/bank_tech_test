# Bank Tech Test
First practice of a tech test with the aim of polishing OOD and TDD

----
## Requirements
- Python 3.8+ (https://www.python.org/downloads/)
- Pip 22.0.2+ (https://pip.pypa.io/en/stable/installation/)
- Coverage.py (https://coverage.readthedocs.io/en/6.3/)
- Modules (part of Python Standard Library): unittest, datetime, dataclasses, typing

# Approach
- Used a dataclass to encapsulate attributes of an account as syntax is neater
- Set default date to today; created a set_date method to allow for testing other dates
- Deposit and withdraw methods separated instead of using a common function to prevent confusion 
  - Deposit and withdraw methods call private method to create new element in statement list
- Print_statement method prints the statement list in reverse order to the terminal with a header 
  - Header printed separately otherwise creating new elements would require insertion at the -2 position
- Balance stored in pence to prevent floating point rounding errors
  - User still inputs in pounds however, the value is multiplied by 100 when stored in balance but divided by 100 (float division) when printing

----
## Running tests
- Run "coverage run -m test_account"
- Run "coverage run -m test_statement_printer"
- To check coverage: "coverage report"

## Running code 
- Run "python account.py" from root
- You should see:
```
date || credit || debit || balance
14/01/2023 || || 500.00 || 2500.00
13/01/2023 || 2000.00 || || 3000.00
10/01/2023 || 1000.00 || || 1000.00
```

