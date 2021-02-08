"""
This module holds the User class.
"""
from bankaccount import BankAccount
from abc import ABC


class User(ABC):
    """
    The User class is the blueprint for creating a User object.
    """

    def __init__(self, name, age):
        """
        Initialize the instance variables name, age and bank.
        :param name: the name of the user as a String
        :param age: the age of the user as an int
        """
        self.__name = name
        self.__age = age

        # creating the user's bank account
        self.__bank = self.input_bank_details()

    @property
    def bank(self):
        """
        Getter of the bank property.
        return: the user's bank account
        """
        return self.__bank

    @staticmethod
    def input_bank_details():
        """
        Input the user for details and creates a bank account object with the details.
        return: the newly created bank account
        """
        bank_number = input("Please enter the bank number: ")
        name = input("Please enter the name of the bank: ")
        balance = float(input("Please enter the bank balance: "))

        return User.create_bank_account(bank_number, name, balance)

    @staticmethod
    def create_bank_account(bank_number, name, balance):
        """
        Create a new Bank Account object with the user's bank details.
        return: the newly created bank account object.
        """
        bank_account = BankAccount(bank_number, name, balance)
        return bank_account

    def view_budgets(self):
        """
        Show the budgets that are stored in the user's bank account.
        """
        self.bank.view_budgets()

    def view_transactions(self):
        """
        Show the transactions that are stored in the user's bank account budgets.
        """
        self.bank.view_transactions_by_budget()

    def record_transaction(self):
        """
        Record a new transaction from the user's bank.
        """
        self.bank.record_transaction()

    def view_bank_details(self):
        """
        Show the details of the user's bank account.
        """
        print(self.bank)
