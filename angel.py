"""
This module holds the Angel user type.
"""
from notifications import Notifications
from user import User


class Angel(User):
    """
    Class that represents an Angel user type.
    """
    def __init__(self, name, age):
        """
        Initialize a User of Angel type.
        :param name: the name of the user as a String
        :param age: the age of the Angel User
        """
        super().__init__(name, age, 90, False, 0)

    def can_lock_account(self):
        """
        Return False, for whether an Angel's account can be locked.
        :return: False as a boolean
        """
        return False

    def get_type(self):
        """
        Return "Angel" as the user type.
        :return: user type as a string
        """
        return "Angel"

    def get_notification(self):
        """
        Return a polite notification.
        :return: polite notification as a string
        """
        return Notifications.POLITE.value
