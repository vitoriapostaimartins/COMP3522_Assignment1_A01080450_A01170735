"""
This module holds the Troublemaker user type.
"""
from Assignments.Assignment1.notifications import Notifications
from user import User


class Troublemaker(User):
    """
    Class that represents a Troublemaker user type.
    """
    def __init__(self, name, age):
        """
        Initialize a User of Troublemaker type.
        :param name: the name of the user as a String
        :param age: the age of the Troublemaker User
        """
        super().__init__(name, age, 75, True, 120)

    def can_lock_account(self):
        """
        Return False, for whether a Troublemaker's account can be locked.
        :return: False as a boolean
        """
        return False

    def get_type(self):
        """
        Return "Troublemaker" as the user type.
        :return: user type as a string
        """
        return "Troublemaker"

    def get_notification(self):
        """
        Return a polite notification.
        :return: polite notification as a string
        """
        return Notifications.POLITE.value
