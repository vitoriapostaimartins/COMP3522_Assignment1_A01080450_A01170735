"""
This module holds the Rebel user type.
"""
from notifications import Notifications
from user import User


class Rebel(User):
    """
    Class that represents a Rebel user type.
    """
    def __init__(self, name, age):
        """
        Initialize a User of Rebel type.
        :param name: the name of the user as a String
        :param age: the age of the Rebel User
        """
        super().__init__(name, age, 50, True, 100)

    def can_lock_account(self):
        """
        Return True or False, for whether an Rebel's account can be locked.
        :return: True if the user has 2 or more locked budgets, False otherwise
        """
        if super().locked_budgets >= 2:
            return True
        return False

    def get_type(self):
        """
        Return "Rebel" as the user type.
        :return: user type as a string
        """
        return "Rebel"

    def get_notification(self):
        """
        Return a rude notification.
        :return: rude notification as a string
        """
        return Notifications.RUDE.value
