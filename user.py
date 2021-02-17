"""
This module holds the User class.
"""
import abc

from Assignments.Assignment1.notifications import Notifications
from bankaccount import BankAccount, BudgetIsLockedError
from bankaccount import NegativeBalanceError
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
        self._locked_budgets = 0

        # creating the user's bank account
        self._bank = self.input_bank_details()

    @property
    def percentage_warning(self):
        """
        Get the percentage warning.
        :return: percentage warning as a string
        """
        return self._percentage_warning

    @property
    def lock_limit(self):
        """
        Get the lock limit.
        :return: lock limit as an int
        """
        return self._lock_limit

    @property
    def locked_budgets(self):
        """
        Get the number of locked budgets.
        :return: locked budgets as an int
        """
        return self._locked_budgets

    @locked_budgets.setter
    def locked_budgets(self, value):
        """
        Set the number of locked budgets to the value passed in.
        :param value: an int
        """
        self._locked_budgets = value

    @property
    def name(self):
        """
        Get of the name property
        :return: the user's name
        """
        return self._name

    @property
    def bank(self):
        """
        Get of the bank property.
        return: the user's bank account
        """
        return self._bank

    @property
    def is_lockable(self):
        """
        Get for the is_lockable property.
        :return: True if user budgets are lockable as a boolean, False if not
        """
        return self._is_lockable

    @abc.abstractmethod
    def get_type(self):
        """
        Return the type of user.
        :return: user type as a string
        """
        pass

    @abc.abstractmethod
    def get_notification(self):
        """
        Return a notification depending on user type.
        :return: polite or rude notification as a string
        """
        pass

    @abc.abstractmethod
    def can_lock_account(self):
        """
        Return whether user can lock their account, depending on user type.
        :return: True or False as a boolean
        """
        pass

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
        except NegativeBalanceError as e:
            print(e)
        except BudgetIsLockedError as e:
            print(e)

    def view_bank_details(self):
        """
        Show the details of the user's bank account.
        """
        print(self.bank)

    def increment_locked_budgets(self):
        """
        Increment the number of budgets that are locked.
        """
        self.locked_budgets += 1

    @staticmethod
    def get_warning():
        """
        Get the warning string from the Notifications enum.
        :return: a warning as a string
        """
        return Notifications.WARNING.value

    @staticmethod
    def input_bank_details():
        """
        Input the user for details and creates a bank account object with the details.
        :return: the newly created bank account
        """
        while True:
            bank_number = ''
            name = ''
            balance = 0

            try:
                bank_number = input("Please enter the bank number: ")
                name = input("Please enter the name of the bank: ")
                balance = float(input("Please enter the bank balance: "))
            except ValueError:
                print("One or more of the values was invalid. Please try again.")
                continue
            else:
                break

        return User.create_bank_account(bank_number, name, balance)

    @staticmethod
    def create_bank_account(bank_number, name, balance):
        """
        Create a new Bank Account object with the user's bank details.
        :return: the newly created bank account object.
        """
        bank_account = BankAccount(bank_number, name, balance)
        return bank_account

    def __str__(self):
        """
        Build and returns a string with the User information.
        :return: the user information as a string
        """
        return f"{self.name}  ({self.get_type()})"


class UserIsLockedError(Exception):
    """
    Exception for when the user is locked out of their accounts.
    """
    def __init__(self, message):
        """
        Initialize an UserIsLockerError Exception and passes in a message to its parent class (Exception).
        :param message: description of the exception as a string
        """
        super().__init__(message)
