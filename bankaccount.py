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
        # self.__budgets = [Budget("Games and Entertainment", 0),
        #                   Budget("Clothing and Accessories", 0),
        #                   Budget("Eating Out", 0),
        #                   Budget("Miscellaneous", 0)]
        self.__budgets = self.input_budget_details()
        self.__number = number
        self.__name = name
        self.__balance = balance

    @staticmethod
    def input_budget_details():
        budget_list = []
        print("\nEnter the budget limit for the given category:")
        cat_one = float(input("Games and Entertainment: "))
        budget_list.append(Budget("Games and Entertainment", cat_one))
        cat_two = float(input("Clothing and Accessories: "))
        budget_list.append(Budget("Clothing and Accessories", cat_two))
        cat_three = float(input("Eating Out: "))
        budget_list.append(Budget("Eating Out", cat_three))
        cat_four = float(input("Miscellaneous: "))
        budget_list.append(Budget("Miscellaneous", cat_four))
        return budget_list

    @property
    def budgets(self):
        """
        Return the list of budgets for a user.
        :return: list of Budgets
        """
        return self.__budgets

    # @property.setter
    # def budgets(self, budget1, budget2, budget3, budget4):
    #

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount


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

        self._update_balance(amount, budget_index)

        self.get_budget_by_index(budget_index - 1).record_transaction(timestamp, amount, purchase_location)

    def _update_balance(self, amount, budget):
        """
        Update the bank and budget balance based on the amount recorded in a transaction.
        :param amount:
        :param budget:
        :return:
        """
        self.balance = self.balance - amount
        self.get_budget_by_index(budget - 1).update_balance(amount)

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
               f"Balance: {self.balance}\n"