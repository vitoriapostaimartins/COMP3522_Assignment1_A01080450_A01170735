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

    def __str__(self):
        return f"\nCategory: {self._category}\n" \
               f"Time: {self._timestamp}\n" \
               f"Amount: {self._dollar_amount} \n" \
               f"Location: {self._purchase_location}\n"
