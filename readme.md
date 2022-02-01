## Requirements
- Python 3.8+
- Coverage.py (https://coverage.readthedocs.io/en/6.3/)
- Modules: unittest, datetime, dataclasses, typing

## Running tests
- From root: "coverage run -m test_account"
- To check coverage: "coverage report"

----

# Approach
- Used a dataclass to encapsulate attributes of an account as syntax is neater
- Set default date to today; created a set_date method to allow for testing other dates
- Deposit and withdraw methods separated instead of using a common function to prevent confusion 
  - Deposit and withdraw methods call private method to create new element in statement list
- Print_statement method prints the statement list in reverse order to the terminal with a header 
  - Header printed separately otherwise creating new elements would require insertion at the -2 position
- Balance stored in pence to prevent floating point rounding errors
  - User still inputs in pounds however, the value is multiplied by 100 when stored in balance but divided by 100 (float division) when printing
