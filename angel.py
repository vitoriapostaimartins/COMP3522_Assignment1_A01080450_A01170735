from notifications import Notifications
from user import User


class Angel(User):

    def __init__(self, name, age):
        super().__init__(name, age, 90)


    def get_type(self):
        return "Angel"

    def get_notification(self):
        return Notifications.POLITE.value
