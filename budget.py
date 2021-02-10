"""This module holds the Budget class"""

from transaction import Transaction


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

    @property
    def transactions(self):
        """
        Return list of transactions.
        :return: list of Transactions
        """
        return self._transactions

    def add_to_transaction(self, transaction):
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
        transaction = Transaction(self._name, timestamp, amount, purchase_location)
        self.add_to_transaction(transaction)
        return transaction

    def print_transactions(self):
        """
        Print all transactions in the transaction list.
        """
        for transaction in self._transactions:
            print("Transaction: \n", transaction)

    @property
    def amount_spent(self):
        """
        Return the amount spent in the budget.
        :return: a float
        """
        return self._amount_spent

    @amount_spent.setter
    def amount_spent(self, amount):
        self._amount_spent = amount

    @property
    def amount_left(self):
        """
        Return the amount left in the budget.
        :return: a float
        """
        return self._amount_left

    @amount_left.setter
    def amount_left(self, amount):
        self._amount_left = amount

    @property
    def limit(self):
        """
        Return the budget limit.
        :return: a float
        """
        return self._limit

    @property
    def name(self):
        """
        The name of the Budget.

        :return name: the name of the Budget, as a String
        """
        return self._name

    def update_balance(self, amount):
        self.amount_spent += amount
        self.amount_left -= amount

    def __str__(self):
        return f"""The budget {self.name} has a limit of {self.limit}. The user has spent {self.amount_spent} dollars 
        and there are {self.amount_left} dollars left"""
