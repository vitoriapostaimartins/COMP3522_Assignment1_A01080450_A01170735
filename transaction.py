from tabulate import tabulate


"""
This module holds the Transaction class.
"""


class Transaction:
    """
    Class representing a single Transaction for a User.
    """
    def __init__(self, category, timestamp, dollar_amount, purchase_location):
        """
        Initialize a new Transaction with a budget category, timestamp,
        dollar amount spent, and purchase location.
        :param category: a string
        :param timestamp: a datetime
        :param dollar_amount: a float
        :param purchase_location: a string
        """
        self._category = category
        self._timestamp = timestamp
        self._dollar_amount = dollar_amount
        self._purchase_location = purchase_location

    @property
    def category(self):
        """
        Return the budget category name that the Transaction belongs to.
        :return: a string
        """
        return self._category

    @property
    def purchase_location(self):
        """
        Return the name of the website/shop where the Transaction took place.
        :return: a string
        """
        return self._purchase_location

    @property
    def timestamp(self):
        """
        Get the timestamp of the transaction
        :return: a datetime
        """
        return self._timestamp

    @property
    def dollar_amount(self):
        """
        Return the dollar amount spent in the transaction.
        :return: a float
        """
        return self._dollar_amount

    def __str__(self):
        """
        Return the transaction details as a string.
        :return: a string
        """
        time = self.timestamp.strftime("%b %d %Y %H:%M:%S")
        transaction_string = tabulate(
            [["Category", f"{self.category}"], ["Time", f"{time}"], ["Amount", f"{self.dollar_amount}"],
             ["Location", f"{self.purchase_location}"]], tablefmt="grid")

        return transaction_string
