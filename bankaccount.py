"""
This module holds the Bank Account class.
"""

from budget import Budget
from datetime import datetime


class BankAccount:
    PERCENT = 100

    """
    Class representing a BankAccount for a user, with methods to
    record and view transactions.
    """

    def __init__(self, number, name, balance):
        """
        Initialize a BankAccount with a budget list, account number,
        name, and balance.
        :param number: an int
        :param name: a string
        :param balance: a float
        """
        # self.__budgets = [Budget("Games and Entertainment", 0),
        #                   Budget("Clothing and Accessories", 0),
        #                   Budget("Eating Out", 0),
        #                   Budget("Miscellaneous", 0)]
        self._budgets = self.input_budget_details()
        self._number = number
        self._name = name
        self._balance = balance

    @staticmethod
    def input_budget_details():
        budget_list = []
        while True:
            try :
                print("\nEnter the budget limit for the given category:")
                cat_one = float(input("Games and Entertainment: "))
                budget_list.append(Budget("Games and Entertainment", cat_one))
                cat_two = float(input("Clothing and Accessories: "))
                budget_list.append(Budget("Clothing and Accessories", cat_two))
                cat_three = float(input("Eating Out: "))
                budget_list.append(Budget("Eating Out", cat_three))
                cat_four = float(input("Miscellaneous: "))
                budget_list.append(Budget("Miscellaneous", cat_four))
            except ValueError:
                print("One or more of the values were incorrect. Please try again.")
                continue
            else:
                break

        return budget_list

    @property
    def budgets(self):
        """
        Return the list of budgets for a user.
        :return: list of Budgets
        """
        return self._budgets

    # @property.setter
    # def budgets(self, budget1, budget2, budget3, budget4):
    #

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def get_budget_by_index(self, index):
        """
        Return a budget from the budget list by index.
        :param index: an int
        :return: a Budget
        """
        return self.budgets[index]

    @staticmethod
    def get_budget_index():
        """
        Return a budget index based on the user input.
        :return: an int
        """
        print("Budget Options:\n"
              "1 - Games and Entertainment\n"
              "2 - Clothing and Accessories\n"
              "3 - Eating Out\n"
              "4 - Miscellaneous")
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

    def _input_transaction_details(self):
        """
        Prompt the user to enter details for a transaction.
        :return: dict of transaction details
        """
        budget_index = BankAccount.get_budget_index()
        budget = self.get_budget_by_index(budget_index)
        if budget.is_locked:
            raise BudgetIsLockedError(f"Budget {budget.name} is locked.")

        amount = float(input("Enter the amount: "))

        if amount < 0:
            raise NegativeTransactionAmountError("Negative amounts are not allowed when making transactions. "
                                                 "Could not complete your transaction.")

        purchase_location = input("Enter the purchase location: ")
        timestamp = datetime.now()

        return {"amount": amount, "purchase_location": purchase_location,
                "timestamp": timestamp, "budget": budget, "budget_index": budget_index}

    def record_transaction(self, user):
        """
        Record a new transaction in a budget.
        """
        try:
            amount, purchase_location, timestamp, budget, budget_index = self._input_transaction_details().values()
        except BudgetIsLockedError as e:
            raise BudgetIsLockedError(e.args) from e
        except ValueError:
            print("Could not record transaction. One or more invalid values were entered.")
            return
        except NegativeTransactionAmountError as e:
            print(e)
            return

        # If the budget is locked, don't continue transaction
        if budget.is_locked:
            raise BudgetIsLockedError("Budget is locked.")

        # if percent > user.get_lock_limit():

        else:
            if self._balance < amount:
                raise InvalidTransactionError("Transaction not processed. Amount would put balance below 0.")
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
        :param user:
        :param budget:
        """
        print("Transaction successful.")
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
        Check if the budget should be locked
        :param percent:
        :param user:
        :return:
        """
        return percent > user.get_lock_limit() and user.get_is_lockable()

    def _lock_budget(self, budget, user):
        """
        Lock a budget and increment the user's locked budget count.
        :param budget:
        :param user:
        :return:
        """
        budget.is_locked = True
        user.increment_locked_budgets()
        print(f"Budget {budget.name} has been locked")

    def _check_budget_almost_exceed(self, user, percent):
        """
        Check if a budget is almost exceeded.
        :param user:
        :param percent:
        :return:
        """
        return percent > user.get_percentage_warning()

    def _warn_budget_almost_exceeded(self, user, budget):
        """
        Warn the user that the budget is almost exceeded and print
        a list of all the transactions for that budget.
        :param user:
        :param budget:
        :return:
        """
        print(user.get_warning())
        budget.print_transactions()

    def _check_budget_exceeded(self, budget_balance):
        """
        Check if a budget is exceeded
        :param budget_balance:
        :return:
        """
        return budget_balance < 0

    def _notify_budget_exceeded(self, user, budget):
        """
        Notify the user that the budget is exceeded and print
        a list of all the transactions for that budget.
        :param user:
        :param budget:
        :return:
        """
        print(user.get_notification())
        budget.print_transactions()

    def _update_balance(self, amount, budget):
        """
        Update the bank and budget balance based on the amount recorded in a transaction.
        :param amount:
        :param budget:
        :return:
        """
        self.balance = self.balance - amount
        self.get_budget_by_index(budget).update_balance(amount)

    def view_budgets(self):
        """
        Print all of the budget information in the budget list.
        """
        for budget in self.budgets:
            print(budget)

    def view_transactions_by_budget(self):
        """
        Print all of the transactions in a specific budget.
        """
        budget_index = BankAccount.get_budget_index()
        self.get_budget_by_index(budget_index).print_transactions()

    def __str__(self):
        return f"Viewing Bank Account Details \n" \
               f"---------------------------- \n" \
               f"\nNumber: {self._number}\n" \
               f"Name: {self._name}\n" \
               f"Balance: {self.balance}\n"


class InvalidTransactionError(Exception):
    def __init__(self, message):
        super().__init__(message)


class BudgetIsLockedError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeTransactionAmountError(Exception):
    def __init__(self, message):
        super().__init__(message)
