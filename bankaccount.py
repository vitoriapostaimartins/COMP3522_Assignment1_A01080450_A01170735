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
    def __init__(self, number, name, balance):
        """
        Initialize a BankAccount with a budget list, account number,
        name, and balance.
        :param number: an int
        :param name: a string
        :param balance: a float
        """
        self.__budgets = [Budget("Games and Entertainment", 123.12),
                          Budget("Clothing and Accessories", 100),
                          Budget("Eating Out", 200),
                          Budget("Miscellaneous", 50)]
        self.__number = number
        self.__name = name
        self.__balance = balance

    @property
    def budgets(self):
        """
        Return the list of budgets for a user.
        :return: list of Budgets
        """
        return self.__budgets

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
        return int(input("Please enter one of the options above:"))

    def record_transaction(self):
        """
        Record a new transaction in a budget.
        """
        budget_index = BankAccount.get_budget_index()
        amount = float(input("Enter the amount: "))
        purchase_location = input("Enter the purchase location: ")
        timestamp = datetime.now()

        self.get_budget_by_index(budget_index - 1).record_transaction(timestamp, amount, purchase_location)

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
        self.get_budget_by_index(budget_index-1).print_transactions()

    def __str__(self):
        return f"Viewing Bank Account Details \n" \
               f"---------------------------- \n" \
               f"\nNumber: {self.__number}\n" \
               f"Name: {self.__name}\n" \
               f"Balance: {self.__balance}\n"
