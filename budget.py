"""This module holds the Budget class"""

from transaction import Transaction
from tabulate import tabulate


class Budget:
    """
    Class representing a Budget category for a User, with methods that
    allow a user to record and view transactions, and view amount
    spent in the budget.
    """

    def __init__(self, name, limit):
        """
        Initialize a new Budget with a name, limit, list of transactions,
        amount spent, and amount left.
        :param name: a string
        :param limit: a float
        """
        self._name = name
        self._limit = limit
        self._transactions = []
        self._amount_spent = 0
        self._amount_left = limit
        self._is_locked = False

    # is locked property
    @property
    def is_locked(self):
        """
        Return if budget is locked.
        :return: True if locked, otherwise False
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, value):
        """
        Set the whether budget is locked to value passed in.
        :param value: a boolean
        """
        self._is_locked = value

    # transaction property
    @property
    def transactions(self):
        """
        Return list of transactions.
        :return: list of Transactions
        """
        return self._transactions

    # limit property
    @property
    def limit(self):
        """
        Return the budget limit.
        :return: a float
        """
        return self._limit

    # name property
    @property
    def name(self):
        """
        The name of the Budget.

        :return name: the name of the Budget, as a String
        """
        return self._name

    # amount_spent property
    @property
    def amount_spent(self):
        """
        Return the amount spent in the budget.
        :return: a float
        """
        return self._amount_spent

    @amount_spent.setter
    def amount_spent(self, amount):
        """
        Set the amount spent to the amount passed in.
        :param amount: a float
        """
        self._amount_spent = amount

    # amount_left property
    @property
    def amount_left(self):
        """
        Return the amount left in the budget.
        :return: a float
        """
        return self._amount_left

    @amount_left.setter
    def amount_left(self, amount):
        """
        Set the amount left to the amount passed in.
        :param amount: a float
        """
        self._amount_left = amount

    def _add_to_transaction(self, transaction):
        """
        Add a transaction to the transaction list.
        :param transaction: Transaction
        """
        self._transactions.append(transaction)

    def record_transaction(self, timestamp, amount, purchase_location):
        """
        Record a new transaction.
        :param timestamp: a datetime object
        :param amount: a float
        :param purchase_location: a string
        """
        transaction = Transaction(self.name, timestamp, amount, purchase_location)
        self._add_to_transaction(transaction)
        return transaction

    def get_transactions_string(self):
        """
        Return all of the transaction details for each transaction in the
        transaction lists as a string.
        :return: a string
        """
        transaction_string = ''
        print(f"\nTransactions for: {self.name}")
        for transaction in self.transactions:
            transaction_string += str(transaction)
        return transaction_string

    def update_balance(self, amount):
        """
        Increment the amount by the amount given
        Decrement the amount left by the amount given.
        :param amount: a float
        """
        self.amount_spent += amount
        self.amount_left -= amount

    def __str__(self):
        """
        Build and return a string that describes this Budget
        :return: a string
        """
    #     return f"""The budget {self.name} (locked: {self.is_locked}) has a limit of {self.limit}. The user has spent
    #             "{self.amount_spent} dollars and there are {self.amount_left} dollars left"""
        locked = "Yes" if self.is_locked else "No"
        budget_string = tabulate(
            [["Category", f"{self.name}"], ["Locked", f"{locked}"], ["Limit in dollars", f"{self.limit}"],
             ["Amount Spent in dollars", f"{self.amount_spent}"], ["Amount left in dollars", f"{self.amount_left}"]],
            tablefmt="grid")
        return budget_string
