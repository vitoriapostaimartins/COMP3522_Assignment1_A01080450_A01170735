"""
This module holds the User class.
"""
import abc

from Assignments.Assignment1.notifications import Notifications
from bankaccount import BankAccount, BudgetIsLockedError
from bankaccount import InvalidTransactionError
from abc import ABC


class User(ABC):
    """
    The User class is the blueprint for creating a User object.
    """

    def __init__(self, name, age, warning, is_lockable, lock_limit):
        """
        Initialize the instance variables name, age and bank.
        :param name: the name of the user as a String
        :param age: the age of the user as an int
        """
        self._name = name
        self._age = age
        self._percentage_warning = warning
        self._is_lockable = is_lockable
        self._lock_limit = lock_limit
        self._locked_budgets = 0 # QUESTION do we keep it in user or in rebel

        # creating the user's bank account
        self.__bank = self.input_bank_details()

    def get_percentage_warning(self):
        return self._percentage_warning

    def get_warning(self):
        return Notifications.WARNING.value

    def increment_locked_budgets(self):
        self._locked_budgets += 1

    def get_lock_limit(self):
        return self._lock_limit

    def get_locked_budgets(self):
        return self._locked_budgets

    def get_is_lockable(self): #    QUESTION: should we make only properties/getters/setters?
        return self._is_lockable

    @abc.abstractmethod
    def get_type(self):
        pass

    @property
    def name(self):
        """
        Getter of the name property
        :return: the user's name
        """
        return self._name

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
        try:
            self.bank.record_transaction(self)
        except InvalidTransactionError as e:
            print(e)
        except BudgetIsLockedError as e:
            print(e)

    def view_bank_details(self):
        """
        Show the details of the user's bank account.
        """
        print(self.bank)

    @abc.abstractmethod
    def get_notification(self):
        pass

    @abc.abstractmethod
    def can_lock_account(self):
        pass

class UserIsLockedError(Exception):
    def __init__(self, message):
        super().__init__(message)
