"""
This module holds the Bank Account class.
"""

from budget import Budget
from datetime import datetime


class BankAccount:
    """
        Class representing a BankAccount for a user, with methods to
        record and view transactions.
    """

    PERCENT = 100

    def __init__(self, number, name, balance):
        """
        Initialize a BankAccount with a budget list, account number,
        name, and balance.
        :param number: a string
        :param name: a string
        :param balance: a float
        """
        self._budgets = self._create_budget_list()
        self._number = number
        self._name = name
        self._balance = balance

    @property
    def name(self):
        """
        Get the bank name.
        :return: a string
        """
        return self._name

    @property
    def number(self):
        """
        Get the bank account number.
        :return: a string
        """
        return self._number

    @property
    def budgets(self):
        """
        Return the list of budgets for a user.
        :return: a list of Budgets
        """
        return self._budgets

    @property
    def balance(self):
        """
        Return the balance of the user's bank account.
        :return: an int or a float
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Set the balance to the amount passed in.
        :param amount: an int or a float
        """
        self._balance = amount

    def _get_budget_by_index(self, index):
        """
        Return a budget from the budget list by index.
        :param index: an int
        :return: a Budget
        """
        return self.budgets[index]

    def _input_transaction_details(self):
        """
        Prompt the user to enter details for a transaction.
        :return: dict of transaction details
        """
        budget_index = BankAccount.get_budget_index()
        budget = self._get_budget_by_index(budget_index)
        if budget.is_locked:
            raise BudgetIsLockedError(f"Budget {budget.name} is locked.")

        amount = float(input("Enter the amount: "))

        if amount <= 0:
            raise TransactionAmountError("Negative or 0 amounts are not allowed when making transactions. "
                                         "Could not complete your transaction.")

        purchase_location = input("Enter the purchase location: ")
        timestamp = datetime.now()

        return {"amount": amount, "purchase_location": purchase_location,
                "timestamp": timestamp, "budget": budget, "budget_index": budget_index}

    def record_transaction(self, user):
        """
        Record a new transaction in a budget. Deny transactions when a budget is locked, if a
        balance would drop below 0 after the transaction, or when invalid values are entered.
        """
        try:
            amount, purchase_location, timestamp, budget, budget_index = self._input_transaction_details().values()
        except BudgetIsLockedError as e:
            raise BudgetIsLockedError(e.args) from e
        except ValueError:
            print("Could not record transaction. One or more invalid values were entered.")
            return
        except TransactionAmountError as e:
            print(e)
            return

        # If the budget is locked or balance will drop below 0, don't continue transaction
        if budget.is_locked:
            raise BudgetIsLockedError("Budget is locked.")
        else:
            if self.balance < amount:
                raise InvalidBalanceError("Transaction not processed. Amount would put balance below 0.")
            else:
                self._complete_transaction(user, amount, budget_index, budget, timestamp, purchase_location)

    def _complete_transaction(self, user, amount, budget_index, budget, timestamp, purchase_location):
        """
        Complete a transaction by updating the bank balance, recording the transaction in the
        specified budget, and running checks on completions.
        :param amount: a float
        :param budget_index: an int
        :param budget: a Budget
        :param timestamp: a datetime object
        :param purchase_location: a string
        """
        self._update_balance(amount, budget_index)
        budget.record_transaction(timestamp, amount, purchase_location)
        self._on_transaction_complete(user, budget)

    def _on_transaction_complete(self, user, budget):
        """
        Execute checks after a transaction is completed.
        :param user: a user
        :param budget: a Budget
        """
        print("\nTransaction successful.")
        budget_balance = budget.amount_left
        percent = (budget.amount_spent / budget.limit) * BankAccount.PERCENT

        # check if the budget is exceeded
        if self._check_budget_exceeded(budget_balance):
            # yes - get notification and print transactions
            self._notify_budget_exceeded(user, budget)

        # check if the budget is almost exceeded
        elif self._check_budget_almost_exceed(user, percent):
            # yes - get warning and print transactions
            self._warn_budget_almost_exceeded(user, budget)

        # lock the budget if exceeded
        if self._check_lock_budget(percent, user):
            self._lock_budget(budget, user)

    def _check_lock_budget(self, percent, user):
        """
        Check if the budget should be locked. Return True if percentage is over the lock limit
        and user is lockable, False if the percentage is not over the lock limit or if the user
        is not lockable.
        :param percent: int or a float
        :param user: a user
        :return: a boolean
        """
        return percent > user.lock_limit and user.is_lockable

    def _lock_budget(self, budget, user):
        """
        Lock a budget and increment the user's locked budget count. Notify
        the user that their budget has been locked.
        :param budget: a Budget
        :param user: a user
        """
        budget.is_locked = True
        user.increment_locked_budgets()
        print(f"Budget {budget.name} has been locked")

    def _check_budget_almost_exceed(self, user, percent):
        """
        Check if a budget is almost exceeded and return True if the percentage of the
        amount spent from the budget, False otherwise.
        :param user: a User
        :param percent: an int or float
        :return: a boolean
        """
        return percent > user.percentage_warning

    def _warn_budget_almost_exceeded(self, user, budget):
        """
        Warn the user that the budget is almost exceeded and print
        a list of all the transactions for that budget.
        :param user: a User
        :param budget: a Budget
        """
        print(user.get_warning())
        print(budget.get_transactions_string())

    def _check_budget_exceeded(self, budget_balance):
        """
        Check if a budget is exceeded.
        :param budget_balance: an int or a float
        :return: True if budget balance is under 0, False otherwise
        """
        return budget_balance < 0

    def _notify_budget_exceeded(self, user, budget):
        """
        Notify the user that the budget is exceeded and print
        a list of all the transactions for that budget.
        :param user: a User
        :param budget: a Budget
        """
        print(user.get_notification())
        print(budget.get_transactions_string())

    def _update_balance(self, amount, budget_index):
        """
        Update the bank and budget balance based on the amount recorded in a transaction.
        :param amount: a User
        :param budget_index: an int
        """
        self.balance = self.balance - amount
        self._get_budget_by_index(budget_index).update_balance(amount)

    def view_budgets(self):
        """
        Print all of the budget information for each budget in the budget list.
        """
        for budget in self.budgets:
            print(budget)

    def view_transactions_by_budget(self):
        """
        Print all of the transactions in a specific budget.
        """
        budget_index = BankAccount.get_budget_index()
        transactions_string = self._get_budget_by_index(budget_index).get_transactions_string()
        print(transactions_string)

    @staticmethod
    def get_budget_index():
        """
        Handle user input to choose a budget and return a budget index based on the user input.
        :return: an int
        """

        # Print out budget options
        print("\nBudget Options:\n"
              "--------------------\n"
              "1 - Games and Entertainment\n"
              "2 - Clothing and Accessories\n"
              "3 - Eating Out\n"
              "4 - Miscellaneous")

        # Keep prompting user to enter an option until a valid one is chosen
        option = 0
        while True:
            try:
                option = int(input("\nPlease enter one of the options above:"))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue
            if 0 < option < 5:
                break
            else:
                print("Option invalid")

        return option - 1

    @staticmethod
    def input_budget_details():
        """
        Prompt the user to enter budget details for each category and
        return the budget list created. Catch any errors regarding invalid inputs.
        :return: a list of Budgets
        """
        budget_list = []
        while True:
            try:
                print("\nEnter the budget limit for the given category:")

                cat_one = float(input("Games and Entertainment: "))
                cat_two = float(input("Clothing and Accessories: "))
                cat_three = float(input("Eating Out: "))
                cat_four = float(input("Miscellaneous: "))

                if cat_one <= 0 or cat_two <= 0 or cat_three <= 0 or cat_four <= 0:
                    raise InvalidBalanceError("Budget limit has to be a positive non-zero value.")
            except ValueError:
                print("One or more of the values were incorrect. Please try again.")
                continue
            else:
                budget_list.append(Budget("Games and Entertainment", cat_one))
                budget_list.append(Budget("Clothing and Accessories", cat_two))
                budget_list.append(Budget("Eating Out", cat_three))
                budget_list.append(Budget("Miscellaneous", cat_four))
                break

        return budget_list

    def __str__(self):
        """
        Build a string that contains the bank account details, as well as all
        the transactions made and the closing balance.
        :return: the information about the bank account as a string.
        """
        transactions_list = [budget.get_transactions_string() for budget in self.budgets]
        transactions_string = "\n ".join(transactions_list)

        return f"Viewing Bank Account Details \n" \
               f"---------------------------- \n" \
               f"\nNumber: {self.number}\n" \
               f"Name: {self.name}\n" \
               f"Transactions by Budget \n" \
               f"----------------------------- \n" \
               f"{transactions_string}\n" \
               f"Balance: {self.balance}"

    def _create_budget_list(self):
        while True:
            try:
                budget_list = self.input_budget_details()
            except InvalidBalanceError as e:
                print(e)
            else:
                break
        return budget_list


class InvalidBalanceError(Exception):
    """
    Exception for when the user tries to input a value that would result in a negative or zero bank/budget balance.
    """

    def __init__(self, message):
        """
        Initialize a InvalidBalanceError Exception and passes in a message to its parent class (Exception).
        :param message: description of the exception as a string
        """
        super().__init__(message)


class BudgetIsLockedError(Exception):
    """
    Exception for when the user tries to make a transaction in a budget that is locked.
    """

    def __init__(self, message):
        """
        Initialize a BudgetIsLockedError Exception and passes in a message to its parent class (Exception).
        :param message: description of the exception as a string
        """
        super().__init__(message)


class TransactionAmountError(Exception):
    """
    Exception for when the user enters an invalid transaction amount, such as negative values or zero.
    """

    def __init__(self, message):
        """
        Initialize a TransactionAmountError Exception and passes in a message to its parent class (Exception).
        :param message: description of the exception as a string
        """
        super().__init__(message)
